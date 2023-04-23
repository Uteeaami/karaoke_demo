const { createProxyMiddleware } = require('http-proxy-middleware');

//SetupProxy to define what paths are used
module.exports = function(app) {
  app.use(
    '/video',
    createProxyMiddleware({
      target: 'https://karaoke-app-ke.herokuapp.com/',
      changeOrigin: true,
    })
  );
  app.use(
    '/script',
    createProxyMiddleware({
      target: 'https://karaoke-app-ke.herokuapp.com/',
      changeOrigin: true,
    })
  );
};
