# Content Moderation AI - Full Stack Deployment

A comprehensive AI-powered content moderation system with Flask backend and React frontend, featuring advanced machine learning models and rule-based filtering.

## 🚀 Features

- **AI-Powered Analysis**: Advanced ML models trained on millions of text samples
- **Multi-Layer Protection**: Combines rule-based filtering with ML predictions
- **Real-Time Processing**: Instant analysis with sub-second response times
- **Precise Classification**: Accurately identifies Safe, Toxic, and Spam content
- **Risk Assessment**: Comprehensive risk scoring from 0-100
- **Modern UI**: Clean, intuitive interface with Google Fonts Bricolage Grotesque

## 🏗️ Architecture

### Backend (Flask API)
- RESTful API endpoints for text analysis
- Integration of trained ML models and rule-based filters
- Risk assessment engine combining both approaches
- Model serving with proper error handling

### Frontend (React)
- Modern, responsive interface
- Real-time text analysis with visual feedback
- Risk score visualization and detailed breakdowns
- Professional, enterprise-ready design

## 📋 Prerequisites

- Python 3.8+
- Node.js 16+
- npm or yarn

## 🛠️ Installation & Setup

### 1. Backend Setup

```bash
# Navigate to deployment directory
cd "ieee deployment"

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Ensure model files exist in parent directory
# The following files should be present:
# - ../vectorizer.pkl
# - ../model.pkl
# - ../label_encoder.pkl
```

### 2. Frontend Setup

```bash
# Install Node.js dependencies
npm install

# Start development server
npm start
```

### 3. Running the Application

```bash
# Terminal 1: Start Flask backend
python app.py

# Terminal 2: Start React frontend
npm start
```

The application will be available at:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:5000
- **Flask Landing**: http://localhost:5000

## 🔧 API Endpoints

### POST /api/analyze
Analyze text content for moderation.

**Request:**
```json
{
  "text": "Your text to analyze"
}
```

**Response:**
```json
{
  "success": true,
  "text": "Your text to analyze",
  "final_verdict": "Safe|Toxic|Spam",
  "risk_score": 85.5,
  "details": {
    "rule_triggered": "Offensive content, Spam patterns",
    "ml_prediction": "toxic",
    "ml_confidence": 0.892,
    "offensive_words": ["hate", "stupid"],
    "spam_patterns": ["URL detected"],
    "suspicious_patterns": ["Excessive capitalization"],
    "rule_score": 45.0,
    "ml_risk": 10.8,
    "reasoning": "ML: toxic (0.892), Rules: 45.0"
  }
}
```

### GET /api/health
Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "models_loaded": true
}
```

## 🎯 Content Classification

The system classifies content into three categories:

- **Safe**: Legitimate, appropriate content that meets community standards
- **Toxic**: Offensive, harmful, or inappropriate material including hate speech and threats
- **Spam**: Promotional material, scams, and unwanted commercial content

## 🔍 Analysis Features

### Rule-Based Detection
- Offensive keyword detection
- Spam pattern recognition (URLs, emails, phone numbers)
- Character pattern analysis (capitalization, repetition, punctuation)
- Promotional content identification

### Machine Learning
- Ensemble model combining multiple algorithms
- TF-IDF vectorization for text processing
- Confidence scoring for predictions
- Trained on 2M+ text samples

### Risk Assessment
- Combined scoring from rules and ML
- 0-100 risk scale
- Detailed breakdown of detected issues
- Confidence-weighted final decisions

## 🚀 Deployment

### Production Deployment

1. **Build React Frontend:**
```bash
npm run build
```

2. **Deploy Flask Backend:**
```bash
# Using Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# Or using Docker
docker build -t content-moderation-ai .
docker run -p 5000:5000 content-moderation-ai
```

3. **Environment Variables:**
```bash
export FLASK_ENV=production
export FLASK_DEBUG=False
```

## 📁 Project Structure

```
ieee deployment/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── package.json          # Node.js dependencies
├── templates/            # Flask templates
│   └── index.html
├── public/               # React public files
│   └── index.html
├── src/                  # React source code
│   ├── App.js
│   ├── App.css
│   ├── index.js
│   ├── index.css
│   └── components/       # React components
│       ├── Header.js
│       ├── TextAnalyzer.js
│       ├── AnalysisResult.js
│       ├── Features.js
│       └── Footer.js
└── README.md
```

## 🔧 Configuration

### Model Files
Ensure the following model files are present in the parent directory:
- `vectorizer.pkl` - TF-IDF vectorizer
- `model.pkl` - Trained ensemble model
- `label_encoder.pkl` - Label encoder for class mapping

### Environment Variables
- `FLASK_ENV` - Flask environment (development/production)
- `FLASK_DEBUG` - Debug mode (True/False)
- `PORT` - Port number (default: 5000)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.


## 🙏 Acknowledgments

- Built with Flask and React
- Uses scikit-learn for machine learning
- Google Fonts Bricolage Grotesque for typography
- Lucide React for icons
- Framer Motion for animations
