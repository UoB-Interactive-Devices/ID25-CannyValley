import os
import random, time, pyttsx3
import speech_recognition as sr
import pyaudio
from openai import OpenAI
import pygame
import threading


client = OpenAI(
    api_key= "OPENAI-KEY",
)
p = pyaudio.PyAudio()

import defaultaiChoices

# it'd be better to do use transformers - but this'll do:
yes_responses = ["yes", "yeah", "yep", "sure", "yup"]
no_responses = ["no", "nope", "nah", "not really", "not now", "later"]
stop_keywords = ["stop", "pause", "end", "quit", "finish", "stop music", "turn off", "enough"]

def contains_keywords(text, keywords):
    """
    Checks if any keyword from the list is present in the text.
    """
    text = text.lower()
    return any(keyword in text for keyword in keywords)

def get_voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Please speak.")
        audio = r.listen(source)

    audio_path = "audio_file.wav"
    with open(audio_path, "wb") as f:
        f.write(audio.get_wav_data())
    try:
        with open(audio_path, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
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
    first_chunk = True

    try:
        with client.audio.speech.with_streaming_response.create(
                model="tts-1",
                voice="nova",
                input=text,
                response_format="wav"
        ) as response:
            for chunk in response.iter_bytes(chunk_size=1024):
                # Skip first chunk to avoid initial noise
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
    except Exception as e:
        print(f"Error during text-to-speech: {e}")
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()


def clean_sentence_end(text):
    if not text:
        return text

    punctuation_marks = ['.', '!', '?', ',', ';', ':', '"', "'"]

    while text and text[-1] in punctuation_marks:
        text = text[:-1]

    return text

def voice_input(prompt=""):
    speak_text(prompt)

    print(prompt, end=" ")
    try:
        user_input = get_voice_input()
        if not user_input:  # If voice recognition fails, fall back to text input
            user_input = input("Voice recognition failed. Please type your response: ")
        return clean_sentence_end(user_input)
    except Exception as e:
        print(f"Error with voice input: {e}")
        return clean_sentence_end(input("Please type your response: "))

pygame.mixer.init()


def listen_for_stop_command():
    stop_keywords = ["stop", "pause", "end", "quit", "finish", "stop music", "turn off", "enough"]

    while pygame.mixer.music.get_busy():
        voice_input = get_voice_input().lower()

        if any(keyword in voice_input for keyword in stop_keywords):
            pygame.mixer.music.stop()
            print("Music stopped")
            break

        time.sleep(0.5)  # Check every half second


def playmusic(number):
    message = "Playing music"
    print(message)
    speak_text(message)
    files = [ "energise.mp3", "calm.mp3",  "focus.mp3", "happy.mp3"]
    music_file = os.path.join(os.path.dirname(__file__), "music", files[number])
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()

    try:
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play()
        print(f"Now playing: {music_file}")
        print("Say 'stop' to end music playback")
        stop_thread = threading.Thread(target=listen_for_stop_command)
        stop_thread.daemon = True
        stop_thread.start()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

    except Exception as e:
        print(f"Error playing music: {e}")

def dosensors():
    x = 0
    return x


def lightsUp():
    message = "Lights going up"
    print(message)
    speak_text(message)


def lightsDown():
    message = "Lights going down"
    print(message)
    speak_text(message)


def deepBreaths():
    prompt = "We're going to take some deep breaths now, if that's alright?"
    response = voice_input(prompt).lower()

    if not contains_keywords(response, no_responses):
        for i in range(3):
            time.sleep(1)
            message = "Breathe in"
            print(message)
            speak_text(message)
            time.sleep(1)

            message = "Hold it"
            print(message)
            speak_text(message)
            time.sleep(1)

            message = "And breathe out"
            print(message)
            speak_text(message)
    elif contains_keywords(response, no_responses):
        message = "OK, we'll do something else."
        print(message)
        speak_text(message)
    else:
        message = "I didn't quite get that. Try again?"
        print(message)
        speak_text(message)
        deepBreaths()


hypeenvironments = [[["Club"], ["popping"], ["lights", "DJ"], ["goes hard"]]]

calmenvironments = [
    [["Rainforest"], ["lush", "verdant", "vibrant", "glimmering"], ["river", "trees", "canopy", "forest floor", "sun"],
     ["flickers", "emanates", "shines", "flows"]]]
sentences = [["the", "2", "is", "1"], ["Watch as the", "2", "3", "across the", "0"],
             ["Imagine the", "1", "2", "as it", "3"]]


def factoryReset():
    defaultaiChoices.writeDefault()


def describeEnvironment(number):
    if (number == 0 or number == 3):
        prompt = "I'm going to create a space for you to get into it now, if that's alright?"
        theinput = voice_input(prompt).lower()

        if contains_keywords(theinput, yes_responses):
            thisenv = random.randint(0, 2)
            thisenv = 0
            placename = str(hypeenvironments[thisenv][0])
            message = f"Welcome to the {placename}"
            print(message)
            speak_text(message)
            time.sleep(1)

            thesetimes = random.randint(4, 6)
            for i in range(thesetimes):
                whichsentence = random.randint(0, 2)
                sentence = ""
                for fragment in sentences[whichsentence]:
                    if fragment.isdigit():
                        value = int(fragment)
                        whichone = random.randint(0, len(hypeenvironments[thisenv][value]) - 1)
                        sentence += hypeenvironments[thisenv][value][whichone] + " "
                    else:
                        sentence += fragment + " "
                print(sentence)
                speak_text(sentence)
                time.sleep(1)
        elif contains_keywords(theinput, yes_responses):
            message = "OK, we'll do something else."
            print(message)
            speak_text(message)
        else:
            message = "I didn't quite get that. Try again?"
            print(message)
            speak_text(message)
            describeEnvironment(number)
    elif (number == 1 or number == 2):
        prompt = "I'm going to create a space for you to reflect now, if that's alright?"
        theinput = voice_input(prompt).lower()

        if contains_keywords(theinput, yes_responses):
            thisenv = random.randint(0, 2)
            thisenv = 0
            placename = str(calmenvironments[thisenv][0])
            message = f"Welcome to the {placename}"
            print(message)
            speak_text(message)
            time.sleep(1)

            thesetimes = random.randint(4, 6)
            for i in range(thesetimes):
                whichsentence = random.randint(0, 2)
                sentence = ""
                for fragment in sentences[whichsentence]:
                    if fragment.isdigit():
                        value = int(fragment)
                        whichone = random.randint(0, len(calmenvironments[thisenv][value]) - 1)
                        sentence += calmenvironments[thisenv][value][whichone] + " "
                    else:
                        sentence += fragment + " "
                print(sentence)
                speak_text(sentence)
                time.sleep(1)
        elif contains_keywords(theinput, no_responses):
            message = "OK, we'll do something else."
            print(message)
            speak_text(message)
        else:
            message = "I didn't quite get that. Try again?"
            print(message)
            speak_text(message)
            describeEnvironment(number)


myaffirmations = [[[0, 3], "Today is my day!"], [[2, 1], "I am enough"], [[1, 2], "I am loved"],
                  [[2, 1], "Through positive thought, I transform obstacles into stepping stones"],
                  [[0, 3], "Let's Go!"]]


def findanaffirmation(number):
    randomaff = random.randint(0, len(myaffirmations) - 1)
    number1 = myaffirmations[randomaff][0][0]
    number2 = myaffirmations[randomaff][0][1]
    if number == number1 or number == number2:
        return (myaffirmations[randomaff][1])
    else:
        foundaff = findanaffirmation(number)
        return foundaff


def saytheaffirmation(theaff, times):
    if times < 3:
        print(f"{theaff} ")
        speak_text(theaff)
        theirinput = voice_input()

        if (theirinput.lower() == theaff.lower()):
            time.sleep(1)
            saytheaffirmation(theaff, times + 1)
        else:
            message = "Give it another try!"
            print(message)
            speak_text(message)
            time.sleep(1)
            saytheaffirmation(theaff, times)
    else:
        return ()


def positiveAffirmations(number):
    if (number == 3):
        prompt = "Let's get hyped! You good to chant back to me?"
        theinput = voice_input(prompt).lower()

        if contains_keywords(theinput, yes_responses):
            thisaff = findanaffirmation(number)
            saytheaffirmation(thisaff, 0)
        elif contains_keywords(theinput, no_responses):
            message = "OK, we'll do something else."
            print(message)
            speak_text(message)
        else:
            message = "I didn't quite get that. Try again?"
            print(message)
            speak_text(message)
            positiveAffirmations(number)
    elif (number == 2):
        prompt = "Let's get into it, time to shout back after me"
        theinput = voice_input(prompt).lower()

        if contains_keywords(theinput.lower(), yes_responses):
            thisaff = findanaffirmation(number)
            saytheaffirmation(thisaff, 0)
        elif contains_keywords(theinput, no_responses):
            message = "OK, we'll do something else."
            print(message)
            speak_text(message)
        else:
            message = "I didn't quite get that. Try again?"
            print(message)
            speak_text(message)
            positiveAffirmations(number)
    elif (number <= 1):
        prompt = "Alright, let's repeat after me"
        theinput = voice_input(prompt).lower()

        if contains_keywords(theinput, yes_responses):
            thisaff = findanaffirmation(number)
            saytheaffirmation(thisaff, 0)
        elif contains_keywords(theinput, no_responses):
            message = "OK, we'll do something else."
            print(message)
            speak_text(message)
        else:
            message = "I didn't quite get that. Try again?"
            print(message)
            speak_text(message)
            positiveAffirmations(number)


questionbank = [["Does this energy feel directed toward something, or is it more free and spontaneous?",
                 "Would you describe this feeling as an intense push forward or a steady momentum?",
                 "Do you feel more in control of this energy, or is it carrying you along?",
                 "If this feeling had a sound, would it be loud and fast or rhythmic and steady?",
                 "Does this energy make you want to take action, or simply enjoy the feeling?",
                 "Would you say this energy is building up, staying consistent, or already peaking?"],
                ["Does this feel like an ordinary state for you, or is today a little different?",
                 "Are you feeling naturally balanced, or did something shift your mood in a good way?",
                 "Does this feel like a moment of quiet focus or a sense of lightness?",
                 "Are you drawn toward something specific, or are you simply going with the flow?",
                 "If this feeling had a pace, would it be slow and steady or gently moving forward?",
                 "Is this the kind of feeling you'd like to hold onto for a while?"],
                ["Does this feel like a moment of stillness or a familiar sense of calm?",
                 "Are you simply resting, or does this feel like a deeper kind of ease?",
                 "Does this moment feel like something you intentionally created or something that just happened?",
                 "Are your thoughts clear, or are they drifting freely?",
                 "Do you feel present in this moment, or is your mind wandering elsewhere?",
                 "If this feeling were a color, would it be soft and muted or warm and rich?"],
                ["Does this energy feel useful, or does it feel like it's pulling in too many directions?",
                 "Is your mind jumping between thoughts, or is it locked onto one thing?",
                 "Does this feeling make you want to move, or does it feel like too much all at once?",
                 "Would you describe this energy as something building up or something already at its peak?",
                 "If this feeling had motion, would it be fast and scattered or sharp and intense?",
                 "Do you feel like this state is leading somewhere, or does it feel like it's circling back on itself?"],
                ["Would you describe this mood as something vague or something clear but hard to define?",
                 "Does this feel like a pause in momentum or a general sense of uncertainty?",
                 "Would you say this moment is still or slightly off balance?",
                 "Do your thoughts feel structured, or are they moving in many directions?",
                 "If this feeling were a space, would it be open and empty or closed and uncertain?",
                 "Does this state feel neutral, or is there something beneath it waiting to surface?"],
                ["Does this feel more like a lack of energy or a weight that's hard to shake?",
                 "Is this a passing feeling, or has it been lingering for a while?",
                 "Would you describe this state as quiet and empty or full and heavy?",
                 "If this feeling had a texture, would it be soft and slow or dense and unmoving?",
                 "Do your thoughts feel distant, or are they looping in the background?",
                 "Would you say this moment needs stillness or a small shift?"]]


def physicalquestions(hr, posneg):
    q1R = 0
    q2R = 0
    value = 0
    if (hr == "high" and posneg == 1):
        value = 0
    elif (hr == "normal" and posneg == 1):
        value = 1
    elif (hr == "low" and posneg == 1):
        value = 2
    elif (hr == "high" and posneg == 0):
        value = 3
    elif (hr == "normal" and posneg == 0):
        value = 4
    elif (hr == "low" and posneg == 0):
        value = 5

    indexlist = list(range(len(questionbank[value])))
    questionsasked = random.randint(2, 4)

    for i in range(questionsasked):
        if not indexlist:
            break

        index_pos = random.randint(0, len(indexlist) - 1)
        index = indexlist.pop(index_pos)

        question = questionbank[value][index]
        print(question)
        speak_text(question)
        q1 = voice_input()
        time.sleep(3)


def rmm():
    heartrate = dosensors()
    if (heartrate > 50):
        userfeeling = "high"
    elif (heartrate <= 20):
        userfeeling = "normal"
    else:
        userfeeling = "low"

    qR = 0
    while qR == 0:
        prompt = "Would you say you're feeling more positive or negative right now?"
        q = voice_input(prompt)

        if q.lower() == "positive":
            qR = 1
        elif q.lower() == "negative":
            qR = 0
        else:
            message = "Can we try that again? I didn't quite catch that."
            print(message)
            speak_text(message)

    physicalquestions(userfeeling, qR)


def drinkWater():
    prompt = "Have you drunk water in the past hour?"
    drinkcheck = voice_input(prompt).lower()

    if contains_keywords(drinkcheck, yes_responses):
        message = "Good! Keep it up."
        print(message)
        speak_text(message)
    else:
        message = "Make sure to drink some water pretty soon, it helps you calm down."
        print(message)
        speak_text(message)
        time.sleep(5)

        prompt = "Have you had a drink yet?"
        watercheck = voice_input(prompt).lower()

        if contains_keywords(watercheck, yes_responses):
            return ()
        else:
            drinkWater()


def guideStretch():
    message = "Let's release some tension. For each position, we’ll hold for 8, but I’ll give you a bit of extra time to get into position."
    print(message)
    speak_text(message)
    time.sleep(3)

    message = "So, first, sit down cross-legged and raise your arms straight above your head and hold."
    print(message)
    speak_text(message)
    time.sleep(15)

    message = "Now move so you are lying on your front and push your top half up of the floor with your arms, trying to keep your legs flat against the floor. See if you can point your toes and curve your back and head back"
    print(message)
    speak_text(message)
    time.sleep(12)

    message = "And relax. Now place your hands in front of you and make sure your feet are firmly on the ground. Push up to create an upside-down V shape. This is the downwards dog."
    print(message)
    speak_text(message)
    time.sleep(11)

    message="Stand up and recentre yourself. Give a little shake to any muscles you feel like you used."
    print(message)
    speak_text(message)
    time.sleep(5)

def counttoFour():
    message = "One"
    print(message)
    speak_text(message)
    time.sleep(1)
    message = "Two"
    print(message)
    speak_text(message)
    time.sleep(1)
    message = "Three"
    print(message)
    speak_text(message)
    time.sleep(1)
    message = "Four."
    print(message)
    speak_text(message)

def guideMeditation():
    mediLoop=0
    while mediLoop<3:
        message = "Let’s take a moment to reset. Follow my guidance as we breathe together."
        print(message)
        speak_text(message)
        time.sleep(3)

        message = "Breathe in slowly through your nose."
        print(message)
        speak_text(message)
        time.sleep(1)
        counttoFour()
        time.sleep(0.5)

        message = "Now hold your breath."
        print(message)
        speak_text(message)
        time.sleep(1)
        counttoFour()
        time.sleep(0.5)

        message = "Gently breathe out through your mouth."
        print(message)
        speak_text(message)
        time.sleep(1)
        counttoFour()
        time.sleep(0.5)

        message = "Gently breathe out through your mouth."
        print(message)
        speak_text(message)
        time.sleep(1)
        counttoFour()
        time.sleep(0.5)

        mediLoop+=1

    message = "Take one final slow breath in and out. Notice how your body feels. You are calm, steady, and in control."
    print(message)
    speak_text(message)

locations = ["Africa"," a zoo","your house","a park"]
numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
colours = ["red","blue","pink","green","yellow","orange","white","black","purple"]
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]

