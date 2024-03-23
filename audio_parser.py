from vosk import Model, KaldiRecognizer
import wave
import json
from datetime import datetime

vosk_model_path = "models/vosk-model-en-us-0.42-gigaspeech"

def new_audio_model():
    model = Model(vosk_model_path)
    return model

def parse_file(model, out_file):
    phrases = []
    start_time = datetime.now()
    print("Starting Transcription")

    with wave.open(out_file, 'rb') as wf:
        recognizer = KaldiRecognizer(model, wf.getframerate())
        recognizer.SetWords(True)

        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                result_json = json.loads(result)
                phrases.append(result_json)

    print("Transcription Finished. Elapsed Time:" + str(datetime.now() - start_time))

    return phrases