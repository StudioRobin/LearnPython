from pydub import AudioSegment
import math
import os

def split_mp3(filename, max_size_mb, output_folder):
    # Load the MP3 file
    audio = AudioSegment.from_mp3(filename)

    # Calculate the target length of each segment in milliseconds
    target_length = (max_size_mb * 1024 * 1024 * 8) // (128 * 1024) * 1000

    # Calculate the number of segments
    number_of_segments = math.ceil(len(audio) / target_length)

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Split and export the segments
    for i in range(number_of_segments):
        start = i * target_length
        end = min((i + 1) * target_length, len(audio))
        segment = audio[start:end]
        output_filename = os.path.join(output_folder, f'segment_{i}.mp3')
        segment.export(output_filename, format="mp3")

# Specify your MP3 file and output directory here
source_file = "/path/to/audio.mp3"
output_directory = "/path/to/output_directory/"
max_file_size_mb = 25

split_mp3(source_file, max_file_size_mb, output_directory)


=======================


curl --request POST \
  --url https://api.openai.com/v1/audio/transcriptions \
  --header 'Authorization: Bearer sk-xxx' \
  --header 'Content-Type: multipart/form-data' \
  --form file=@/home/ubuntu/whisper/trailer_audio.flac \
  --form model=whisper-1