def formSequence():
    sequencelist=[]
    loop=random.randint(5,7)
    iterate=1
    while iterate<loop:
        sequencelist.append(colours[random.randint(0,len(colours)-1)])
    return sequencelist

def playGame(number):
    if (number == 0):
        message = "Let's play a calm game. I want you to name 3 blue things you can see or imagine."
        print(message)
        speak_text(message)
        voice_input()
    elif (number == 1):
        message = "I’ve got a quick game for you. Are you ready for a challenge?"
        print(message)
        speak_text(message)
        voice_input()
        time.sleep(1)
        number=random.randint(len(locations)-1)
        message = ("An easy one to start: name three animals you would find in"+locations[number])
        print(message)
        speak_text(message)
        voice_input()
        message = ("Okay, maybe some maths next? What is "+str(numbers[random.randint(0,11)])+" times "+str(numbers[random.randint(0,11)])+"?")
        print(message)
        speak_text(message)
        voice_input()
        message = ("Cool, now can you name something that is ",colours[random.randint(0,len(colours)-1)])
        print(message)
        speak_text(message)
        voice_input()
        message = ("Nice. Now can you name somewhere beginning with "+letters[random.randint(0,len(letters)-1)])
        print(message)
        speak_text(message)
        voice_input()
        sequence = formSequence()
        message = ("Finally, can you remember this sequence: "+sequence)
        print(message)
        speak_text(message)
        voice_input()
        message="Well done, you did great! "
        print(message)
        speak_text(message)
        


