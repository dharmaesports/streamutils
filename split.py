# each int in this array is a second to split on; will start at the first entry,
# so it should probably start with 0; it will go from the last entry to the end
# of the video
splits_in_seconds = [0, 60, 120]

# input file name
input_filename = 'DITP2MeleeSinglesPools.mkv'

# output parameters; output files will follow the pattern:
# "{output_base} 001 - {descriptor_item}{output_extension}"
# descriptors must be same length as splits_in_seconds
output_base = 'DITP2 Melee Doubles'
descriptors = ['Team A Vs Team B', 'Team C vs Team D', 'Team A vs Team D']
output_extension = '.mp4'


import ffmpeg

num_splits = len(splits_in_seconds)
last_split_index = num_splits - 1

for split_index in range(0, num_splits):
    vid_index = split_index + 1
    vid_index_string = str(vid_index).zfill(3) # 3 is number of digits in the index output

    if split_index < last_split_index:
        dur = splits_in_seconds[split_index + 1] - splits_in_seconds[split_index]
        stream = ffmpeg.input(input_filename, ss=splits_in_seconds[split_index], t=dur)
    else:
        stream = ffmpeg.input(input_filename, ss=splits_in_seconds[split_index])

    stream = ffmpeg.output(stream, output_base + ' ' + vid_index_string + ' - ' + descriptors[split_index] + output_extension, acodec='copy', vcodec='copy')
    ffmpeg.run(stream)
