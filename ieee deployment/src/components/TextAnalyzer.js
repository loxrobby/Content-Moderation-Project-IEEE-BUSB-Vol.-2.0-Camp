import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Send, Loader, FileText, Lightbulb } from 'lucide-react';
import './TextAnalyzer.css';

const TextAnalyzer = ({ onAnalyze, isAnalyzing }) => {
  const [text, setText] = useState('');
  const [charCount, setCharCount] = useState(0);

  // Categorized suggestions
  const suggestions = {
    safe: [
      "This is a nice day and I hope everyone is well",
      "I disagree with your opinion but respect it",
      "Great work on this project, well done!",
      "Thank you for sharing your thoughts on this topic"
    ],
    toxic: [
      "You are stupid and don't know anything",
      "Fuck you bitch, go to hell",
      "Go kill yourself you worthless piece of shit",
      "You're an idiot and I hate you"
    ],
    spam: [
      "Check out this amazing deal at http://fake-deals-now.com! Free money guaranteed!",
      "Click here for free money! Limited time offer!",
      "URGENT: You've won $1000! Click now to claim!",
      "Buy now! Amazing deals! Don't miss out!"
    ]
  };

  const handleTextChange = (e) => {
    const newText = e.target.value;
    setText(newText);
    setCharCount(newText.length);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (text.trim() && !isAnalyzing) {
      onAnalyze(text.trim());
    }
  };

  const handleClear = () => {
    setText('');
    setCharCount(0);
  };

  const handleKeyDown = (e) => {
    // Submit on Enter (but not Shift+Enter for new lines)
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      if (text.trim() && !isAnalyzing) {
        onAnalyze(text.trim());
      }
    }
  };

  const handleSuggestionClick = (suggestionText) => {
    setText(suggestionText);
    setCharCount(suggestionText.length);
  };

  const isTextValid = text.trim().length > 0;
  const isOverLimit = charCount > 1000;

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
      className="text-analyzer"
    >
      <div className="analyzer-card">
        <div className="analyzer-header">
          <FileText className="analyzer-icon" />
          <h2 className="analyzer-title">Text Analysis</h2>
          <p className="analyzer-description">
            Enter text to analyze for content moderation using ML (70%) + rule-based (30%) detection
          </p>
        </div>

        <form onSubmit={handleSubmit} className="analyzer-form">
          <div className="input-container">
            <div className="input-group">
              <textarea
                value={text}
                onChange={handleTextChange}
                onKeyDown={handleKeyDown}
                placeholder="Enter text to analyze for toxicity, spam, or safety... (Press Enter to submit)"
                className={`text-input ${isOverLimit ? 'error' : ''}`}
                rows={6}
                maxLength={2000}
                disabled={isAnalyzing}
              />
              <div className="input-footer">
                <span className={`char-count ${isOverLimit ? 'error' : ''}`}>
                  {charCount}/2000 characters
                </span>
                {text && (
                  <button
                    type="button"
                    onClick={handleClear}
                    className="clear-btn"
                    disabled={isAnalyzing}
                  >
                    Clear
                  </button>
                )}
              </div>
            </div>

            <div className="suggestions-panel">
              <div className="suggestions-header">
                <Lightbulb className="suggestions-icon" />
                <h3 className="suggestions-title">Try These Examples</h3>
              </div>
              
              <div className="suggestions-categories">
                {Object.entries(suggestions).map(([category, items]) => (
                  <div key={category} className="suggestion-category">
                    <h4 className={`category-title category-${category}`}>
                      {category.charAt(0).toUpperCase() + category.slice(1)}
                    </h4>
                    <div className="suggestion-items">
                      {items.map((suggestion, index) => (
                        <button
                          key={index}
                          type="button"
                          className={`suggestion-item suggestion-${category}`}
                          onClick={() => handleSuggestionClick(suggestion)}
                          disabled={isAnalyzing}
                        >
                          {suggestion}
                        </button>
                      ))}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>

          <div className="submit-group">
            <motion.button
              type="submit"
              className={`submit-btn ${!isTextValid || isAnalyzing ? 'disabled' : ''}`}
              disabled={!isTextValid || isAnalyzing || isOverLimit}
              whileHover={isTextValid && !isAnalyzing && !isOverLimit ? { scale: 1.02 } : {}}
              whileTap={isTextValid && !isAnalyzing && !isOverLimit ? { scale: 0.98 } : {}}
            >
              {isAnalyzing ? (
                <>
                  <Loader className="btn-icon spinning" />
                  Analyzing...
                </>
              ) : (
                <>
                  <Send className="btn-icon" />
                  Analyze Text
                </>
              )}
            </motion.button>
          </div>
        </form>

        {isOverLimit && (
          <div className="error-message">
            Text exceeds the maximum length of 2000 characters
          </div>
        )}
      </div>
    </motion.div>
  );
};

export default TextAnalyzer;
