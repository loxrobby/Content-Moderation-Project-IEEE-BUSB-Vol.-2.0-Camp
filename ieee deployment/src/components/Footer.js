import React from 'react';
import { Shield } from 'lucide-react';
import './Footer.css';

const Footer = () => {
  return (
    <footer className="footer">
      <div className="container">
        <div className="footer-content">
          <div className="footer-brand">
            <div className="footer-logo">
              <Shield className="footer-logo-icon" />
              <span className="footer-logo-text">ContentMod AI</span>
            </div>
            <p className="footer-description small">
              Advanced AI-powered content moderation system for safe and secure online communities.
            </p>
            <p className="footer-thanks">Special thanks to <strong>IEEE BUSB CAMP Vol 2.0</strong> for the camp and guidance.</p>
          </div>
        </div>
        
        <div className="footer-bottom">
          <p className="footer-copyright">© 2025 ContentMod AI. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
