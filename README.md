# JordanSearch

JordanSearch is my final project

## Dependencies

JordanSearch uses [ffmpeg](https://ffmpeg.org/documentation.html), [Vosk](https://alphacephei.com/vosk/), and [ElasticSearch](https://www.elastic.co/guide/index.html).

## Instructions

- Download your desired [Vosk Model](https://alphacephei.com/vosk/models) and place it in the main directory. I used the `vosk-model-en-us-0.42-gigaspeech` in my development. If you use a different one, you will need to change `vosk_model_path` in `audio_parser.py`.

- Place all video files in the `input` folder. They must be `.mp4` files.

- Run ElasticSearch with `docker-compose up -d`.

- Run `main.py` with the `-p` flag to parse all video files.

- Now, you can search for queries and if will return the top results including the file name and timestamp.

- As long as you are using the same ElasticSearch instance, re-running `main.py` without the `-p` flag will skip parsing and begin query entry.

## Todo

- Implement visual transcription

- Implement opening up the source files at the chosen timestamps

- Implement a GUI