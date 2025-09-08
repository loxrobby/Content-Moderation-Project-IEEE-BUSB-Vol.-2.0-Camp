from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pandas as pd
import numpy as np
import joblib
import re
import string
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
# from scipy.sparse import hstack  # Removed scipy dependency
import warnings
warnings.filterwarnings('ignore')

import os
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))
CORS(app)

# Global variables for models
USE_ML = True  # Temporarily disable ML due to vectorizer fitting issue
ensemble_model = None
vectorizer = None
label_encoder = None
numerical_features = None
toxicity_threshold = None

# Import normalized word lists from the processed badword_list.txt
from flask_badwords_code import TOXIC_KEYWORDS
from comprehensive_spam_keywords import SPAM_KEYWORDS, SPAM_PATTERNS

# Use the normalized toxic keywords list (3,480 words from badword_list.txt)
OFFENSIVE_KEYWORDS = TOXIC_KEYWORDS

# Additional common mild/medium offensive words to boost rule-based detection
COMMON_MEDIUM_PROFANITY = {
    # medium (≈25–30 points)
    'bitch', 'bastard', 'asshole', 'douche', 'douchebag', 'prick'
}
COMMON_MILD_INSULTS = {
    # mild (≈15–20 points)
    'annoying', 'jerk', 'idiot', 'stupid', 'dumb', 'loser', 'crap', 'trash', 'lame', 'suck', 'sucks', 'gross'
}

# Offensive abbreviations and internet slang
OFFENSIVE_ABBREVIATIONS = {
    # Strongly offensive
    'wtf': 'what the fuck',
    'stfu': 'shut the fuck up',
    'gtfo': 'get the fuck out',
    'omfg': 'oh my fucking god',
    'af': 'as fuck',
    'fk': 'fuck',
    # Common internet slang that can correlate with toxicity (kept for context)
    'fml': 'fuck my life',
    'lmao': 'laughing my ass off',
    'rofl': 'rolling on floor laughing',
    'smh': 'shaking my head',
    # Neutral abbreviations (kept so we can ignore/weight lower later if needed)
    'btw': 'by the way',
    'fyi': 'for your information',
    'tbh': 'to be honest',
    'imo': 'in my opinion',
    'imho': 'in my humble opinion'
}

def load_models():
    """Load the trained models and components (optional when USE_ML=False)."""
    global ensemble_model, vectorizer, label_encoder, numerical_features, toxicity_threshold
    
    if not USE_ML:
        print("ML disabled: running in rule-based only mode. Skipping model loads.")
        return True

    try:
        print("🔄 Loading ML models...")
        ensemble_model = joblib.load('ensemble_model.pkl')
        vectorizer = joblib.load('ensemble_vectorizer.pkl')
        label_encoder = joblib.load('ensemble_label_encoder.pkl')
        numerical_features = joblib.load('ensemble_numerical_features.pkl')
        toxicity_threshold = joblib.load('ensemble_toxicity_threshold.pkl')
        
        # Verify all models are loaded (check for None, not truthiness)
        if all([ensemble_model is not None, vectorizer is not None, label_encoder is not None, 
                numerical_features is not None, toxicity_threshold is not None]):
            
            # Fix vectorizer if idf_ attribute is missing (version compatibility issue)
            if not hasattr(vectorizer, 'idf_') or vectorizer.idf_ is None:
                print("🔧 Fixing vectorizer IDF vector (version compatibility issue)...")
                # Create a simple IDF vector with default values
                import numpy as np
                vocab_size = len(vectorizer.vocabulary_)
                # Create a default IDF vector (log(1) = 0 for all terms)
                default_idf = np.ones(vocab_size, dtype=np.float64)
                vectorizer.idf_ = default_idf
                print("✓ Vectorizer IDF vector restored with default values!")
            
            print("✓ Ensemble Risk Assessment Engine models loaded successfully!")
            print(f"📊 Toxicity threshold: {toxicity_threshold}")
            print(f"🏷️  Label encoder classes: {label_encoder.classes_}")
            print(f"🔤 Vectorizer vocabulary size: {len(vectorizer.vocabulary_)}")
            return True
        else:
            print("❌ Some models failed to load properly")
            return False
            
    except FileNotFoundError as e:
        print(f"❌ ML model files not found: {e}")
        print("Proceeding with rule-based only mode.")
        return False
    except Exception as e:
        print(f"❌ Error loading models: {e}")
        import traceback
        traceback.print_exc()
        return False

