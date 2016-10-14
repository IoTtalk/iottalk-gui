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
        test: /\.(png|jpg|gif|svg)$/,
        loader: 'file',
        query: {
          name: '[name].[ext]?[hash]'
        }
      },
		]
  },
  babel: {
    presets: ['es2015'],
    plugins: ['transform-runtime'],
  },
  plugins: [
    new webpack.ProvidePlugin({
      $: "jquery",
      jQuery: "jquery",
      "window.jQuery": "jquery",
      semantic: "./static/semantic/semantic.min.js",
    }),
  ]
}
