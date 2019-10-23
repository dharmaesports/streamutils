# streamutils

A project to help Dharma Esports do various stream activities. Currently this holds the code for using ffmpeg to split VoDs quickly. **This code has only been tested on Mac and would need modification to work on Windows**. To split your VoD, do the following:

1. install dependencies by running `bash install.sh` in a terminal window (this assumes you have pip installed).

1. Download this code from github (if you download as a zip file, extract all files).

1. copy the VoD you want to split into the same folder as this code.

1. edit `input_filename` in split.py to be the name of your VoD file.

1. Edit `splits` to be the chunks you want to split the video into. Each row is in this format: (beginning timestamp, ending timestamp, video description).

1. Edit `output_base` to be the tournament name (or whatever you want to be at the beginning of each video).

1. run 'python split.py' in a terminal window in the same directory as this code.