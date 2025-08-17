# How to run
* `moviepy` does not work well in python script, use `subprocess.run` with `ffmpeg` command instead

## Run with Dockerfile
```
docker run -it --rm -v $(pwd):/home/proj/ myvideo bash
```

* using `ffmpeg` with `"crop=width:height:x:y"`
```
ffmpeg -i my_16_9_video.mp4 -vf "crop=128:128:0:0" -c:v libx264 -c:a aac output_test.mp4
```


