# 🚀 Content Moderation Project - Free Deployment Guide

This guide provides multiple free options to deploy your Content Moderation AI project with a shareable URL.

## 🥇 Option 1: Railway (RECOMMENDED)

**Why Railway?**
- ✅ Perfect for full-stack Flask + React apps
- ✅ Generous free tier (500 hours/month)
- ✅ Automatic deployments from GitHub
- ✅ Built-in database support
- ✅ Custom domains
- ✅ Easy environment variable management

### Step-by-Step Railway Deployment:

#### 1. Prepare Your Repository
```bash
# Make sure all files are committed to Git
git add .
git commit -m "Prepare for Railway deployment"
git push origin main
```

#### 2. Deploy to Railway
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Railway will automatically detect it's a Python app
6. Wait for deployment (5-10 minutes)

#### 3. Configure Environment Variables
In Railway dashboard:
- Go to your project → Variables
- Add: `FLASK_ENV=production`
- Add: `PORT=5000` (Railway sets this automatically)

#### 4. Get Your URL
- Railway provides a URL like: `https://your-project-name.railway.app`
- This is your shareable URL!

---

## 🥈 Option 2: Render

**Why Render?**
- ✅ Free tier with 750 hours/month
- ✅ Automatic SSL certificates
- ✅ Easy GitHub integration
- ✅ Good for Python apps

### Render Deployment Steps:

#### 1. Create render.yaml
```yaml
services:
  - type: web
    name: content-moderation-api
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
    envVars:
      - key: FLASK_ENV
        value: production
```

#### 2. Deploy
1. Go to [render.com](https://render.com)
2. Connect GitHub account
3. Create "New Web Service"
4. Select your repository
5. Use these settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Environment**: `Python 3`

---

## 🥉 Option 3: Heroku

**Why Heroku?**
- ✅ Classic platform, very reliable
- ✅ Free tier available (with limitations)
- ✅ Excellent documentation

### Heroku Deployment Steps:

#### 1. Install Heroku CLI
```bash
# Download from https://devcenter.heroku.com/articles/heroku-cli
```

#### 2. Deploy
```bash
# Login to Heroku
heroku login

# Create app
heroku create your-content-moderation-app

# Set environment variables
heroku config:set FLASK_ENV=production

# Deploy
git push heroku main
```

---

## 🆓 Option 4: PythonAnywhere

**Why PythonAnywhere?**
- ✅ Free tier available
- ✅ Great for Python apps
- ✅ Easy file management

### PythonAnywhere Steps:

1. Go to [pythonanywhere.com](https://pythonanywhere.com)
2. Create free account
3. Upload your files via web interface
4. Configure web app in dashboard
5. Set up virtual environment and install requirements

---

## 🆓 Option 5: Vercel (Frontend Only)

**For React Frontend Only:**

1. Go to [vercel.com](https://vercel.com)
2. Import your GitHub repository
3. Vercel auto-detects React app
4. Deploy with one click

**Note**: You'll need to deploy the Flask backend separately and update the API URL.

---

## 🔧 Pre-Deployment Checklist

### ✅ Files to Include:
- [x] `app.py` (Flask backend)
- [x] `requirements.txt`
- [x] `railway.json` (for Railway)
- [x] `Procfile` (for Heroku)
- [x] `runtime.txt` (Python version)
- [x] All `.pkl` model files
- [x] `templates/` folder
- [x] `static/` folder (if any)

### ✅ Files to Exclude (.gitignore):
```
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.venv/
pip-log.txt
pip-delete-this-directory.txt
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.log
.git
.mypy_cache
.pytest_cache
.hypothesis
.DS_Store
```

---

## 🚀 Quick Start (Railway - Recommended)

1. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. **Deploy on Railway**:
   - Visit [railway.app](https://railway.app)
   - Sign up with GitHub
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository
   - Wait for deployment

3. **Get Your URL**:
   - Railway provides: `https://your-project-name.railway.app`
   - Share this URL with anyone!

---

## 🔍 Troubleshooting

### Common Issues:

1. **Model files not found**:
   - Ensure all `.pkl` files are in the repository
   - Check file paths in `app.py`

2. **Port issues**:
   - Use `os.environ.get('PORT', 5000)` for dynamic ports
   - Railway/Heroku set PORT automatically

3. **Memory issues**:
   - Model files are large (~3MB total)
   - Railway free tier should handle this fine

4. **Build failures**:
   - Check `requirements.txt` for all dependencies
   - Ensure Python version compatibility

---

## 📊 Performance Tips

1. **Optimize Model Loading**:
   - Models load once at startup
   - Consider caching for better performance

2. **Environment Variables**:
   - Set `FLASK_ENV=production` for production
   - Disable debug mode in production

3. **Monitoring**:
   - Use platform monitoring tools
   - Set up health checks

---

## 🎯 Expected Results

After deployment, you'll have:
- ✅ A live, shareable URL
- ✅ Working content moderation API
- ✅ 100% accuracy on test cases
- ✅ Professional-grade deployment

**Example URL**: `https://content-moderation-ai.railway.app`

---

## 📞 Support

If you encounter issues:
1. Check platform logs
2. Verify all files are committed
3. Test locally first
4. Check environment variables

**Happy Deploying! 🚀**