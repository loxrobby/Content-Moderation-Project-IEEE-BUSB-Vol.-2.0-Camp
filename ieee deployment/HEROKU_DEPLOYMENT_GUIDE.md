# Heroku Deployment Guide for Content Moderation AI

## 🚀 Deploy to Heroku (Free Tier Available!)

Heroku offers a free tier without requiring a credit card, making it perfect for your Content Moderation AI project.

### Prerequisites
- GitHub repository with your code
- Heroku account (free)
- Heroku CLI (optional but recommended)

### Step 1: Create Heroku Account
1. Go to [heroku.com](https://heroku.com)
2. Sign up for a free account (no credit card required!)
3. Verify your email address

### Step 2: Install Heroku CLI (Optional)
Download from [devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli)

### Step 3: Deploy via GitHub (Recommended)

#### Method A: GitHub Integration (Easiest)
1. **Login to Heroku Dashboard**
2. **Click "New" → "Create new app"**
3. **App Name**: `your-content-moderation-ai` (must be unique)
4. **Region**: United States
5. **Click "Create app"**

6. **Connect to GitHub**:
   - Go to "Deploy" tab
   - Click "Connect to GitHub"
   - Authorize Heroku to access your GitHub
   - Search for your repository: `content-moderation-ai`
   - Click "Connect"

7. **Configure Deployment**:
   - **Branch**: `main`
   - **Root Directory**: `ieee deployment` (IMPORTANT!)
   - Click "Enable Automatic Deploys"

8. **Manual Deploy**:
   - Click "Deploy Branch"
   - Wait for build to complete (2-5 minutes)

#### Method B: Heroku CLI
```bash
# Login to Heroku
heroku login

# Create app
heroku create your-content-moderation-ai

# Set buildpack
heroku buildpacks:set heroku/python

# Deploy
git subtree push --prefix="ieee deployment" heroku main
```

### Step 4: Configure Environment Variables
In Heroku Dashboard → Settings → Config Vars:
- `FLASK_ENV` = `production`
- `PYTHON_VERSION` = `3.9.18`

### Step 5: Test Your Deployment
1. **Get your app URL**: `https://your-content-moderation-ai.herokuapp.com`
2. **Test health endpoint**: `https://your-content-moderation-ai.herokuapp.com/api/health`
3. **Test main app**: `https://your-content-moderation-ai.herokuapp.com`

## 🔧 Important Configuration Notes

### Root Directory Setting
**CRITICAL**: Set the root directory to `ieee deployment` in Heroku settings, otherwise it won't find your app.py file.

### File Structure
```
ieee deployment/          # ← This is your root directory
├── app.py               # Main Flask application
├── requirements.txt     # Python dependencies
├── Procfile            # Start command
├── runtime.txt         # Python version
├── ensemble_*.pkl      # ML model files
└── templates/
    └── index.html      # Frontend template
```

## 📊 Expected Results

Your Content Moderation AI will be available at:
- **Main App**: `https://your-app-name.herokuapp.com`
- **API Health**: `https://your-app-name.herokuapp.com/api/health`
- **Text Analysis**: `https://your-app-name.herokuapp.com/api/analyze`

## 🆓 Heroku Free Tier Limits

### What You Get:
- ✅ **512MB RAM** - Sufficient for your ML models
- ✅ **No credit card required**
- ✅ **Custom domains** (with paid plans)
- ✅ **Automatic deployments** from GitHub
- ✅ **SSL certificates** included

### Limitations:
- ⚠️ **App sleeps after 30 minutes** of inactivity
- ⚠️ **550-1000 free dyno hours** per month
- ⚠️ **No persistent file storage** (use external storage for uploads)

## 🛠️ Troubleshooting

### Common Issues:

1. **"No app.py found"**:
   - Ensure root directory is set to `ieee deployment`
   - Check that app.py is in the deployment folder

2. **"Module not found"**:
   - Verify requirements.txt has all dependencies
   - Check build logs for missing packages

3. **"App crashes on startup"**:
   - Check logs: `heroku logs --tail`
   - Verify all .pkl model files are present
   - Ensure Procfile syntax is correct

4. **"Memory issues"**:
   - Heroku free tier has 512MB RAM limit
   - Your ML models should fit within this limit

### Viewing Logs:
```bash
# Via CLI
heroku logs --tail --app your-app-name

# Via Dashboard
Go to your app → More → View logs
```

## 🎯 Deployment Checklist

- [ ] Heroku account created
- [ ] GitHub repository connected
- [ ] Root directory set to `ieee deployment`
- [ ] Automatic deploys enabled
- [ ] Environment variables set
- [ ] App deployed successfully
- [ ] Health endpoint responding
- [ ] Main application accessible

## 🚀 Post-Deployment

1. **Test all endpoints**:
   - `/` - Main page
   - `/api/health` - Health check
   - `/api/analyze` - Text analysis

2. **Update frontend URLs** (if you have a separate frontend):
   - Point API calls to your Heroku URL
   - Update CORS settings if needed

3. **Monitor performance**:
   - Check Heroku metrics
   - Monitor memory usage
   - Watch for any errors in logs

## 💡 Pro Tips

- **Keep your app awake**: Use a service like UptimeRobot to ping your app every 20 minutes
- **Monitor logs**: Check logs regularly for any issues
- **Optimize models**: Consider model compression if you hit memory limits
- **Use environment variables**: Store sensitive data in Heroku config vars

Your Content Moderation AI should work perfectly on Heroku! 🎉

## 📞 Support

If you encounter issues:
1. Check Heroku build logs
2. Verify all files are in the correct directory
3. Ensure requirements.txt is complete
4. Check that all .pkl model files are present

Happy deploying! 🚀
