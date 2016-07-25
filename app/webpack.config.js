module.exports = {
	entry: './static/js/app.js',
	output: {
		path: __dirname,
		filename: './static/js/build.js'
	},
	module: {
		loaders: [
			{
				test: /\.vue$/,
				loader: 'vue'
			}
		]
	}
}
