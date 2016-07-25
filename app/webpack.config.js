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
			},
			{
				// use babel-loader for *.js files
				test: /\.js$/,
				loader: 'babel',
				// important: exclude files in node_modules
				// otherwise it's going to be really slow!
				exclude: /node_modules/
			}
		]
  },
  babel: {
    presets: ['es2015'],
    plugins: ['transform-runtime']
  }
}
