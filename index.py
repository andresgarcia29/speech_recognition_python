#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import requests
import json
import pprint
import json

def transcribe_file(speech_file):
    """Transcribe the given audio file."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code='es-MX')

    response = client.recognize(config, audio)

    for index, result in enumerate(response.results):
        print("Resultado: " + str(index+1))
        print(result.alternatives[0].transcript.encode('utf-8', 'strict'))
        print("")

if __name__ == '__main__':
    transcribe_file('prueba.wav')