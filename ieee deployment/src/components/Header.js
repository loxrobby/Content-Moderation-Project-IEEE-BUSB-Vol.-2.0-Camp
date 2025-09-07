import React from 'react';
import { Shield, Brain, Zap } from 'lucide-react';
import './Header.css';

const Header = () => {
  return (
    <header className="header">
      <div className="container">
        <div className="header-content">
          <div className="logo">
            <Shield className="logo-icon" />
            <span className="logo-text">ContentMod AI</span>
          </div>
          
          <nav className="nav">
            <div className="nav-spacer"></div>
            <div className="nav-item">
              <Brain className="nav-icon" />
              <span>AI Analysis</span>
            </div>
            <div className="nav-item">
              <Zap className="nav-icon" />
              <span>Real-time</span>
            </div>
          </nav>
        </div>
      </div>
    </header>
  );
};

export default Header;
