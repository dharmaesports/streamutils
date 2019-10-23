import ffmpeg

# each int in this array is a second to split on; will start at the first entry,
# so it should probably start with 0; it will go from the last entry to the end
# of the video
splits_in_seconds = [0, 552, 1166, 1682, 2180, 2667, 3275, 4093, 5400, 6023, 6622, 7454, 8017, 8659, 9840, 10591, 11185]
descriptors = ['Vincessant Vs Soup Nazi', 'Jaded Vs Soup Nazi', 'Panda Vs Vincessant', 'Bladewise Vs Rosebud', 'Panda Vs Soup Nazi', 'Panda Vs Jaded', 'Panda Vs Dacky', 'Vincessant Vs Blink', 'Luigi Ka-Master Vs Melo', 'Bladewise Vs Kramer', 'Bladewise Vs Vincessant', 'Dacky Vs Melo', 'Panda Vs Luigi Ka-Master', 'Panda Vs Bladewise', 'Luigi Ka-Master Vs Dacky', 'Panda Vs Luigi Ka-Master', 'Panda Vs Bladewise']

# input file name
input_filename = 'Diamond in the puff 1.mkv'

# output parameters; output files will follow the pattern:
# "{output_base} 001 - {descriptor_item}{output_extension}"
# descriptors must be same length as splits_in_seconds
output_base = 'DITP1 Melee Singles'
output_extension = '.mp4'


num_splits = len(splits_in_seconds)
print(num_splits)
last_split_index = num_splits - 1

for split_index in range(0, num_splits):
    print(split_index)
    vid_index = split_index + 1
    vid_index_string = str(vid_index).zfill(3) # 3 is number of digits in the index output

    if split_index < last_split_index:
        dur = splits_in_seconds[split_index + 1] - splits_in_seconds[split_index]
        stream = ffmpeg.input(input_filename, ss=splits_in_seconds[split_index], t=dur)
    else:
        stream = ffmpeg.input(input_filename, ss=splits_in_seconds[split_index])

    stream = ffmpeg.output(stream, output_base + ' ' + vid_index_string + ' - ' + descriptors[split_index] + output_extension, acodec='copy', vcodec='copy')
    ffmpeg.run(stream)