def setGoal():
    prompt = "Let's set a goal! What can you get done in the next 5 minutes?"
    goaltoset = voice_input(prompt)

    message = "Sounds good! I'll see you then!"
    print(message)
    speak_text(message)

    time.sleep(30)  # Changed from 300 for testing purposes

    prompt = "Did you get it done?"
    complete = voice_input(prompt).lower()

    if contains_keywords(complete, yes_responses):
        message = "Amazing. Super productive."
        print(message)
        speak_text(message)
    else:
        message = "Unfortunate, but you'll get there next time!"
        print(message)
        speak_text(message)


def listGratitude():
    prompt = "OK, now it's time to talk gratitude. What's something you're grateful for today?"
    thing1 = voice_input(prompt)
    time.sleep(1)

    prompt = "And something else?"
    thing2 = voice_input(prompt)
    time.sleep(1)

    prompt = "Anything more?"
    thing3 = voice_input(prompt)
    time.sleep(1)

    message = "That sounds great!"
    print(message)
    speak_text(message)

def distractionCheck():
    message = "Let us make sure you can stay on track."
    print(message)
    speak_text(message)
    time.sleep(1)
    message = "Place your phone on do not disturb and make sure it is out of reach"
    print(message)
    speak_text(message)
    time.sleep(5)
    message = "Clear your working area. Remove any unnecessary paper or other distractions"
    print(message)
    speak_text(message)
    time.sleep(10)
    message = "If you are using a laptop, close those extra tabs and make sure your games or other distractions aren’t open"
    print(message)
    speak_text(message)
    time.sleep(5)
    message = "Take a second just to breath."
    print(message)
    speak_text(message)
    time.sleep(1)
    message = "OK, let's begin!"
    print(message)
    speak_text(message)

