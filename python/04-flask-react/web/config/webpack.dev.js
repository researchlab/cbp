const webpack = require('webpack')
const path = require('path')

const devConfig = {
    devtool: 'eval-cheap-module-source-map',
    mode: 'development',
    devServer: {
			// contentBase: path.resolve(__dirname, '../public'),  不支持
        historyApiFallback: true, 
			// publicPath: '/',  也不支持了
        port: 9901,
			// progress: true, // 进度条  webpack-dev-server 4.11 也不支持l
			//hotOnly: true, //页面构建失败不刷新页面 webpack-dev-server 4.11 已经不支持这个参数了
        hot: true, // 热加载
        open: true, // 自动打开浏览器
    },
    plugins: [new webpack.HotModuleReplacementPlugin()]
}

module.exports = devConfig 
