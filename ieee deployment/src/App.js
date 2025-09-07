import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Toaster, toast } from 'react-hot-toast';
import Header from './components/Header';
import TextAnalyzer from './components/TextAnalyzer';
import AnalysisResult from './components/AnalysisResult';
import Features from './components/Features';
import Credits from './components/Credits';
import Footer from './components/Footer';
import GalaxyBackground from './components/GalaxyBackground';
import './App.css';

function App() {
  const [analysisResult, setAnalysisResult] = useState(null);
  const [isAnalyzing, setIsAnalyzing] = useState(false);

  const API_BASE = process.env.REACT_APP_API_URL || '';
  const handleAnalysis = async (text) => {
    setIsAnalyzing(true);
    setAnalysisResult(null);

    try {
      const response = await fetch(`${API_BASE}/api/analyze`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text }),
      });

      const data = await response.json();

      if (data.success) {
        setAnalysisResult(data);
        toast.success('Analysis completed successfully!');
      } else {
        toast.error(data.error || 'Analysis failed');
      }
    } catch (error) {
      console.error('Analysis error:', error);
      toast.error('Failed to connect to the analysis service');
    } finally {
      setIsAnalyzing(false);
    }
  };

  return (
    <div className="App">
      <GalaxyBackground />
      
      <Toaster 
        position="top-right"
        toastOptions={{
          duration: 4000,
          style: {
            background: 'rgba(0, 0, 0, 0.8)',
            color: '#fff',
            fontFamily: 'Bricolage Grotesque, sans-serif',
            backdropFilter: 'blur(10px)',
            border: '1px solid rgba(255, 255, 255, 0.1)',
          },
        }}
      />
      
      <Header />
      
      <main className="main-content">
        <div className="container">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            className="hero-section"
          >
            <h1 className="hero-title">
              AI-Powered Content Moderation
            </h1>
            <p className="hero-subtitle">
              Analyze text content for toxicity, spam, and safety using advanced machine learning (70% weight) and rule-based detection (30% weight)
            </p>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.2 }}
            className="analyzer-section"
          >
            <TextAnalyzer 
              onAnalyze={handleAnalysis}
              isAnalyzing={isAnalyzing}
            />
          </motion.div>

          <AnimatePresence>
            {analysisResult && (
              <motion.div
                initial={{ opacity: 0, y: 30 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -30 }}
                transition={{ duration: 0.5 }}
                className="result-section"
              >
                <AnalysisResult result={analysisResult} />
              </motion.div>
            )}
          </AnimatePresence>

          <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.4 }}
            className="features-section"
          >
            <Features />
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.6 }}
            className="credits-section"
          >
            <Credits />
          </motion.div>
        </div>
      </main>

      <Footer />
    </div>
  );
}

export default App;
