import ffmpeg

# each row will end up in its own video
# each row is in the format (beginning timestamp, ending timestamp, description)
# timestamps are in format 'hh:mm:ss'
splits = [
    ('00:00:00', '03:03:05', 'A Vs B'),
    ('03:03:05', '03:04:08', 'C Vs D')
]

# input file name
input_filename = 'Diamond in the puff 1.mkv'

# output parameters; output files will follow the pattern:
# "{output_base} 001: {descriptor_item}{output_extension}"
output_base = 'DITP1 Melee Singles'
output_extension = '.mp4'


def timestamp_to_seconds(t):
    parts = t.split(':')
    return int(parts[0])*3600 + int(parts[1])*60 + int(parts[2])

num_splits = len(splits)
for split_index in range(0, num_splits):
    vid_index = split_index + 1
    vid_index_string = str(vid_index).zfill(3) # 3 is number of digits in the index output

    beginning_timestamp = splits[split_index][0]
    ending_timestamp = splits[split_index][1]
    descriptor = splits[split_index][2]
    beginning_second = timestamp_to_seconds(beginning_timestamp)
    ending_second = timestamp_to_seconds(ending_timestamp)
    dur = ending_second - beginning_second

    stream = ffmpeg.input(input_filename, ss=beginning_second, t=dur)
    stream = ffmpeg.output(stream, output_base + ' ' + vid_index_string + ': ' + descriptor + output_extension, acodec='copy', vcodec='copy')
    ffmpeg.run(stream)
