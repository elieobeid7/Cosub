Cosub beta version
===================


I created Cosub to download subtitles for the TV series I watch, convert them from MKV to MP4, because my TV doesn't support MKV, then download subtitles and finally rename the subtitles to match the names of the movie files so that the TV would load then 

----------


Features
-------------

> - It asks you a bunch of questions 
> - It can convert from any format to any format, primarily tested by converting MKV to MP4, because that's what it was created for, you can change the FFMPEG options in **main.py, line 97** 
> - It deletes sends the original files to trash using [Send2Trash](https://github.com/hsoft/send2trash)
> - It downloads subtitles using [Subliminal](https://github.com/Diaoul/subliminal) 
> - It renames the subtitles to match the names of the files
> - If you leave the path empty, the folder that you are currently in is considered as your path
> - The script detects the operating system you're using and should in theory work on any platform, but for the time being, it's only tested on Linux



##  Known issues

 > - Subliminal can't download subtitles to movies located in sub folders, it will cause the program to crash. [Issue reported here.](https://github.com/Diaoul/subliminal/issues/771)  
 > - The program has been tested only on Fedora 25

## Requirements

> - Python 2.7
> - Send2Trash
> - Subliminal

## TODO
> - Packaging
> - Testing on Mac and Windows