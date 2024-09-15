const { createProxyMiddleware } = require('http-proxy-middleware')

module.exports = function (app) {
    app.use(
        '/api',
        createProxyMiddleware({
            target: 'http://localhost:8000',
            changeOrigin: true,

            // 删掉开头的 /api 再传给后端
            pathRewrite: { '^/api': '' }
        })


    )
}
