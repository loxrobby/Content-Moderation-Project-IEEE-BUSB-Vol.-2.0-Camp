# Render Deployment Guide for Content Moderation AI

## 🚀 Deploy to Render (Recommended)

Render is more reliable than Railway for Python applications and has better support for ML models.

### Prerequisites
- GitHub repository with your code
- Render account (free tier available)

### Step 1: Create Render Account
1. Go to [render.com](https://render.com)
2. Sign up with your GitHub account
3. Connect your GitHub repository

### Step 2: Create New Web Service
1. Click "New +" → "Web Service"
2. Connect your GitHub repository
3. Select the `ieee deployment` folder as the root directory

### Step 3: Configure Service Settings
- **Name**: `content-moderation-ai`
- **Environment**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT`
- **Health Check Path**: `/api/health`

### Step 4: Environment Variables
Add these environment variables in Render dashboard:
- `FLASK_ENV` = `production`
- `PYTHON_VERSION` = `3.9.16`

### Step 5: Deploy
1. Click "Create Web Service"
2. Render will automatically build and deploy your application
3. Wait for deployment to complete (usually 2-5 minutes)

### Step 6: Test Your Deployment
1. Once deployed, you'll get a URL like `https://your-app-name.onrender.com`
2. Test the health endpoint: `https://your-app-name.onrender.com/api/health`
3. Test the main application: `https://your-app-name.onrender.com`

## 🔧 Alternative: Manual Configuration

If you prefer manual setup:

1. **Repository**: Select your GitHub repo
2. **Root Directory**: `ieee deployment`
3. **Runtime**: Python 3
4. **Build Command**: `pip install -r requirements.txt`
5. **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT`

## 📊 Expected Results

Your Content Moderation AI will be available at:
- **Main App**: `https://your-app-name.onrender.com`
- **API Health**: `https://your-app-name.onrender.com/api/health`
- **Text Analysis**: `https://your-app-name.onrender.com/api/analyze`

## 🆚 Why Render vs Railway?

### Render Advantages:
- ✅ Better Python support
- ✅ More reliable ML model loading
- ✅ Simpler configuration
- ✅ Better error messages
- ✅ Free tier with good limits

### Railway Issues:
- ❌ Complex configuration conflicts
- ❌ Module import issues
- ❌ Mixed Python/Node.js detection problems

## 🛠️ Troubleshooting

### If deployment fails:
1. Check build logs in Render dashboard
2. Ensure all model files are in the deployment directory
3. Verify requirements.txt has all dependencies
4. Check that app.py is in the root of deployment directory

### Common Issues:
- **Import errors**: Check requirements.txt completeness
- **Model loading errors**: Verify .pkl files are present
- **Memory issues**: Render free tier has 512MB RAM limit

## 📁 File Structure for Render
```
ieee deployment/
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── Procfile                 # Start command
├── render.yaml              # Render configuration
├── ensemble_model.pkl       # ML model files
├── ensemble_vectorizer.pkl
├── ensemble_label_encoder.pkl
├── ensemble_numerical_features.pkl
├── ensemble_toxicity_threshold.pkl
└── templates/
    └── index.html           # Frontend template
```

## 🎯 Next Steps
1. Deploy to Render using this guide
2. Test all endpoints
3. Update your frontend to use the new Render URL
4. Monitor performance and scale as needed

Your Content Moderation AI should work perfectly on Render! 🚀
