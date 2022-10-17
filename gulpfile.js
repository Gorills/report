//let replace = require('gulp-replace'); //.pipe(replace('bar', 'foo'))
let { src, dest } = require("gulp");
let fs = require('fs');
let gulp = require("gulp");
let browsersync = require("browser-sync").create();
let autoprefixer = require("gulp-autoprefixer");
let scss = require("gulp-sass")(require('sass'));;
let group_media = require("gulp-group-css-media-queries");
let plumber = require("gulp-plumber");
let del = require("del");
let imagemin = require("gulp-imagemin");
let uglify = require("gulp-uglify-es").default;
let rename = require("gulp-rename");
let fileinclude = require("gulp-file-include");
let clean_css = require("gulp-clean-css");
let newer = require('gulp-newer');

let webp = require('imagemin-webp');
let webpcss = require("gulp-webpcss");
let webphtml = require('gulp-webp-html');

let fonter = require('gulp-fonter');

let ttf2woff = require('gulp-ttf2woff');
let ttf2woff2 = require('gulp-ttf2woff2');

let project_name = require("path").basename(__dirname);
let src_folder = "#src";

let path = {
	build: {
		html: "./main/templates/",
		js: "./static/js/",
		css: "./static/css/",
		images: "./static/images/",
		
	},
	src: {
		favicon: src_folder + "/images/favicon.{jpg,jpeg,png,svg,gif,ico,webp}",
		html: [src_folder + "/templates/**/*.html", src_folder + "/templates/**/*.txt", "!" + src_folder + "/**/_*.html"],
		js: [src_folder + "/js/app.js", src_folder + "/js/jquery.js"],
		css: [src_folder + "/scss/style.scss", "!" + src_folder + "/**/_*.scss"],
		images: [src_folder + "/images/**/*.{jpg,png,svg,gif,ico,webp}", "!**/favicon.*"],
		
	},
	watch: {
		html: src_folder + "/templates/**/*.html",
		js: src_folder + "/js/**/*.js",
		css: src_folder + "/scss/**/*.scss",
		images: src_folder + "/images/**/*.{jpg,png,svg,gif,ico,webp}"
	},
	cleancss: "./static/css",
	cleanjs: "./static/js",
	cleanimages: "./static/images",
	clear: "./templates/"
};

function runServer() {
    var proc = exec('python manage.py runserver')
}

function browserSync(done) {
	browsersync.init({
		notify: false,
        port: 3000,
        proxy: 'localhost:8000'
	});
}
function html() {
	return src(path.src.html, {})
		
		.pipe(fileinclude())
		// .pipe(webphtml())
		.pipe(dest(path.build.html))
		.pipe(browsersync.stream());
}
function css() {
	return src(path.src.css, {})
		
		.pipe(
			scss({
				outputStyle: "expanded"
			})
		)
		.pipe(group_media())
		.pipe(
			autoprefixer({
				grid: true,
				overrideBrowserslist: ["last 5 versions"],
				cascade: true
			})
		)
		.pipe(webpcss(
			{
				webpClass: "._webp",
				noWebpClass: "._no-webp"
			}
		))
		.pipe(dest(path.build.css))
		.pipe(clean_css())
		// .pipe(
		// 	rename({
		// 		extname: ".min.css"
		// 	})
		// )
		.pipe(dest(path.build.css))
		.pipe(browsersync.stream());
}
function js() {
	return src(path.src.js, {})
		
		.pipe(fileinclude())
		.pipe(gulp.dest(path.build.js))
		.pipe(uglify(/* options */))
		.pipe(
			rename({
				suffix: ".min",
				extname: ".js"
			})
		)
		.pipe(dest(path.build.js))
		.pipe(browsersync.stream());
}
function images() {
	return src(path.src.images)
		.pipe(newer(path.build.images))
		.pipe(
			imagemin([
				webp({
					quality: 75
				})
			])
		)
		.pipe(
			rename({
				extname: ".webp"
			})
		)
		.pipe(dest(path.build.images))
		.pipe(src(path.src.images))
		.pipe(newer(path.build.images))
		.pipe(
			imagemin({
				progressive: true,
				svgoPlugins: [{ removeViewBox: false }],
				interlaced: true,
				optimizationLevel: 3 // 0 to 7
			})
		)
		.pipe(dest(path.build.images))
}
function favicon() {
	return src(path.src.favicon)
		
		.pipe(
			rename({
				extname: ".ico"
			})
		)
		.pipe(dest(path.build.html))
}

function cb() { }


function cleancss() {
	return del(path.cleancss);
}
function cleanjs() {
	return del(path.cleanjs);
}
function cleanimages() {
	return del(path.cleanimages);
}
function clear() {
	return del(path.clear);
}

function watchFiles() {
	gulp.watch([path.watch.html], html);
	gulp.watch([path.watch.css], css);
	gulp.watch([path.watch.js], js);
	gulp.watch([path.watch.images], images);
}
let build = gulp.series(cleancss, cleanjs, cleanimages, clear, gulp.parallel(html, css, js, favicon, images));
let watch = gulp.parallel(build, watchFiles, browserSync);

exports.html = html;
exports.css = css;
exports.js = js;
exports.favicon = favicon;

exports.images = images;
exports.clear = clear;
exports.cleancss = cleancss;
exports.cleanjs = cleanjs;
exports.cleanimages = cleanimages;
exports.build = build;
exports.watch = watch;
exports.default = watch;