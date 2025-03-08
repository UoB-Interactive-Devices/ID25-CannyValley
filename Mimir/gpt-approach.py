# import openai
#
# openai.api_key = "OPENAI-KEY"
#
# response = openai.ChatCompletion.create(
#         model="gpt-4o",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": "What is the capital of France?"}
#         ],
#         temperature=1.0)
#
# print(response['choices'][0]['message']['content'])

'''
start
'''
from openai import OpenAI
import openai
client = OpenAI(
    api_key= "OPENAI-KEY",
)

import pyaudio
import speech_recognition as sr
p = pyaudio.PyAudio()
openai.api_key = "OPENAI-KEY"

def get_voice_input():
    """
    Capture audio from the microphone, save it as a WAV file,
    and use OpenAI's Whisper via the new interface to transcribe it.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Please speak.")
        audio = r.listen(source)
    audio_path = "audio_file.wav"
    with open(audio_path, "wb") as f:
        f.write(audio.get_wav_data())

    try:
        with open(audio_path, "rb") as audio_file:
            transcript = openai.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
        recognized_text = transcript.text
        print("You said:", recognized_text)
        return recognized_text
    except Exception as e:
        print("Error during transcription:", e)
        return None


def speak_text(text):
    stream = None
    first_chunk = True  # Flag to discard the first chunk if needed

    with client.audio.speech.with_streaming_response.create(
            model="tts-1",
            voice="ash",
            input=text,
            response_format="wav"
    ) as response:
        for chunk in response.iter_bytes(chunk_size=1024):
            if first_chunk:
                first_chunk = False
                continue

            if stream is None and len(chunk) > 0:
                stream = p.open(format=pyaudio.paInt16,
                                channels=1,
                                rate=24000,
                                output=True)
            if stream:
                stream.write(chunk)
    if stream:
        stream.stop_stream()
        stream.close()

def get_assistant_reply(messages):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )
    return response.choices[0].message.content



def main():
    messages = [{
        "role": "system",
        "content": (
            "You are an emotion regulation assistant. "
            "Your responses should be empathetic, concise, and focused. "
            "Limit your answers to two to three sentences, and only provide one actionable suggestion or one clarifying question per response. "
            "Avoid overly long or generic replies, and ensure that each response is tailored to the user's emotional state."
        )
    }]
    print("Voice conversation started. Say 'exit' or 'quit' to stop.")

    while True:
        user_text = get_voice_input()
        if user_text is None:
            continue
        if user_text.lower() in ["exit", "quit"]:
            print("Exiting conversation.")
            break

        messages.append({"role": "user", "content": user_text})
        assistant_reply = get_assistant_reply(messages)
        print("Assistant:", assistant_reply)
        messages.append({"role": "assistant", "content": assistant_reply})
        speak_text(assistant_reply)

    p.terminate()


if __name__ == "__main__":
    main()
