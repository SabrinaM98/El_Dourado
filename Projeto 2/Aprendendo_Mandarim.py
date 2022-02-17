# -*- coding: utf-8 -*-
"""aprendendo_mandarim.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/157Md0KjhWzVpU_T0DUqf_2stHl-gvG0I

# Transcrevendo aúdio em chinês com as APIs de fala da IBM

De caracteres em mandarim para aúdio
"""

!pip install ibm_watson wget

import json
from ibm_watson import TextToSpeechV1, SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticatorTTS = IAMAuthenticator('uE5xgRYWFhtHBAnd_5xHLiWXTHMIuUnEq_4CbF7hcg9V')
text_to_speech = TextToSpeechV1(
    authenticator=authenticatorTTS
)

text_to_speech.set_service_url('https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/5ed0b86c-c03d-4a5a-9c49-5a57edab7846')

with open('dianxia_cn.wav', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            '太子殿下',
            voice='zh-CN_ZhangJingVoice',
            accept='audio/wav'        
        ).get_result().content)

"""Audio para caracteres em mandarim"""

url_s2t = "https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/b552f651-24d8-45bb-8564-1e934c9e51ac"
iam_apikey_s2t = "4C1jFpg54OiM8AbrHysCKBU9aii4kSYDyMvNOxcWTabE"

authenticatorSTT = IAMAuthenticator(iam_apikey_s2t)
speech_to_text = SpeechToTextV1(authenticator=authenticatorSTT)
speech_to_text.set_service_url(url_s2t)
speech_to_text

filename='audio_2022-02-16_17-02-03.wav'

with open(filename, mode="rb") as wav:
    response = speech_to_text.recognize(audio=wav, content_type='audio/wav', model='zh-CN_BroadbandModel')

response.result

from pandas import json_normalize

json_normalize(response.result['results'],"alternatives")