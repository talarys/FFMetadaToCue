# FFmpeg chapters metadata to CUE sheet file

This is a simple script that takes an audiobook file, uses ffprobe to get the chapters metadata and parses it into a .cue file.
It should work on any file that contains chapters metadata, which is most .m4b files and some .mp3.

## IMPORTANT
This script has only one dependency, you need to have ffmpeg or at least ffprobe installed on your system.

## How to use
```console
python FFMetadataToCue.py target_file.m4b
```
This will create a cue file in the same directory as the target file