def physicalRoutine():
    message = "Are you ready to get that blood pumping?"
    print(message)
    speak_text(message)
    time.sleep(1)
    message = "Give me 5 jumping jacks first"
    print(message)
    speak_text(message)
    time.sleep(7)
    message = "Awesome. Now run on the spot until I say stop!"
    print(message)
    speak_text(message)
    time.sleep(10)
    message = "STOP! Well done, bit slower now so give me 5 squats."
    print(message)
    speak_text(message)
    time.sleep(12)
    message = "Now, a bit more running but get those knees as high as you can!"
    print(message)
    speak_text(message)
    time.sleep(10)
    message = "Great! Give me a bit of shadow boxing, just to finish"
    print(message)
    speak_text(message)
    time.sleep(10)
    message = "Don't you feel that blood pumping?"
    print(message)
    speak_text(message)


def cmm(aiChoices, goalmood):
    aiDecision = random.choice(aiChoices)
    if (aiDecision == 1):
        playmusic(goalmood)
    elif aiDecision == 2:
        deepBreaths()
    elif aiDecision == 3:
        describeEnvironment(goalmood)
    elif aiDecision == 4:
        positiveAffirmations(goalmood)
    elif aiDecision == 5:
        drinkWater()
    elif aiDecision == 6:
        guideStretch()
    elif aiDecision == 7:
        guideMeditation()
    elif aiDecision == 8:
        playGame(goalmood)
    elif aiDecision == 9:
        setGoal()
    elif aiDecision == 10:
        listGratitude()
    elif aiDecision == 11:
        physicalRoutine()
    elif aiDecision == 12:
        distractionCheck()
    



