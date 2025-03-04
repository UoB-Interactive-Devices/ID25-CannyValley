import os
import speech_recognition as sr
from transformers import pipeline

audio_path = "audio_file.wav"


def capture_audio():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    with open(audio_path, "wb") as f:
        f.write(audio.get_wav_data())

# openai too slow... ideally use a local version that's not ~$£% ->



capture_audio()
sent = recog()
print(sent)

#  classification of emotion using roberta

classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)
model_outputs = classifier(sent)
print(model_outputs[0])


# linking to our model:
'''
1. Low Arousal + Positive (LA + P) 

2. Normal Arousal + Positive (NA + P) 

3. High Arousal + Positive (HA + P) 

4. Low Arousal + Negative (LA + N) 

5. Normal Arousal + Negative (NA + N) 

6. High Arousal + Negative (HA + N) 
'''
# we could have 20 sentences for each of these and use RL to select the best.

# baseline approach:



## regression approac:






