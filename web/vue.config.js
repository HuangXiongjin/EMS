const webpack = require('webpack')
module.exports ={
    devServer:{
        proxy:{
            '/api': {  //使用"/api"来代替"http://xxx"
                target: 'http://127.0.0.1:5000', //源地址
                changeOrigin: true, //请求头
                pathRewrite: {
                  '^/api': '/' //路径重写
                  }
              },
              '/socket': {
                target: 'ws://127.0.0.1:5002',
                changeOrigin: true,
                pathRewrite: {
                  '^/socket': '/'
                  }
              }
        }
    },
    chainWebpack: config => {
        config.plugin('provide').use(webpack.ProvidePlugin, [{
          $: 'jquery',
          jquery: 'jquery',
          jQuery: 'jquery',
          'window.jQuery': 'jquery'
        }])
    }
}