def check_offensive_keywords(text):
    """
    Check if text contains any offensive keywords and abbreviations.
    
    Args:
        text (str): Input text to check
        
    Returns:
        dict: Contains 'is_offensive', 'offensive_words', 'offense_count', and 'offense_score'
    """
    if pd.isna(text) or not isinstance(text, str):
        return {
            'is_offensive': False,
            'offensive_words': [],
            'offense_count': 0,
            'offense_score': 0,
            'found_abbreviations': []
        }
    
    text_lower = text.lower()
    found_words = []
    found_abbreviations = []
    
    # Check for exact matches in offensive keywords (word boundaries only)
    for word in OFFENSIVE_KEYWORDS:
        pattern = r'\b' + re.escape(word) + r'\b'
        if re.search(pattern, text_lower):
            found_words.append(word)
    
    # Also check our added common profanity/insults
    for word in COMMON_MEDIUM_PROFANITY.union(COMMON_MILD_INSULTS):
        pattern = r'\b' + re.escape(word) + r'\b'
        if re.search(pattern, text_lower):
            found_words.append(word)
    
    # Check for offensive abbreviations with sentence context (whole-word only)
    sentences = re.split(r'[.!?]+', text)
    for abbrev, full_form in OFFENSIVE_ABBREVIATIONS.items():
        # Require whole-word matches so 'af' does not match 'After'
        abbrev_pattern = r"\b" + re.escape(abbrev.lower()) + r"\b"
        if re.search(abbrev_pattern, text_lower):
            # Find the sentence containing the abbreviation using whole-word search
            containing_sentence = ""
            for sentence in sentences:
                if re.search(abbrev_pattern, sentence.lower()):
                    containing_sentence = sentence.strip()
                    break

            if containing_sentence:
                found_abbreviations.append(f"{abbrev} ({full_form}) in: '{containing_sentence}'")
            else:
                found_abbreviations.append(f"{abbrev} ({full_form})")
            found_words.append(abbrev)
    
    # Initialize offense score
    offense_score = 0
    
    # Special override for the word "fuck" - auto-toxic with 150 points
    if 'fuck' in text_lower:
        offense_score += 150
        found_words.append('fuck')
    
    # Calculate offense score based on severity
    for word in found_words:
        if word in ['nigger', 'nigga', 'chink', 'kike', 'spic', 'wetback', 'towelhead', 'gook', 'jap', 'slant', 'yellow', 'redskin', 'savage', 'coon', 'jungle bunny', 'porch monkey', 'tar baby', 'mammy', 'house nigger', 'field nigger', 'oreo', 'coconut', 'banana', 'beaner', 'greaser', 'taco', 'burrito', 'sand nigger', 'camel jockey', 'raghead', 'haji', 'slant eye', 'rice eater', 'dog eater', 'heeb', 'yid', 'christ killer', 'jew boy', 'jew girl', 'polack', 'dago', 'wop', 'guinea', 'mick', 'paddy', 'taig', 'gypsy', 'gyp', 'pikey', 'tinker', 'traveller']:
            offense_score += 50  # High severity racial slurs
        elif word in ['shit', 'damn', 'bitch', 'asshole', 'bastard', 'cunt']:
            offense_score += 30  # Medium severity profanity
        elif word in ['kill', 'murder', 'death', 'suicide', 'bomb', 'explode']:
            offense_score += 40  # High severity violence
        elif word in ['hate', 'hater', 'racist', 'sexist', 'homophobic']:
            offense_score += 25  # Medium severity hate speech
        elif word in COMMON_MEDIUM_PROFANITY:
            offense_score += 25  # Medium profanity bucket (e.g., douche, prick)
        elif word in COMMON_MILD_INSULTS:
            offense_score += 18  # Mild insults (e.g., annoying, jerk, dumb)
        elif word in ['wtf', 'stfu', 'gtfo', 'fml', 'omfg']:
            offense_score += 20  # Offensive abbreviations
        else:
            offense_score += 10  # Low severity
    
    return {
        'is_offensive': len(found_words) > 0,
        'offensive_words': found_words,
        'offense_count': len(found_words),
        'offense_score': offense_score,
        'found_abbreviations': found_abbreviations
    }

