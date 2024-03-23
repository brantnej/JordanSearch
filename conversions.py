import ffmpeg
import os

out_file = "audio.wav"
out_image = "image.jpg"

def extract_audio(file_name):
    clean_up_audio()

    stream = ffmpeg.input(file_name)
    stream = ffmpeg.output(stream, out_file, format='wav', ac=1)
    ffmpeg.run(stream)

    return out_file

def extract_image(file_name, timestamp):
    clean_up_image()

    stream = ffmpeg.input(file_name, ss=timestamp)
    stream = ffmpeg.output(stream, out_image, vframes=1)
    ffmpeg.run(stream)

    return out_image


def clean_up_audio():
    if os.path.exists(out_file):
        os.remove(out_file)

def clean_up_image():
    if os.path.exists(out_image):
        os.remove(out_image)

def seconds_to_timestamp(seconds):
    m = seconds // 60
    s = str(seconds % 60)
    h = str(m // 60)
    m = str(m % 60)
    if len(s) == 1:
        s = "0" + s
    if len(m) == 1:
        m = "0" + m
    if len(h) == 1:
        h = "0" + h
    return h + ":" + m + ":" + s