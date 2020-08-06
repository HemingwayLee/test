#
Install `tesseract`, make sure tesseract cli is installed in your system
```
which tesseract
```

# Change all png files into tif files
```
for foo in *.png; do mv $foo `basename $foo .png`.tif; done
```

# Generate box files by tif files
```
./boxfile_generator.sh /path/to/english/images eng
./boxfile_generator.sh /path/to/japanese/images jpn
```


