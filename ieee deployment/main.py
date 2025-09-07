#!/usr/bin/env python3
"""
Main entry point for Railway deployment
This file imports the Flask app from app.py to satisfy Railway's default expectations
"""
from app import app

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
