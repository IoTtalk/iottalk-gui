const path = require('path')
const webpack = require('webpack')

module.exports = {
	entry: {
    app: './static/app.js',
  },
	output: {
		path: path.resolve(__dirname, './static'),
		filename: 'build.js',
	},
  resolveLoader: {
    root: path.join(__dirname, 'node_modules'),
  },
  resolve: {
    extensions: ['', '.js', '.vue'],
    fallback: [path.join(__dirname, 'node_modules')],
    alias: {
      animate: path.resolve(__dirname, 'node_modules/animate.css/animate.min.css'),
      semantic: path.resolve(__dirname, 'static/semantic/semantic.min.css')
    }
  },
	module: {
		loaders: [
			{
				test: /\.vue$/,
				loader: 'vue',
			},
			{
				test: /\.js$/,
				loader: 'babel',
				exclude: /node_modules/,
			},
      {
        test: /\.css$/,
        loader: "style-loader!css-loader"
      },
      {
        test: /\.(png|jpg|gif|woff|woff2|eot|ttf|svg)$/,
        loader: 'url-loader',
      },
		]
  },
  babel: {
    presets: ['es2015'],
    plugins: ['transform-runtime'],
  },
}
