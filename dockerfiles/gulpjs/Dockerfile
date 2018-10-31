FROM ubuntu:16.04

#install multiple package
RUN apt-get update && apt-get install -y \
nodejs \
npm \
vim

RUN mkdir -p /home/hello
WORKDIR /home/hello
#Try installing your dependencies first
#RUN npm install
RUN npm install -g gulp

#create a symlink from nodejs to node with
RUN ln -s `which nodejs` /usr/bin/node

#a html file to be minified
RUN mkdir -p /home/hello/html
RUN echo "<html>" > html/test.html
RUN echo "<body>" >> html/test.html
RUN echo "<h2>" >> html/test.html
RUN echo "test" >> html/test.html
RUN echo "</h2>" >> html/test.html
RUN echo "<body>" >> html/test.html
RUN echo "</html>" >> html/test.html

#
RUN npm install --save-dev gulp-minify-html
RUN echo "var gulp = require('gulp')" > gulpfile.js
RUN echo ", minifyHtml = require('gulp-minify-html');" >> gulpfile.js
RUN echo "gulp.task('minify-html', function () {" >> gulpfile.js
RUN echo "    gulp.src('./html/test.html') // path to your files" >> gulpfile.js
RUN echo "    .pipe(minifyHtml())" >> gulpfile.js
RUN echo "    .pipe(gulp.dest('path/to/destination'));" >> gulpfile.js
RUN echo "});" >> gulpfile.js

#create a local link to the globally installed Gulp module
# fix "Local gulp not found in /home/hello" problem
RUN npm link gulp
RUN gulp minify-html

#javascript files to be concated
RUN mkdir -p /home/hello/javascript
RUN echo "function foo() { alert('hello'); }" > javascript/foo.js
RUN echo "function bar() { foo(); }" > javascript/bar.js
RUN echo "<html>" >> javascript/index.html
RUN echo "<body>" >> javascript/index.html
RUN echo "<input type='button' onclick='bar();' value='Start' style='font-size: 25px;'></input>" >> javascript/index.html
RUN echo "<body>" >> javascript/index.html
RUN echo "</html>" >> javascript/index.html

#
RUN npm install --save-dev gulp-concat
RUN echo "var concat = require('gulp-concat');" >> gulpfile.js
RUN echo "gulp.task('concat', function () {" >> gulpfile.js
RUN echo "    gulp.src('./javascript/*.js') // path to your files" >> gulpfile.js
RUN echo "    .pipe(concat('concat.js'))  // concat and name it 'concat.js'" >> gulpfile.js
RUN echo "    .pipe(gulp.dest('path/to/destination'));" >> gulpfile.js
RUN echo "});" >> gulpfile.js
RUN gulp concat


ENTRYPOINT ["/bin/bash"]

#ref:
#https://julienrenaux.fr/2014/05/25/introduction-to-gulp-js-with-practical-examples/
