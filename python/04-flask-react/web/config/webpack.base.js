const path = require('path');
const htmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const {CleanWebpackPlugin} = require('clean-webpack-plugin')
const FaviconsWebpackPlugin = require('favicons-webpack-plugin')
const HappyPack = require('happypack');
const { merge } = require('webpack-merge');
const devConfig = require('./webpack.dev');
const proConfig = require('./webpack.pro');

const Appconfig = {
    target: 'web',
    entry:{
        main: './src/index.jsx'
    },
    output:{
      path: path.resolve(__dirname, '../public'),
			filename: 'static/js/[name].js',  // 将js 单独生成到 public/static/js文件夹下
    },
    resolve:{
			extensions:['.jsx','.tsx','.ts','.js'],
			alias:{
				crypto:false
			},
			fallback:{
				url:false
			}
    },
    module: {
        rules:[
            {
                test: /\.css$/,
                use: [
                    'css-hot-loader',
                    MiniCssExtractPlugin.loader,
                    {
                        loader: 'css-loader'
                    },
                    {
                        loader: 'postcss-loader',
                        options: {
                            postcssOptions:{
                                plugins:[
                                    ['autoprefixer'],
                                ]
                            }
                        }
                    }
                ]
            },
            {
                test: /\.(png|jpe?g|gif|svg|ttf|eot|woff|woff2)$/,
                use: {
                  loader: 'url-loader',
                  options: {
                    esModule: false,
                    name: '[name]_[hash].[ext]',
										outputPath: 'static/images', // 将图片单独生成到 public/static下面
                    limit: 2048
                  }
                }
            },
					  {
								test: /\.(ico)$/,
							  use:{
									loader:'url-loader',
									options:{
										//limit:50,
										name: '[name].[ext]',
										outputPath: 'static'
									}
								}
						},
					  {
							  test: /\.html$/,
							  use:{
									loader: 'html-loader',
							    options:{
								  	// html-loader 0.5.5 版本可以写如下方式
								  	// attrs: ['img:src', 'link:href']
								  	// html-loader 1.3.2 版本需要写为对象形式
										// attributes:{
										// html-loader 3.0.0 没有attributes属性改为sources了
										sources:{
								  		list:[
								  			{ tag: 'link', attribute: 'href', type: 'src'},
								  			{ tag:'img', attribute: 'src', type: 'src'},
								  		]
								  	}
								  }
								}	
					  },
            {
                test: /\.scss$/,
                use: [
                    'css-hot-loader',
                    MiniCssExtractPlugin.loader,
                    'css-loader',
                    {
                        loader: 'postcss-loader',
                        options:{
                            postcssOptions:{
                                plugins:[
                                    ['autoprefixer'],
                                ]
                            }
                        }
                    },
                    'sass-loader'
                ]
            },
            {
                test: /\.less$/,
                use: [
                    'css-hot-loader',
                    MiniCssExtractPlugin.loader,
                    'css-loader',
                    {
                        loader: 'postcss-loader',
                        options:{
                            postcssOptions:{
                                plugins:[
                                    ['autoprefixer'],
                                ]
                            }
                        }
                    },
                    'less-loader'
                ]
            },
            {
                test: /\.tsx?$/,
                use: {
                    loader: 'ts-loader'
                }
            },
            {
                test: /\.jsx?$/,
                exclude: /node_modules/,
                include: path.resolve(__dirname, '../src'),
                use: ['happypack/loader?id=babel']
            }
        ]
    },
    optimization:{
        splitChunks:{
            chunks: 'all'
        }
    },
    plugins:[
			 new CleanWebpackPlugin(),
       new htmlWebpackPlugin({
           filename: 'index.html', // 输出文件【注意：这里的根路径是module.exports.output.path】
           template: 'src/index.html', // 源模板文件
           // inejct: 向template或者templateContent中注入所有静态资源，不同的配置值注入的位置不经相同。
           // 1.true或者body：所有JavaScript资源插入到body元素的底部 true 好像还是插入到头部
           // 2.head: 所有JavaScript资源插入到head元素中
           // 3.false： 所有静态资源css和JavaScript都不会注入到模板文件中
           inject:'body',
				   //favicon: path.resolve(__dirname,'../src/assets/images/favicon.ico') //动态添加favicon
       }),
			 new FaviconsWebpackPlugin({
				 logo:'../web/src/assets/images/favicon.png', // 只能处理png
				 publicPath:'static/favicon',
				 outputPath:'static/favicon',
				 prefix:''
			 }),
       new MiniCssExtractPlugin({
				 filename: 'static/css/[name].css' // 将css文件单独抽离到public/static文件夹中
       }),
       new HappyPack({
           id: 'babel',
           loaders:['babel-loader?cacheDirectory']
       })
    ]
}

module.exports = env => {
	  console.log('Production:', env.production)
    if (env && env.production){
        return merge(Appconfig, proConfig)
    } else {
        return merge(Appconfig, devConfig)
    }
}
