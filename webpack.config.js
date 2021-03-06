const path = require('path');

module.exports = {
	entry: './web/assets/scripts/app.js',
	output: {
		filename: 'bundle.js',
		path: path.resolve(__dirname, 'static')
	},
	devtool: 'source-map',
	resolve: {
		alias: {
			jquery: "jquery/src/jquery"
		}
	},
	performance: {
		// Turn off size warnings for entry points
		hints: false,
	},
	module: {
		rules: [
			{
				test: /\.(scss)$/,
				use: [
					{
						loader: 'style-loader',
					},
					{
						loader: 'css-loader',
					},
					{
						loader: 'postcss-loader',
						options: {
							plugins: function () {
								return [
									require('precss'),
									require('autoprefixer')
								];
							}
						}
					}, {
						loader: 'sass-loader'
					}]
			},
			{
				test: /\.css$/,
				use: ['style-loader', 'css-loader']
			}
		]
	}
};
