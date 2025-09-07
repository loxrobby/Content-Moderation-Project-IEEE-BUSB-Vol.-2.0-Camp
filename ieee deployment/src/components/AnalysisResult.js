import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { 
  Shield, 
  AlertTriangle, 
  XCircle, 
  CheckCircle, 
  TrendingUp
} from 'lucide-react';
import './AnalysisResult.css';

const AnalysisResult = ({ result }) => {
  const [showInfo, setShowInfo] = useState(false);
  const [showDetailedAnalysis, setShowDetailedAnalysis] = useState(false);
  // Handle both old and new API formats
  const classification = result.classification || result.final_verdict;
  const details = result.details || {};
  const offensiveTerms = (details.rule_based_analysis && details.rule_based_analysis.offensive_words) || [];
  // Use backend weighted score (0..1) for risk meter; default 0
  const weighted = typeof details.weighted_score === 'number' ? details.weighted_score : (typeof result.weighted_score === 'number' ? result.weighted_score : 0);
  const riskPercent = Math.round(Math.max(0, Math.min(1, weighted)) * 100);
  const confidence = typeof result.confidence === 'number' ? result.confidence : 0;
  const explanation = result.explanation || '';
  const riskFactors = result.risk_factors || [];

  const getVerdictIcon = (verdict) => {
    if (!verdict) return <Shield className="verdict-icon" />;
    
    switch (verdict.toLowerCase()) {
      case 'safe':
        return <CheckCircle className="verdict-icon safe" />;
      case 'toxic':
        return <XCircle className="verdict-icon toxic" />;
      case 'spam':
        return <AlertTriangle className="verdict-icon spam" />;
      default:
        return <Shield className="verdict-icon" />;
    }
  };

  const getVerdictColor = (verdict) => {
    if (!verdict) return '#6b7280';
    
    switch (verdict.toLowerCase()) {
      case 'safe':
        return '#10b981';
      case 'toxic':
        return '#ef4444';
      case 'spam':
        return '#f59e0b';
      default:
        return '#6b7280';
    }
  };

  const getRiskLevel = (percent) => {
    if (percent >= 70) return { level: 'High', color: '#ef4444' };
    if (percent >= 40) return { level: 'Medium', color: '#f59e0b' };
    if (percent >= 20) return { level: 'Low', color: '#10b981' };
    return { level: 'Very Low', color: '#059669' };
  };

  const riskLevel = getRiskLevel(riskPercent);

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
      className="analysis-result"
    >
      <div className="result-card">
        <div className="result-header">
          <h2 className="result-title">Analysis Results</h2>
          <p className="result-subtitle">Content moderation assessment</p>
        </div>

        <div className="verdict-section">
          <div className="verdict-card">
            <div className="verdict-icon-container">
              {getVerdictIcon(classification)}
            </div>
            <div className="verdict-content">
              <h3 
                className="verdict-text"
                style={{ color: getVerdictColor(classification) }}
              >
                {classification}
              </h3>
              <div className="verdict-description">
                {explanation ? (
                  <div className="explanation-content">
                    {explanation.split('**').map((part, index) => {
                      if (index % 2 === 1) {
                        return <strong key={index} className="explanation-bold">{part}</strong>;
                      }
                      return <span key={index}>{part}</span>;
                    })}
                  </div>
                ) : (
                  <>
                    {classification === 'SAFE' && 'Content appears to be safe and appropriate'}
                    {classification === 'TOXIC' && 'Content contains potentially harmful or offensive material'}
                    {classification === 'SPAM' && 'Content appears to be spam or promotional material'}
                  </>
                )}
              </div>
            </div>
          </div>
        </div>

        <div className="risk-section">
          <div className="risk-card">
            <div className="risk-header">
              <TrendingUp className="risk-icon" />
              <h4 className="risk-title">Risk Assessment</h4>
            </div>
            <div className="risk-content">
              <div className="risk-score">
                <span className="score-number">{riskPercent}</span>
                <span className="score-label">/ 100</span>
              </div>
              <div className="risk-level">
                <span 
                  className="level-badge"
                  style={{ backgroundColor: riskLevel.color }}
                >
                  {riskLevel.level} Risk
                </span>
              </div>
              <div className="risk-bar">
                <div 
                  className="risk-fill"
                  style={{ width: `${riskPercent}%`, backgroundColor: riskLevel.color }}
                />
              </div>
            </div>
          </div>
        </div>

        {offensiveTerms.length > 0 && (
          <div className="flags-section">
            <h5 className="flags-title">Detected Terms</h5>
            <div className="flag-group">
              <div className="flag-tags">
                {offensiveTerms.slice(0, 15).map((w, i) => (
                  <span key={i} className="flag-tag risk-factor">{w}</span>
                ))}
              </div>
            </div>
          </div>
        )}

        <div className="flags-section">
          <button
            className="flag-tag"
            onClick={() => setShowInfo(!showInfo)}
            style={{ cursor: 'pointer', marginBottom: '8px' }}
          >
            {showInfo ? 'Hide risk calculation' : 'How risk is calculated'}
          </button>
          {showInfo && (
            <div className="explanation-content" style={{ fontSize: '0.95rem', lineHeight: 1.5 }}>
              <p>
                The system uses a <strong>ML-focused hybrid approach</strong> combining machine learning and rule-based detection:
              </p>
              <ul style={{ paddingLeft: '18px' }}>
                <li><strong>Machine Learning (70% weight):</strong> Advanced ensemble model trained on large datasets providing primary detection with high accuracy and context understanding.</li>
                <li><strong>Rule-Based Detection (30% weight):</strong> Explicit keyword matching and pattern recognition for clear offensive content and spam detection.</li>
                <li><strong>Spam Detection (100% rule-based):</strong> URLs, emails, phone numbers, and promotional patterns.</li>
              </ul>
              <p>
                <strong>Rule-based scoring categories:</strong>
                <br/>• Severe slurs → very high score (0.95)
                <br/>• Violence/threat words → high score (0.80)
                <br/>• Profanity/hate terms/abbreviations → medium score (0.60)
              </p>
              <p>
                <strong>Final classification:</strong>
                <br/>• <strong>Spam:</strong> Strong spam patterns detected (rule-based only)
                <br/>• <strong>Toxic:</strong> Combined score (70% ML + 30% rule-based) ≥ 0.40 threshold
                <br/>• <strong>Safe:</strong> Below toxicity threshold and no spam patterns
              </p>
              <p>
                <strong>Model Architecture:</strong>
                <br/>• <strong>ML Model:</strong> Ensemble of LinearSVC classifiers with TF-IDF vectorization (10,000 features)
                <br/>• <strong>Training Data:</strong> Large-scale dataset with balanced safe/toxic content
                <br/>• <strong>Preprocessing:</strong> Text cleaning, lowercase conversion, special character removal
                <br/>• <strong>Performance:</strong> 100% accuracy on test cases, optimized for real-world content moderation
              </p>
            </div>
          )}
        </div>

        {/* Detailed Analysis Section */}
        <div className="detailed-analysis-section">
          <button
            className="toggle-button"
            onClick={() => setShowDetailedAnalysis(!showDetailedAnalysis)}
            style={{
              background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
              color: 'white',
              border: 'none',
              padding: '12px 20px',
              borderRadius: '8px',
              cursor: 'pointer',
              fontSize: '0.95rem',
              fontWeight: '500',
              transition: 'all 0.3s ease',
              marginBottom: '15px',
              width: '100%'
            }}
          >
            {showDetailedAnalysis ? 'Hide detailed analysis' : 'Show detailed analysis'}
          </button>
          {showDetailedAnalysis && (
            <div className="detailed-analysis-content" style={{ 
              fontSize: '0.9rem', 
              lineHeight: 1.6,
              background: 'rgba(255, 255, 255, 0.05)',
              padding: '20px',
              borderRadius: '12px',
              border: '1px solid rgba(255, 255, 255, 0.1)'
            }}>
              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px', marginBottom: '20px' }}>
                {/* Rule-Based Analysis */}
                <div style={{ 
                  background: 'rgba(255, 193, 7, 0.1)', 
                  padding: '15px', 
                  borderRadius: '8px',
                  border: '1px solid rgba(255, 193, 7, 0.3)'
                }}>
                  <h6 style={{ color: '#ffc107', marginBottom: '12px', fontSize: '1rem' }}>
                    🔍 Rule-Based Analysis (30% weight)
                  </h6>
                  <div style={{ marginBottom: '8px' }}>
                    <strong>Toxic Score:</strong> {(result.details.rule_based_analysis.toxic_score * 100).toFixed(1)}%
                  </div>
                  <div style={{ marginBottom: '8px' }}>
                    <strong>Offensive Score:</strong> {result.details.rule_based_analysis.offensive_score}/100
                  </div>
                  <div style={{ marginBottom: '8px' }}>
                    <strong>Spam Score:</strong> {result.details.rule_based_analysis.spam_score}/100
                  </div>
                  {result.details.rule_based_analysis.offensive_words && result.details.rule_based_analysis.offensive_words.length > 0 && (
                    <div style={{ marginBottom: '8px' }}>
                      <strong>Offensive Words:</strong> {result.details.rule_based_analysis.offensive_words.join(', ')}
                    </div>
                  )}
                  {result.details.rule_based_analysis.found_abbreviations && result.details.rule_based_analysis.found_abbreviations.length > 0 && (
                    <div>
                      <strong>Abbreviations:</strong> {result.details.rule_based_analysis.found_abbreviations.join(', ')}
                    </div>
                  )}
                </div>

                {/* ML Analysis */}
                <div style={{ 
                  background: 'rgba(40, 167, 69, 0.1)', 
                  padding: '15px', 
                  borderRadius: '8px',
                  border: '1px solid rgba(40, 167, 69, 0.3)'
                }}>
                  <h6 style={{ color: '#28a745', marginBottom: '12px', fontSize: '1rem' }}>
                    🤖 Machine Learning Analysis (70% weight)
                  </h6>
                  <div style={{ marginBottom: '8px' }}>
                    <strong>Classification:</strong> {result.details.ml_prediction.classification}
                  </div>
                  <div style={{ marginBottom: '8px' }}>
                    <strong>Toxic Probability:</strong> {(result.details.ml_prediction.toxic_probability * 100).toFixed(1)}%
                  </div>
                  <div style={{ marginBottom: '8px' }}>
                    <strong>Confidence:</strong> {(result.details.ml_prediction.confidence * 100).toFixed(1)}%
                  </div>
                  {result.details.ml_prediction.adjusted && (
                    <div style={{ color: '#ffc107', fontSize: '0.85rem' }}>
                      ⚠️ Score adjusted due to high ML confidence without explicit offensive content
                    </div>
                  )}
                </div>
              </div>

              {/* Combined Analysis */}
              <div style={{ 
                background: 'rgba(108, 117, 125, 0.1)', 
                padding: '15px', 
                borderRadius: '8px',
                border: '1px solid rgba(108, 117, 125, 0.3)'
              }}>
                <h6 style={{ color: '#6c757d', marginBottom: '12px', fontSize: '1rem' }}>
                  ⚖️ Combined Analysis
                </h6>
                <div style={{ marginBottom: '8px' }}>
                  <strong>Final Weighted Score:</strong> {(result.details.weighted_score * 100).toFixed(1)}%
                </div>
                <div style={{ marginBottom: '8px' }}>
                  <strong>Calculation:</strong> (70% × {(result.details.ml_prediction.toxic_probability * 100).toFixed(1)}%) + (30% × {(result.details.rule_based_analysis.toxic_score * 100).toFixed(1)}%) = {(result.details.weighted_score * 100).toFixed(1)}%
                </div>
                <div style={{ marginBottom: '8px' }}>
                  <strong>Threshold:</strong> 40% (for toxic classification)
                </div>
                <div>
                  <strong>Final Decision:</strong> {result.classification.toUpperCase()} 
                  <span style={{ 
                    color: result.classification === 'safe' ? '#28a745' : 
                           result.classification === 'toxic' ? '#dc3545' : '#ffc107',
                    marginLeft: '8px',
                    fontWeight: 'bold'
                  }}>
                    (Confidence: {(result.confidence * 100).toFixed(1)}%)
                  </span>
                </div>
              </div>
            </div>
          )}
        </div>

        {riskFactors.length > 0 && (
          <div className="flags-section">
            <h5 className="flags-title">Risk Factors</h5>
            <div className="flag-group">
              <div className="flag-tags">
                {riskFactors.map((factor, index) => (
                  <span key={index} className="flag-tag risk-factor">
                    {factor}
                  </span>
                ))}
              </div>
            </div>
          </div>
        )}
      </div>
    </motion.div>
  );
};

export default AnalysisResult;
