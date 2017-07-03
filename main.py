import os
import subprocess
from sys import platform as _platform
from babelfish import Language
from subliminal import download_best_subtitles, region, save_subtitles, scan_videos
from send2trash import send2trash


# Ask the user a bunch of questions and process the input


print("Cosub is a video converter that will:")
print("- Scan all your video folders Looking for videos. (And subfolders, optional)")
print("- Convert videos, then delete the original video to trash (Optional)")
print("- Download subtitles that match the tv series/movie files (Optional)")
print("- Remove the subtitle language code so that you could watch it on tv")
print("- For more info please visit: ")

originalFormat = raw_input("Please enter a format you wish to convert: ")
convertedFormat = raw_input("What format to convert to?: ")
inputPath = raw_input("Enter the path of the folder containing the videos: ")
dirBooloan = raw_input("Do you wish to scan subfolders? Yes or No: ")
deleteBoolean = raw_input(
    "Do you wish to delete videos after convertion? Yes or No: ")
subtitlesBoolean = raw_input("Do you want to download subtitles? Yes or No: ")
subtitlesBoolean.strip()
dirBooloan.strip()
deleteBoolean.strip()
originalFormat.strip()
convertedFormat.strip()
inputPath.strip()
movie_list = []
listCounter = 0
# Complete the path on windows and linux/mac

if (_platform == "win64" or _platform == "win32"):
    if (inputPath.endswith("\\")):
        pass
    else:
        inputPath = inputPath + "\\"
else:
    if (inputPath.endswith("/")):
        pass
    else:
        inputPath = inputPath + "/"

if (deleteBoolean == 'Yes' or deleteBoolean == 'YES' or deleteBoolean == 'yes' or deleteBoolean == 'y' or deleteBoolean == 'Y'):
    deleteBoolean = True
else:
    deleteBoolean = False
if (dirBooloan == 'Yes' or dirBooloan == 'YES' or dirBooloan == 'yes' or dirBooloan == 'y' or dirBooloan == 'Y'):
    dirBooloan = True
else:
    dirBooloan = False

if (subtitlesBoolean == 'Yes' or subtitlesBoolean == 'YES' or subtitlesBoolean == 'yes' or subtitlesBoolean == 'y' or subtitlesBoolean == 'Y'):
    subtitlesBoolean = True
else:
    subtitlesBoolean = False

# If the user wants to download subtitles run this code, and get the first
# 2 letters of subtitles, will be used to delet srt language code from srt
# files

if (subtitlesBoolean == True):
    subtitlesLanguageCode = raw_input(
        "Please enter subtiles language code(first 3 letters - Read https://www.loc.gov/standards/iso639-2/php/code_list.php ) : ")
    subtitlesLanguageCode.strip()
if (convertedFormat.startswith('.')):
    pass
else:
    convertedFormat = '.' + convertedFormat

if (originalFormat.startswith('.')):
    pass
else:
    originalFormat = '.' + originalFormat

# rename subtitles


def renameSubs():
    global listCounter
    if file.endswith('.srt'):
        if listCounter <= len(movie_list):
            os.rename(inputPath + file, inputPath +
                      movie_list[listCounter] + '.srt')
            listCounter = listCounter + 1


# converts videos and removes language code from .srt

def converter():
    name = file[:file.rfind(".")]
    if file.endswith(originalFormat):
        movie_list.append(name)
        subprocess.call(["ffmpeg", "-i", inputPath + name + originalFormat,
                         "-codec", "copy", inputPath + name + convertedFormat])
        if (deleteBoolean == True):
            send2trash(inputPath + file)

# download subtitles


def downloadSubs():
    region.configure('dogpile.cache.dbm', arguments={
        'filename': 'cachefile.dbm'})
    videos = scan_videos(inputPath)
    subtitles = download_best_subtitles(
        videos, {Language(subtitlesLanguageCode)})
    for video in videos:
        save_subtitles(video, subtitles[video])


if (subtitlesBoolean == True):
    downloadSubs()

if (dirBooloan == True):
    for root, dirs, files in os.walk(inputPath):
        for file in files:
            converter()
    for root, dirs, files in os.walk(inputPath):
        for file in files:
            renameSubs()


else:
    for file in os.listdir(inputPath):
        converter()
    for file in os.listdir(inputPath):
        renameSubs()
