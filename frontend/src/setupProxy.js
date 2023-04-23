const { createProxyMiddleware } = require('http-proxy-middleware');

//SetupProxy to define what paths are used
module.exports = function(app) {
  app.use(
    '/video',
    createProxyMiddleware({
      target: 'https://arcane-wave-87002.herokuapp.com/',
      changeOrigin: true,
    })
  );
  app.use(
    '/script',
    createProxyMiddleware({
      target: 'https://arcane-wave-87002.herokuapp.com/',
      changeOrigin: true,
    })
  );
};
