const webpack = require('webpack')

module.exports = {
	entry: {
    app: './static/app.js',
  },
	output: {
		path: __dirname,
		filename: './static/build.js',
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
			}
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
      })
  ]
}