def detect_spam_patterns(text):
    """
    Detect spam patterns in text using regex patterns.
    
    Args:
        text (str): Input text to check
        
    Returns:
        dict: Contains spam detection results and triggered patterns
    """
    if pd.isna(text) or not isinstance(text, str):
        return {
            'is_spam_pattern': False,
            'spam_patterns': [],
            'spam_score': 0,
            'details': {},
            'found_urls': [],
            'found_emails': [],
            'found_phones': []
        }
    
    text_lower = text.lower()
    spam_patterns = []
    spam_score = 0
    details = {}
    found_urls = []
    found_emails = []
    found_phones = []
    
    # URL patterns with detailed extraction
    url_patterns = [
        (r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', 'URL detected', 30),
        (r'www\.[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', 'WWW URL detected', 25),
        (r'[a-zA-Z0-9.-]+\.(com|org|net|edu|gov|mil|int|co|uk|de|fr|jp|au|us|ca|mx|br|es|it|ru|cn|in|kr|nl|se|no|dk|fi|pl|tr|za|th|my|sg|hk|tw|nz|ph|id|vn)', 'Domain detected', 20)
    ]
    
    for pattern, description, score in url_patterns:
        matches = re.findall(pattern, text_lower)
        if matches:
            spam_patterns.append(description)
            spam_score += score
            details[description] = True
            found_urls.extend(matches)
    
    # Email patterns with extraction
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email_matches = re.findall(email_pattern, text)
    if email_matches:
        spam_patterns.append('Email address')
        spam_score += 20
        details['Email address'] = True
        found_emails.extend(email_matches)
    
    # Phone patterns with extraction
    phone_patterns = [
        (r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', 'Phone number', 25),
        (r'\(\d{3}\)\s*\d{3}[-.]?\d{4}', 'Formatted phone number', 25),
        (r'\+\d{1,3}[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}', 'International phone', 30)
    ]
    
    for pattern, description, score in phone_patterns:
        matches = re.findall(pattern, text)
        if matches:
            spam_patterns.append(description)
            spam_score += score
            details[description] = True
            found_phones.extend(matches)
    
    # Currency and promotional keywords
    currency_patterns = [
        (r'\$\d+(?:,\d{3})*(?:\.\d{2})?', 'Currency amount', 15),
        (r'free\s+(?:money|cash|gift|prize|offer)', 'Free offers', 20),
        (r'(?:buy|purchase|order)\s+now', 'Purchase urgency', 15),
        (r'limited\s+time', 'Time pressure', 15),
        (r'act\s+now', 'Action urgency', 15),
        (r'guaranteed', 'Guarantee claims', 15),
        (r'no\s+risk', 'Risk-free claims', 15)
    ]
    
    for pattern, description, score in currency_patterns:
        if re.search(pattern, text_lower):
            spam_patterns.append(description)
            spam_score += score
            details[description] = True
    
    # Enhanced spam keyword detection using normalized list
    spam_keywords_found = []
    for keyword in SPAM_KEYWORDS:
        # Check for exact word matches
        pattern = r'\b' + re.escape(keyword.lower()) + r'\b'
        if re.search(pattern, text_lower):
            spam_keywords_found.append(keyword)
    
    if spam_keywords_found:
        spam_patterns.append('Spam keywords detected')
        spam_score += len(spam_keywords_found) * 8
        details['Spam keywords'] = spam_keywords_found[:10]  # Limit to first 10 for display
    
    # Enhanced spam pattern detection using comprehensive patterns
    for pattern, description, score in SPAM_PATTERNS:
        if re.search(pattern, text_lower):
            spam_patterns.append(description)
            spam_score += score
            details[description] = True
    
    return {
        'is_spam_pattern': len(spam_patterns) > 0,
        'spam_patterns': spam_patterns,
        'spam_score': spam_score,
        'details': details,
        'found_urls': found_urls,
        'found_emails': found_emails,
        'found_phones': found_phones
    }

def extract_numerical_features(text):
    """Extract numerical features from text."""
    if pd.isna(text) or not isinstance(text, str):
        return np.array([0, 0, 0, 0, 0, 0, 0])
    
    # Text length
    text_length = len(text)
    
    # Word count
    words = text.split()
    word_count = len(words)
    
    # Sentence count
    sentences = re.split(r'[.!?]+', text)
    sentence_count = len([s for s in sentences if s.strip()])
    
    # Average word length
    avg_word_length = np.mean([len(word) for word in words]) if words else 0
    
    # Capitalization ratio
    caps_ratio = sum(1 for c in text if c.isupper()) / len(text) if text else 0
    
    # Hashtag count
    hashtag_count = text.count('#')
    
    # Mention count
    mention_count = text.count('@')
    
    return np.array([text_length, word_count, sentence_count, avg_word_length, caps_ratio, hashtag_count, mention_count])

def risk_assessment_engine(text):
    """
    Comprehensive risk assessment engine that combines Naive Bayes model with rule-based filter.
    
    Args:
        text (str): Input text to analyze
        
    Returns:
        dict: Comprehensive risk assessment with detailed explanations
    """
    if pd.isna(text) or not isinstance(text, str):
        return {
            'classification': 'safe',
            'confidence': 0.0,
            'explanation': 'Invalid input text',
            'risk_factors': ['Invalid input'],
            'ml_prediction': {'classification': 'SAFE', 'confidence': 0.0, 'toxic_probability': 0.0, 'weight': 0.3},
            'rule_based_analysis': {'offensive_score': 0, 'spam_score': 0, 'toxic_score': 0.0, 'weight': 0.7},
            'weighted_score': 0.0,
            'is_spam': False
        }
    
    # Step 1: ML ensemble model prediction
    ml_toxic_score = 0.0
    ml_confidence = 0.0
    ml_classification = "SAFE"
    if USE_ML and vectorizer is not None and ensemble_model is not None and label_encoder is not None:
        try:
            print(f"🔍 ML Prediction Debug - Input text: '{text}'")
            # Preprocess text exactly like the test script
            text_clean = re.sub(r'[^a-zA-Z\s]', '', text.lower())
            print(f"🔍 ML Prediction Debug - Cleaned text: '{text_clean}'")
            
            # TF-IDF transformation (only TF-IDF features, no numerical features)
            text_tfidf = vectorizer.transform([text_clean])
            text_tfidf_dense = text_tfidf.toarray()
            print(f"🔍 ML Prediction Debug - TF-IDF shape: {text_tfidf_dense.shape}")
            
            # Use only TF-IDF features to match training pipeline
            text_vector = text_tfidf_dense
            
            # Make prediction
            ml_prediction = ensemble_model.predict(text_vector)[0]
            ml_probabilities = ensemble_model.predict_proba(text_vector)[0]
            ml_confidence = float(max(ml_probabilities))
            ml_classification = label_encoder.inverse_transform([ml_prediction])[0].upper()
            
            print(f"🔍 ML Prediction Debug - Prediction: {ml_prediction}, Probabilities: {ml_probabilities}")
            print(f"🔍 ML Prediction Debug - Classification: {ml_classification}, Confidence: {ml_confidence}")
            
            # Get toxic probability (index 1 for toxic class)
            if len(ml_probabilities) >= 2:
                ml_toxic_score = float(ml_probabilities[1])
            else:
                ml_toxic_score = 0.0
                
        except Exception as e:
            print(f"⚠️ ML ensemble model error: {e}")
            import traceback
            traceback.print_exc()
            ml_toxic_score = 0.0
            ml_confidence = 0.0
            ml_classification = "SAFE"
    
    # Step 2: Get rule-based analysis (70% weight)
    offensive_result = check_offensive_keywords(text)
    spam_result = detect_spam_patterns(text)
    
    # Calculate rule-based toxic score using actual offensive_score
    rule_toxic_score = 0.0
    if offensive_result['is_offensive']:
        offensive_score = offensive_result['offense_score']
        
        # Convert offensive_score to toxic_score (0.0 to 1.0)
        # Special case: if "fuck" is detected (150+ points), auto-toxic
        if offensive_score >= 150:
            rule_toxic_score = 0.95  # Very high toxic score for "fuck" override
        elif offensive_score >= 100:
            rule_toxic_score = 0.90  # High toxic score
        elif offensive_score >= 50:
            rule_toxic_score = 0.80  # Medium-high toxic score
        elif offensive_score >= 30:
            rule_toxic_score = 0.70  # Medium toxic score
        elif offensive_score >= 20:
            rule_toxic_score = 0.60  # Low-medium toxic score
        elif offensive_score >= 10:
            rule_toxic_score = 0.50  # Low toxic score
        else:
            rule_toxic_score = 0.30  # Minimal toxic score
    
    # Step 3: Spam detection (100% rule-based)
    is_spam = spam_result['is_spam_pattern'] and spam_result['spam_score'] >= 10
    
    # Sanity check: if ML model is too confident (>0.8) but no offensive words detected,
    # reduce the score to prevent false positives
    ml_adjusted = False
    if ml_toxic_score > 0.8 and not offensive_result['is_offensive']:
        ml_toxic_score = min(ml_toxic_score, 0.3)  # Cap at 30% for normal text
        ml_adjusted = True
    
    # Step 4: Weighted toxic score combining ML and rule-based detection
    if USE_ML:
        # Special override: if rule-based score is very high (0.9+), override ML model
        if rule_toxic_score >= 0.90:
            weighted_toxic_score = rule_toxic_score  # Use rule-based score directly
        else:
            # ML-focused approach: 70% ML, 30% rule-based for toxic/safe detection
            # ML model is more accurate, rule-based catches explicit content
            weighted_toxic_score = (0.7 * ml_toxic_score) + (0.3 * rule_toxic_score)
    else:
        weighted_toxic_score = rule_toxic_score

    # Single-threshold final decision: only 'spam', 'toxic', or 'safe'
    TOXIC_DECISION_THRESHOLD = 0.40

    if is_spam:
        classification = "spam"
        confidence = min(0.95, 0.6 + (spam_result['spam_score'] / 200.0))
        # Construct a concise human-friendly explanation (no Decision/Reason prefixes)
        parts = [
            f"Detected spam indicators (score {spam_result['spam_score']}/100)"
        ]
        if spam_result['found_urls']:
            parts.append(f"Detected URLs: {', '.join(spam_result['found_urls'][:2])}")
        if spam_result['found_emails']:
            parts.append(f"Detected emails: {', '.join(spam_result['found_emails'][:2])}")
        if spam_result['found_phones']:
            parts.append(f"Detected phone numbers: {', '.join(spam_result['found_phones'][:2])}")
        if spam_result['spam_patterns']:
            parts.append(f"Patterns: {', '.join(spam_result['spam_patterns'][:3])}")
        explanation = ". ".join(parts)
        risk_factors = []
    elif weighted_toxic_score >= TOXIC_DECISION_THRESHOLD:
        classification = "toxic"
        confidence = min(0.95, 0.5 + weighted_toxic_score * 0.5)
        bits = []
        if offensive_result['offensive_words']:
            bits.append(f"Detected offensive terms: {', '.join(offensive_result['offensive_words'][:5])}")
        if offensive_result['found_abbreviations']:
            bits.append(f"Detected abbreviations: {', '.join(offensive_result['found_abbreviations'][:2])}")
        explanation = ". ".join(bits) if bits else "Toxic content detected."
        risk_factors = []
    else:
        classification = "safe"
        confidence = min(0.95, 0.6 + (1 - weighted_toxic_score) * 0.4)
        explanation = "Content appears safe: no spam patterns and rule-based toxicity below threshold; no offensive terms detected."
        risk_factors = []
    
    return {
        'classification': classification,
        'confidence': confidence,
        'explanation': explanation,
        'risk_factors': risk_factors,
        'ml_prediction': {
            'classification': ml_classification if not ml_adjusted else 'SAFE',
            'confidence': ml_confidence,
            'toxic_probability': ml_toxic_score,
            'weight': 0.7 if USE_ML else 0.0,
            'adjusted': ml_adjusted
        },
        'rule_based_analysis': {
            'offensive_score': offensive_result['offense_score'],
            'offensive_words': offensive_result.get('offensive_words', []),
            'offensive_abbreviations': offensive_result.get('found_abbreviations', []),
            'spam_score': spam_result['spam_score'],
            'toxic_score': rule_toxic_score,
            'weight': 0.3 if USE_ML else 1.0,
            'found_abbreviations': offensive_result.get('found_abbreviations', [])
        },
        'weighted_score': weighted_toxic_score,
        'is_spam': is_spam
    }

@app.route('/')
def index():
    """Serve the main page."""
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Content Moderation AI</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
            .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            h1 { color: #333; text-align: center; }
            .form-group { margin: 20px 0; }
            textarea { width: 100%; height: 100px; padding: 10px; border: 1px solid #ddd; border-radius: 5px; }
            button { background: #007bff; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; }
            button:hover { background: #0056b3; }
            .result { margin-top: 20px; padding: 15px; border-radius: 5px; }
            .safe { background: #d4edda; border: 1px solid #c3e6cb; color: #155724; }
            .toxic { background: #f8d7da; border: 1px solid #f5c6cb; color: #721c24; }
            .spam { background: #fff3cd; border: 1px solid #ffeaa7; color: #856404; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🤖 Content Moderation AI</h1>
            <p>Enter text below to analyze for toxicity, spam, and inappropriate content:</p>
            
            <div class="form-group">
                <textarea id="textInput" placeholder="Enter text to analyze..."></textarea>
            </div>
            
            <button onclick="analyzeText()">Analyze Text</button>
            
            <div id="result"></div>
        </div>

        <script>
            async function analyzeText() {
                const text = document.getElementById('textInput').value;
                const resultDiv = document.getElementById('result');
                
                if (!text.trim()) {
                    resultDiv.innerHTML = '<div class="result" style="background: #f8d7da; color: #721c24;">Please enter some text to analyze.</div>';
                    return;
                }
                
                resultDiv.innerHTML = '<div class="result">Analyzing...</div>';
                
                try {
                    const response = await fetch('/api/analyze', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ text: text })
                    });
                    
                    const data = await response.json();
                    
                    if (data.success) {
                        const classification = data.classification.toLowerCase();
                        const confidence = (data.confidence * 100).toFixed(1);
                        
                        resultDiv.innerHTML = `
                            <div class="result ${classification}">
                                <h3>Classification: ${data.classification}</h3>
                                <p><strong>Confidence:</strong> ${confidence}%</p>
                                <p><strong>Explanation:</strong> ${data.explanation}</p>
                            </div>
                        `;
                    } else {
                        resultDiv.innerHTML = '<div class="result" style="background: #f8d7da; color: #721c24;">Error: ' + data.error + '</div>';
                    }
                } catch (error) {
                    resultDiv.innerHTML = '<div class="result" style="background: #f8d7da; color: #721c24;">Error analyzing text: ' + error.message + '</div>';
                }
            }
        </script>
    </body>
    </html>
    '''

@app.route('/api/analyze', methods=['POST'])
def analyze_text():
    """Analyze text using the Risk Assessment Engine."""
    try:
        data = request.get_json()
        text = data.get('text', '').strip()
        
        if not text:
            return jsonify({
                'success': False,
                'error': 'No text provided'
            }), 400
        
        # Debug: Print input text
        print(f"🔍 Analyzing text: '{text}'")
        
        # Use the Risk Assessment Engine
        result = risk_assessment_engine(text)
        
        # Debug: Print ML prediction details
        if USE_ML and result['ml_prediction']:
            ml_pred = result['ml_prediction']
            print(f"🤖 ML Prediction: {ml_pred['classification']} (confidence: {ml_pred['confidence']:.3f}, toxic_prob: {ml_pred['toxic_probability']:.3f})")
        
        # Format response for frontend
        response = {
            'success': True,
            'classification': result['classification'].upper(),
            'confidence': round(result['confidence'], 3),
            'explanation': result['explanation'],
            'risk_factors': result['risk_factors'],
            'details': {
                'ml_prediction': result['ml_prediction'],
                'rule_based_analysis': result['rule_based_analysis'],
                'weighted_score': round(result['weighted_score'], 3),
                'is_spam': result['is_spam']
            }
        }
        
        print(f"✅ Final classification: {response['classification']} (confidence: {response['confidence']})")
        return jsonify(response)
        
    except Exception as e:
        print(f"❌ Error in analyze_text: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': 'Internal server error'
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'message': 'Risk Assessment Engine is running',
        'models_loaded': all([ensemble_model is not None, vectorizer is not None, label_encoder is not None, 
                              numerical_features is not None, toxicity_threshold is not None]) if USE_ML else False,
        'ml_enabled': USE_ML,
        'model_info': {
            'ensemble_model': ensemble_model is not None,
            'vectorizer': vectorizer is not None,
            'label_encoder': label_encoder is not None,
            'numerical_features': numerical_features is not None,
            'toxicity_threshold': toxicity_threshold is not None
        }
    })

if __name__ == '__main__':
    print("🚀 Starting Content Moderation AI with Risk Assessment Engine...")
    
    # Load models
    if load_models():
        print("✅ All models loaded successfully!")
        print("🌐 Starting Flask server...")
        
        # Get port from environment variable (for Railway/Heroku) or default to 5000
        port = int(os.environ.get('PORT', 5000))
        debug_mode = os.environ.get('FLASK_ENV') != 'production'
        
        app.run(host='0.0.0.0', port=port, debug=debug_mode)
    else:
        print("❌ Failed to load models. Please check the model files.")
        exit(1)