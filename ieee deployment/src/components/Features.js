import React from 'react';
import { motion } from 'framer-motion';
import { 
  Brain, 
  Shield, 
  Zap, 
  Target, 
  BarChart3, 
  Clock,
  CheckCircle,
  AlertTriangle,
  Filter
} from 'lucide-react';
import './Features.css';

const Features = () => {
  const features = [
    {
      icon: <Brain className="feature-icon" />,
      title: "AI-Powered Analysis (70% weight)",
      description: "Advanced ensemble ML models with 100% test accuracy, providing primary detection with high precision.",
      color: "#667eea"
    },
    {
      icon: <Shield className="feature-icon" />,
      title: "Rule-Based Protection (30% weight)",
      description: "Explicit keyword matching and pattern recognition for clear offensive content and spam detection.",
      color: "#10b981"
    },
    {
      icon: <Zap className="feature-icon" />,
      title: "Real-Time Processing",
      description: "Instant analysis with sub-second response times for seamless user experience.",
      color: "#f59e0b"
    },
    {
      icon: <Target className="feature-icon" />,
      title: "Precise Classification",
      description: "Accurately identifies Safe, Toxic, and Spam content with detailed confidence scores.",
      color: "#ef4444"
    },
    {
      icon: <BarChart3 className="feature-icon" />,
      title: "Risk Assessment",
      description: "Comprehensive risk scoring from 0-100 with detailed breakdown of detected issues.",
      color: "#8b5cf6"
    },
    {
      icon: <Clock className="feature-icon" />,
      title: "Always Available",
      description: "24/7 content moderation service with high availability and reliability.",
      color: "#06b6d4"
    }
  ];

  const capabilities = [
    {
      icon: <CheckCircle className="capability-icon" />,
      title: "Safe Content",
      description: "Legitimate, appropriate content that meets community standards"
    },
    {
      icon: <AlertTriangle className="capability-icon" />,
      title: "Toxic Content",
      description: "Offensive, harmful, or inappropriate material including hate speech and threats"
    },
    {
      icon: <Filter className="capability-icon" />,
      title: "Spam Content",
      description: "Promotional material, scams, and unwanted commercial content"
    }
  ];

  return (
    <div className="features">
      <div className="features-header">
        <h2 className="features-title">Advanced Content Moderation</h2>
        <p className="features-subtitle">
          Powered by cutting-edge AI (70% weight) and comprehensive rule-based systems (30% weight)
        </p>
      </div>

      <div className="features-grid">
        {features.map((feature, index) => (
          <motion.div
            key={index}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: index * 0.1 }}
            className="feature-card"
            whileHover={{ y: -5 }}
          >
            <div 
              className="feature-icon-container"
              style={{ backgroundColor: `${feature.color}20` }}
            >
              <div style={{ color: feature.color }}>
                {feature.icon}
              </div>
            </div>
            <h3 className="feature-title">{feature.title}</h3>
            <p className="feature-description">{feature.description}</p>
          </motion.div>
        ))}
      </div>

      <div className="capabilities-section">
        <h3 className="capabilities-title">Content Classification</h3>
        <p className="capabilities-subtitle">
          Our system can accurately identify and categorize different types of content
        </p>
        
        <div className="capabilities-grid">
          {capabilities.map((capability, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.5, delay: index * 0.1 }}
              className="capability-card"
            >
              <div className="capability-icon-container">
                {capability.icon}
              </div>
              <div className="capability-content">
                <h4 className="capability-title">{capability.title}</h4>
                <p className="capability-description">{capability.description}</p>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Features;