def takeUserFeedback(currentlist):
    prompt = "Give me input >"
    feedback = voice_input(prompt).lower()

    # Define keyword mappings
    keyword_actions = {
        "music": (1, ["music", "songs", "tune", "melody"]),
        "breathing": (2, ["breath", "breathing", "inhale", "exhale"]),
        "description": (3, ["description", "describing", "detail", "explain"]),
        "affirmations": (4, ["affirmation", "affirming", "positive", "encourage"]),
        "water": (5, ["water", "drink", "hydrate", "fluid"]),
        "stretching": (6, ["stretch", "stretching", "flexibility", "extend"]),
        "meditating": (7, ["meditate", "meditating", "meditation", "mindful"]),
        "games": (8, ["game", "games", "play", "activity"]),
        "goals": (9, ["goal", "goals", "target", "objective"]),
        "gratitude": (10, ["gratitude", "grateful", "thankful", "appreciation"])
    }

    more_words = ["more", "increase", "add", "extra", "additional"]
    less_words = ["less", "reduce", "decrease", "remove", "fewer"]

    more_requested = any(word in feedback for word in more_words)
    less_requested = any(word in feedback for word in less_words)

    while not (more_requested or less_requested):
        speak_text("You said: " + feedback + ". Let's try that again.")
        feedback = voice_input(prompt).lower()
        more_requested = any(word in feedback for word in more_words)
        less_requested = any(word in feedback for word in less_words)

    # Check which feature was mentioned
    for feature, (feature_id, keywords) in keyword_actions.items():
        if any(keyword in feedback for keyword in keywords):
            if more_requested:
                defaultaiChoices.choicesAdd([feature_id], currentlist)
                return 1
            elif less_requested:
                defaultaiChoices.choicesRemove([feature_id], currentlist)
                return 1


