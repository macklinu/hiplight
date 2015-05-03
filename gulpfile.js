var gulp = require("gulp");
var mocha = require("gulp-mocha");
var jscs = require("gulp-jscs");
var nodemon = require("gulp-nodemon");
var gutil = require("gulp-util");

gulp.task("default", function() {
  nodemon({
    script: "src/app.js"
  });
});

gulp.task("test", ["jscs"], function(cb) {
  return gulp.src("test/*.js", {read: false})
    .pipe(mocha());
});

gulp.task("jscs", function() {
  return gulp.src("src/**.js")
    .pipe(jscs({
      configPath: ".jscsrc",
      fix: true
    }))
    .pipe(gulp.dest("src"));
});
