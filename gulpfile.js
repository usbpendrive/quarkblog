var gulp = require('gulp');
var sass = require('gulp-sass');

gulp.task('sass', function () {
    return gulp.src('base/static/base/css/style.scss')
        .pipe(sass())
        .pipe(gulp.dest('base/static/base/css'))
});

gulp.task('default', function () {
    gulp.watch('base/static/base/css/*.scss', ['sass']);
});