# streamutils

A project to help Dharma Esports do various stream activities. Currently this holds the code for using ffmpeg to split VoDs quickly. **This code has only been tested on Mac**. To split your VoD, do the following:

1. Download this code from github (if you download as a zip file, extract all files).

1. Copy the VoD you want to split into the same folder as the downloaded code.

1. Install dependencies by running `bash install.sh` in a terminal window in the same folder as the downloaded code (this assumes you have pip installed). NOTE: this will only work on Mac/Linux. That being said, at the moment all this does is install the python bindings for ffmpeg. If you are trying to run this on Windows, you _might_ be able to run this command instead: `pip install ffmpeg-python`.

1. Edit `input_filename` in split.py to be the name of your VoD file.

1. Edit `splits` to be the chunks you want to split the video into. Each row is in this format: (beginning timestamp, ending timestamp, video description).

1. Edit `output_base` to be the tournament name (or whatever you want to be at the beginning of each video).

1. Run 'python split.py' in a terminal window in the same directory as this code.