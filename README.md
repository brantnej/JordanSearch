# JordanSearch

JordanSearch is my final project for CS 499 that focuses on parsing and indexing audio and visual content within videos so users can locate content within a large corpus of videos.

## Dependencies

JordanSearch uses [ffmpeg](https://ffmpeg.org/documentation.html), [Vosk](https://alphacephei.com/vosk/), [ElasticSearch](https://www.elastic.co/guide/index.html), and [ImageAI](https://imageai.readthedocs.io/en/latest/).

## Instructions

- Download your desired [Vosk Model](https://alphacephei.com/vosk/models) and your [ImageAI model](https://imageai.readthedocs.io/en/latest/customdetection/) and place it in the `models` directory. I used `vosk-model-en-us-0.42-gigaspeech` and `YOLOv3` in my development. If you use different models, you will need to change `vosk_model_path`, `imageai_model_path`, and the ImageAI model type in `audio_parser.py` and `image_parser.py` respectively.

- Place all video files in the `input` folder. They must be `.mp4` files.

- Run ElasticSearch with `docker-compose up -d`.

- Run `main.py` with the `-p` flag to parse all video files.

- Now, you can search for queries and if will return the top results including the file name and timestamp.

- As long as you are using the same ElasticSearch instance, re-running `main.py` without the `-p` flag will skip parsing and begin query entry.

- If you use the `-f` flag, you will search for full videos rather than finding specific timestamps within those videos.

## Todo

- Implement opening up the source files at the chosen timestamps

- Implement a GUI

- Use an LLM to generate keywords summarizing what the audio is *about*, so users don't have to search by exact match of content

- Use an audio model that can also parse sound effects, rather than just dialogue

- Use an image model that can identify more than just 80 items