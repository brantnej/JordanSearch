import ffmpeg
import os

out_file = "audio.wav"

def convert_file(file_name):
    clean_up_audio_converter()

    stream = ffmpeg.input(file_name)
    stream = ffmpeg.output(stream, out_file, format='wav', ac=1)
    ffmpeg.run(stream)

    return out_file

def clean_up_audio_converter():
    if os.path.exists(out_file):
        os.remove(out_file)