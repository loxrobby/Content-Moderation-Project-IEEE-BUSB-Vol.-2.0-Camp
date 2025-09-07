#!/usr/bin/env python3
"""
Quick deployment helper script for Content Moderation Project
"""

import os
import subprocess
import sys

def check_git_status():
    """Check if git is initialized and files are committed"""
    try:
        # Check if git is initialized
        result = subprocess.run(['git', 'status'], capture_output=True, text=True)
        if result.returncode != 0:
            print("❌ Git not initialized. Please run: git init")
            return False
        
        # Check for uncommitted changes
        if "nothing to commit" not in result.stdout:
            print("⚠️  You have uncommitted changes. Please commit them first:")
            print("   git add .")
            print("   git commit -m 'Ready for deployment'")
            return False
        
        print("✅ Git repository is ready")
        return True
    except FileNotFoundError:
        print("❌ Git not found. Please install Git first.")
        return False

def check_required_files():
    """Check if all required files exist"""
    required_files = [
        'app.py',
        'requirements.txt',
        'railway.json',
        'Procfile',
        'runtime.txt',
        'ensemble_model.pkl',
        'ensemble_vectorizer.pkl',
        'ensemble_label_encoder.pkl',
        'ensemble_numerical_features.pkl',
        'ensemble_toxicity_threshold.pkl'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print("❌ Missing required files:")
        for file in missing_files:
            print(f"   - {file}")
        return False
    
    print("✅ All required files present")
    return True

def show_deployment_options():
    """Show deployment options"""
    print("\n🚀 DEPLOYMENT OPTIONS:")
    print("=" * 50)
    
    print("\n1. 🥇 RAILWAY (RECOMMENDED)")
    print("   - Go to: https://railway.app")
    print("   - Sign up with GitHub")
    print("   - Click 'New Project' → 'Deploy from GitHub repo'")
    print("   - Select your repository")
    print("   - Wait for deployment (5-10 minutes)")
    print("   - Get your URL: https://your-project.railway.app")
    
    print("\n2. 🥈 RENDER")
    print("   - Go to: https://render.com")
    print("   - Connect GitHub account")
    print("   - Create 'New Web Service'")
    print("   - Select your repository")
    print("   - Build Command: pip install -r requirements.txt")
    print("   - Start Command: gunicorn app:app")
    
    print("\n3. 🥉 HEROKU")
    print("   - Install Heroku CLI")
    print("   - Run: heroku create your-app-name")
    print("   - Run: git push heroku main")
    
    print("\n4. 🆓 PYTHONANYWHERE")
    print("   - Go to: https://pythonanywhere.com")
    print("   - Upload files via web interface")
    print("   - Configure web app in dashboard")

def main():
    """Main deployment helper"""
    print("🚀 Content Moderation Project - Deployment Helper")
    print("=" * 50)
    
    # Check prerequisites
    print("\n📋 Checking prerequisites...")
    
    if not check_required_files():
        print("\n❌ Please ensure all required files are present before deploying.")
        return
    
    if not check_git_status():
        print("\n❌ Please commit your changes before deploying.")
        return
    
    print("\n✅ All prerequisites met!")
    
    # Show deployment options
    show_deployment_options()
    
    print("\n🎯 QUICK START (Railway):")
    print("1. Push to GitHub: git push origin main")
    print("2. Go to: https://railway.app")
    print("3. Deploy from GitHub repo")
    print("4. Share your URL!")
    
    print("\n📚 For detailed instructions, see: DEPLOYMENT_GUIDE.md")
    print("\n🎉 Happy Deploying!")

if __name__ == "__main__":
    main()
