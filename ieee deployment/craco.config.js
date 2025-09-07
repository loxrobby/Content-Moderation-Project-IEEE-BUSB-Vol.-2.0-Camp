const path = require('path');

module.exports = {
  devServer: {
    port: 3000
  },
  webpack: {
    configure: (webpackConfig) => {
      // Find the source-map-loader rule and modify it
      const sourceMapLoaderRule = webpackConfig.module.rules.find(
        rule => rule.use && rule.use.some && rule.use.some(use => 
          use.loader && use.loader.includes('source-map-loader')
        )
      );

      if (sourceMapLoaderRule) {
        // Add ignore patterns for problematic modules
        sourceMapLoaderRule.exclude = [
          ...(sourceMapLoaderRule.exclude || []),
          /node_modules\/@mediapipe\/tasks-vision/,
          /vision_bundle_mjs\.js\.map$/,
          /vision_bundle\.mjs$/
        ];
      }

      // Also suppress warnings for specific modules
      webpackConfig.ignoreWarnings = [
        ...(webpackConfig.ignoreWarnings || []),
        /Failed to parse source map/,
        /@mediapipe\/tasks-vision/
      ];

      return webpackConfig;
    }
  }
};
