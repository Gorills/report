"use strict";

import gulp from "gulp";

const requireDir = require("require-dir"),
    paths = {
        views: {
            src: [
                "./#src/templates/**/*.html",
                "./#src/templates/pages/*.html"
            ],
            dist: "./main/templates/",
            watch: [
                "./#src/templates/**/*.html",
                "./#src/templates/pages/*.html"
            ]
        },
        styles: {
            src: "./#src/scss/style.{scss,sass}",
            dist: "./static/css/",
            watch: [
                "./#src/scss/**/*.{scss,sass}",
                "./#src/scss/**/*.{scss,sass}"
            ]
        },
        scripts: {
            src: "./#src/js/app.js",
            dist: "./static/js/",
            watch: [
                "./#src/js/**/*.js",
                "./#src/js/**/*.js"
            ]
        },
        images: {
            src: [
                "./#src/images/**/*.{jpg,jpeg,png,gif,tiff,svg}",
                "!./#src/images/fav/*.{jpg,jpeg,png,gif,tiff}"
            ],
            dist: "./static/images/",
            watch: "./#src/images/**/*.{jpg,jpeg,png,gif,svg,tiff}"
        },
        sprites: {
            src: "./#src/images/sprites/*.svg",
            dist: "./static/images/sprites/",
            watch: "./#src/images/sprites/*.svg"
        },
        fonts: {
            src: "./#src/fonts/**/*.{woff,woff2,ttf}",
            dist: "./static/fonts/",
            watch: "./#src/fonts/**/*.{woff,woff2,ttf}"
        },
        favicons: {
            src: "./#src/img/fav/*.{jpg,jpeg,png,gif}",
            dist: "./static/img/fav/",
        },
        gzip: {
            src: "./#src/.htaccess",
            dist: "./static/"
        }
       
    };

requireDir("./gulp-tasks/");

export { paths };

export const development = gulp.series("clean",
    gulp.parallel([
        "views", 
        "styles", 
        "scripts", 
        "images", 
        "webp", 
        "sprites", 
        "fonts", 
        "favicons"
      
    ]),
    gulp.parallel("serve"));

export const prod = gulp.series("clean",
    gulp.parallel([
        "views", 
        "styles", 
        "scripts", 
        "images", 
        "webp", 
        "sprites", 
        "fonts", 
        "favicons", 
        "gzip",
      
    ]));

export default development;