def checkFeedback(currentlist, numbergoup):
    numbergoup += 1
    if numbergoup % 5 == 0:
        prompt = "Have you had enough of this mode?"
        endinput = voice_input(prompt).lower()

        if contains_keywords(endinput, yes_responses):
            prompt = "Do you have any feedback?"
            anyfeedback = voice_input(prompt).lower()

            if contains_keywords(anyfeedback, yes_responses):
                takeUserFeedback(currentlist)
            return "break"
        else:
            prompt = "Do you have any feedback while we're still going?"
            anyfeedback = voice_input(prompt).lower()

            if contains_keywords(anyfeedback, yes_responses):
                takeUserFeedback(currentlist)

    return "continue"


def energyenhance():
    lightsUp()
    numbergoup = 0

    while True:
        aiChoices = defaultaiChoices.choicesRead()
        mylist = defaultaiChoices.populateChoices(0)
        aiChoices = aiChoices + mylist
        cmm(aiChoices, 0)

        breaking = checkFeedback(0, numbergoup)
        numbergoup += 1

        if breaking == "break":
            prompt = "Which would you like to do: switch modes or finish?"
            leave = voice_input(prompt)

            if leave.lower() == "finish":
                return "finish"
            else:
                return "switch"


def deeprelax():
    lightsDown()
    numbergoup = 0

    while True:
        aiChoices = defaultaiChoices.choicesRead()
        mylist = defaultaiChoices.populateChoices(1)
        aiChoices = aiChoices + mylist
        cmm(aiChoices, 1)

        breaking = checkFeedback(1, numbergoup)
        numbergoup += 1

        if breaking == "break":
            prompt = "Which would you like to do: switch modes or finish?"
            leave = voice_input(prompt)

            if leave.lower() == "finish":
                return "finish"
            else:
                return "switch"


