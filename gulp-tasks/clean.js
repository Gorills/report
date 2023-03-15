"use strict";

import gulp from "gulp";
import del from "del";

gulp.task("clean", () => {
    return del(
        ["./static/css/*"],
        ["./static/fonts/*"],
        ["./static/images/*"],
        ["./static/js/*"],
        ["./main/teplates/*"],
        
        );
});