def focus():
    lightsDown()
    numbergoup = 0

    while True:
        aiChoices = defaultaiChoices.choicesRead()
        mylist = defaultaiChoices.populateChoices(2)
        aiChoices = aiChoices + mylist
        cmm(aiChoices, 2)

        breaking = checkFeedback(2, numbergoup)
        numbergoup += 1

        if breaking == "break":
            prompt = "Which would you like to do: switch modes or finish?"
            leave = voice_input(prompt)

            if leave.lower() == "finish":
                return "finish"
            else:
                return "switch"


def happinessboost():
    lightsUp()
    numbergoup = 0

    while True:
        aiChoices = defaultaiChoices.choicesRead()
        mylist = defaultaiChoices.populateChoices(3)
        aiChoices = aiChoices + mylist
        cmm(aiChoices, 3)

        breaking = checkFeedback(3, numbergoup)
        numbergoup += 1

        if breaking == "break":
            prompt = "Which would you like to do: switch modes or finish?"
            leave = voice_input(prompt)

            if leave.lower() == "finish":
                return "finish"
            else:
                return "switch"


def navigate():
    noreply = True

    while noreply:
        message = """Hello, this is Mimir.
Would you like to:
1. Find Your Mood
2. Energy Enhance
3. Deep Relaxation
4. Focus 
5. Happiness Boost"""

        print(message)
        speak_text(message)

        navigation = voice_input()

        if navigation == "1" or "find" in navigation.lower() or "mood" in navigation.lower():
            rmm()
            noreply = False
        elif navigation == "2" or "energy" in navigation.lower() or "enhance" in navigation.lower():
            finish = energyenhance()
            if finish == "finish":
                noreply = False
        elif navigation == "3" or "deep" in navigation.lower() or "relax" in navigation.lower():
            finish = deeprelax()
            if finish == "finish":
                noreply = False
        elif navigation == "4" or "focus" in navigation.lower():
            finish = focus()
            if finish == "finish":
                noreply = False
        elif navigation == "5" or "happiness" in navigation.lower() or "boost" in navigation.lower():
            finish = happinessboost()
            if finish == "finish":
                noreply = False
        else:
            message = "Sorry, I didn't catch that. Try again?"
            print(message)
            speak_text(message)


if __name__ == "__main__":
    numbergoup = 0
    navigate()
    message = "Goodbye!"
    print(message)
    speak_text(message)
    p.terminate()
