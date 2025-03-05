import random, time, pyttsx3, spotipy

# import speech_recognition as s_r
# import SpeechRecognition as sr
# user_mood = 0
# user_goal = 0
# #these aren't used right now 
import defaultaiChoices
#zero-shot model
# recog = sr.Recognizer() 

# def speakText(command):
#     engine=pyttsx3.init('nsss', True)
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice', voices[0].id)
#     engine.say(command)
#     engine.runAndWait()

def playmusic(number):
    print("playing music")

def dosensors():
    x=0
    return x

def lightsUp():
    print("lights going up")
def lightsDown():
    print("lights going down")

def deepBreaths():
    input("We're going to take some deep breaths now, if thats alright?") 
    if input == "yes" | input == "yeah" | input == "y":
        for i in range (3):
            time.sleep(1)
            print("Breathe in")
            time.sleep(1)
            print("Hold it")
            time.sleep(1)
            print("And breathe out")
    elif input == "no" | input == "n" | input == "nah":
        print ("OK, we'll do something else.")
    else:
        print ("I didn't quite get that. Try again?")
        deepBreaths()

hypeenvironments = [[["Club"],["popping"],["lights","DJ"],["goes hard"]]]

calmenvironments = [[["Rainforest"], ["lush", "verdant", "vibrant", "glimmering"], ["river", "trees", "canopy", "forest floor", "sun"], ["flickers", "emanates", "shines", "flows"]]]
sentences = [["the","2","is","1"],["Watch as the","2","3","across the","0"], ["Imagine the","1","2","as it","3"]]
#these should be better but i can't be arsed rn

def factoryReset():
    defaultaiChoices.writeDefault()

def describeEnvironment(number):
    if(number==0 or number==3):
        theinput = input("I'm going to create a space for you to get into it now, if that's alright? ")
        if theinput == "yes" or theinput == "yeah" or theinput == "y" or theinput == "OK":
            thisenv = random.randint(0,2)
            thisenv=0
            placename = str(hypeenvironments[thisenv][0])
            print("Welcome to the",placename)
            time.sleep(1)
            thesetimes = random.randint(4,6)
            for i in range(thesetimes):
                whichsentence = random.randint(0,2)
                for fragment in sentences[whichsentence]:
                    if(fragment[0:].isdigit()):
                        value = int(fragment)
                        whichone = random.randint(0,len(hypeenvironments[thisenv][value])-1)
                        print(hypeenvironments[thisenv][value][whichone], end=" ")
                    else:
                        print (fragment, end = " ")
                print("\n")
                time.sleep(1)

        elif theinput == "no" or theinput == "n" or theinput == "nah":
            print ("OK, we'll do something else.")
        else:
            print ("I didn't quite get that. Try again?")
            describeEnvironment(number)
    elif(number==1 or number==2):
        theinput=input ("I'm going to create a space for you to reflect now, if that's alright? ")
        if theinput == "yes" or theinput == "yeah" or theinput == "y" or theinput == "OK":
            thisenv = random.randint(0,2)
            thisenv=0
            placename = str(calmenvironments[thisenv][0])
            print("Welcome to the "+placename)
            time.sleep(1)
            thesetimes = random.randint(4,6)
            for i in range(thesetimes):
                whichsentence = random.randint(0,2)
                for fragment in sentences[whichsentence]:
                    if(fragment[0:].isdigit()):
                        value = int(fragment)
                        whichone = random.randint(0,len(calmenvironments[thisenv][value])-1)
                        print(calmenvironments[thisenv][value][whichone], end=" ")
                    else:
                        print (fragment, end = " ")
                print("\n")
                time.sleep(1)
        elif theinput == "no" | theinput == "n" | theinput == "nah":
            print ("OK, we'll do something else.")
        else:
            print ("I didn't quite get that. Try again? ")
            describeEnvironment(number)

myaffirmations = [[[0,3],"Today is my day!"], [[2,1], "I am enough"], [[1,2], "I am loved"], [[2,1], "Through positive thought, I transform obstacles into stepping stones"], [[0,3], "Let's Go!"]]

def findanaffirmation(number):
    randomaff = random.randint(0,len(myaffirmations)-1)
    number1 = myaffirmations[randomaff][0][0]
    number2 = myaffirmations[randomaff][0][1]
    if number==number2 or number==number2:
        return (myaffirmations[randomaff][1])
    else:
        foundaff=findanaffirmation(number)
        return foundaff

def saytheaffirmation(theaff, times):
    if times<3:
        theirinput = input(str(theaff)+" ")
        if(theirinput == theaff):
            time.sleep(1)
            saytheaffirmation(theaff,times+1)
        else:
            print("Give it another try!")
            time.sleep(1)
            saytheaffirmation(theaff,times)
    else:
        return()
    

def positiveAffirmations(number):
    if(number==3):
        theinput=input ("Let's get hyped! You good to chant back to me? ") 
        if theinput == "yes" or theinput == "yeah" or theinput == "y" or theinput == "OK":
            thisaff = findanaffirmation(number)
            saytheaffirmation(thisaff, 0)
        
        elif theinput == "no" or theinput == "n" or theinput == "nah":
            print ("OK, we'll do something else.")
        else:
            print ("I didn't quite get that. Try again? ")
            positiveAffirmations(number)
    elif(number==2):
        theinput=input ("Let's get into it, time to shout back after me ")
        if theinput == "yes" or theinput == "yeah" or theinput == "y" or theinput == "OK":
            thisaff = findanaffirmation(number)
            saytheaffirmation(thisaff, 0)
        
        elif theinput == "no" or theinput == "n" or theinput == "nah":
            print ("OK, we'll do something else.")
        else:
            print ("I didn't quite get that. Try again? ")
            positiveAffirmations(number)
    elif(number<=1):
        theinput=input ("Alright, let's repeat after me ")
        if theinput == "yes" or theinput == "yeah" or theinput == "y" or theinput == "OK":
            thisaff = findanaffirmation(number)
            saytheaffirmation(thisaff, 0)
        
        elif theinput == "no" or theinput == "n" or theinput == "nah":
            print ("OK, we'll do something else.")
        else:
            print ("I didn't quite get that. Try again? ")
            positiveAffirmations(number)

def physicalquestions(hr, posneg):
    q1R=0
    q2R=0
    value=0
    if(hr=="high" and posneg==1):
        value=0
    elif(hr=="normal" and posneg==1):
        value=1
    elif(hr=="low" and posneg==1):
        value=2
    elif(hr=="high" and posneg==0):
        value=3
    elif(hr=="normal" and posneg==0):
        value=4
    elif(hr=="low" and posneg==0):
        value=5
    indexlist=[0,1,2,3,4,5]
    questionsasked=random.randint(2,4)
    for i in range(questionsasked):
        index = random.randint(0,len(questionbank[value]))
        indexlist.remove(index)
        q1 = input(questionbank[value][index])
        time.sleep(3)
    #run the questions for user to think through their mood
        

questionbank=[["Does this energy feel directed toward something, or is it more free and spontaneous?","Would you describe this feeling as an intense push forward or a steady momentum?","Do you feel more in control of this energy, or is it carrying you along?","If this feeling had a sound, would it be loud and fast or rhythmic and steady?","Does this energy make you want to take action, or simply enjoy the feeling?","Would you say this energy is building up, staying consistent, or already peaking?"],["Does this feel like an ordinary state for you, or is today a little different?","Are you feeling naturally balanced, or did something shift your mood in a good way?","Does this feel like a moment of quiet focus or a sense of lightness?","Are you drawn toward something specific, or are you simply going with the flow?","If this feeling had a pace, would it be slow and steady or gently moving forward?","Is this the kind of feeling you’d like to hold onto for a while?"],["Does this feel like a moment of stillness or a familiar sense of calm?","Are you simply resting, or does this feel like a deeper kind of ease?","Does this moment feel like something you intentionally created or something that just happened?","Are your thoughts clear, or are they drifting freely?","Do you feel present in this moment, or is your mind wandering elsewhere?","If this feeling were a color, would it be soft and muted or warm and rich?"],["Does this energy feel useful, or does it feel like it’s pulling in too many directions?","Is your mind jumping between thoughts, or is it locked onto one thing?","Does this feeling make you want to move, or does it feel like too much all at once?","Would you describe this energy as something building up or something already at its peak?","If this feeling had motion, would it be fast and scattered or sharp and intense?","Do you feel like this state is leading somewhere, or does it feel like it’s circling back on itself?"],["Would you describe this mood as something vague or something clear but hard to define?","Does this feel like a pause in momentum or a general sense of uncertainty?","Would you say this moment is still or slightly off balance?","Do your thoughts feel structured, or are they moving in many directions?","If this feeling were a space, would it be open and empty or closed and uncertain?","Does this state feel neutral, or is there something beneath it waiting to surface?"],["Does this feel more like a lack of energy or a weight that’s hard to shake?","Is this a passing feeling, or has it been lingering for a while?","Would you describe this state as quiet and empty or full and heavy?","If this feeling had a texture, would it be soft and slow or dense and unmoving?","Do your thoughts feel distant, or are they looping in the background?","Would you say this moment needs stillness or a small shift?"]]

def rmm ():
    heartrate=dosensors()
    if(heartrate>50):
        userfeeling="high"
    elif(heartrate<=20):
        userfeeling="normal"
    else:
        userfeeling="low"
    qR=0
    while qR==0:
        q = input("Would you say you're feeling more positive or negative right now? ")
        if(q == "Positive" or q == "positive"):
            qR=1
        elif(q == "Negative" or q == "negative"):
            qR=0
        else:
            print("can we try that again? I didn't quite catch that.")  
    physicalquestions(userfeeling,qR)
    #user_mood = round((0.6*float(userfeeling))+(0.4*(heartrate)))
    #usergoal = input ("how do you want to be feeling on a scale from -3 to 3 ")
    #usergoal = int(usergoal)

def drinkWater():
    drinkcheck = input("Have you drunk water in the past hour? ")
    if(drinkcheck == "yes" or drinkcheck == "y" or drinkcheck=="Yes"):
        print("Good! Keep it up.")
    else:
        print("Make sure to drink some water pretty soon, it helps you calm down. ")
        time.sleep(3)
        watercheck=input("Have you had a drink yet? ")
        if(watercheck == "yes" or watercheck == "y" or watercheck=="Yes"):
            return()
        else:
            drinkWater()

def guideStretch():
    print("do some stretches idk")
    #fill this out


def guideMeditation():
    print("honk shoo")
    #fill this out

def playGame(number):
    if(number==0):
        pass #do calm game
    elif (number==1):
        pass #do focus game

def setGoal():
    goaltoset = input("Let's set a goal! What can you get done in the next 5 minutes? ")
    print("Sounds good! I'll see you then!")
    time.sleep(300) #arbitrary number
    complete=input("did you get it done? ")
    if(complete == "yes" or complete == "y" or complete=="Yes"):
        print("Amazing. Super productive.")
    else:
        print("Unfortunate, but you'll get there next time!")

def listGratitude():
    thing1 = input("OK, now it's time to talk gratitude. What's something you're grateful for today? ")
    time.sleep(1)
    thing2 = input("And something else? ")
    time.sleep(1)
    thing3 = input("Anything more? ")
    time.sleep(1)
    print("That sounds great! ")

def cmm(aiChoices, goalmood):
    aiDecision = random.choice(aiChoices)
    if(aiDecision == 1):
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


def takeUserFeedback(currentlist):
    feedback=input ("give me input > ")
    #sentiment analyse feedback somehow?
    if feedback == "more music":
        defaultaiChoices.choicesAdd([1],currentlist)
    elif feedback == "less music":
        defaultaiChoices.choicesRemove([1],currentlist)
    elif feedback == "more breaths" or feedback == "more breathing":
        defaultaiChoices.choicesAdd([2],currentlist)
    elif feedback == "less breaths" or feedback == "less breathing":
        defaultaiChoices.choicesRemove([2],currentlist)
    elif feedback == "more description" or feedback == "more describing":
        defaultaiChoices.choicesAdd([3],currentlist)
    elif feedback == "less description" or feedback == "less describing":
        defaultaiChoices.choicesRemove([3],currentlist)
    elif feedback == "more affirmations" or feedback == "more affirming":
        defaultaiChoices.choicesAdd([4],currentlist)
    elif feedback == "less affirmations" or feedback == "less affirming":
        defaultaiChoices.choicesRemove([4],currentlist)
    elif feedback == "more water" or feedback=="more drinking":
        defaultaiChoices.choicesAdd([5],currentlist)
    elif feedback == "less water" or feedback=="less drinking":
        defaultaiChoices.choicesRemove([5],currentlist)
    elif feedback == "more stretching":
        defaultaiChoices.choicesAdd([6],currentlist)
    elif feedback == "less stretching":
        defaultaiChoices.choicesRemove([6],currentlist)
    elif feedback == "more meditating":
        defaultaiChoices.choicesAdd([7],currentlist)
    elif feedback == "less meditating":
        defaultaiChoices.choicesRemove([7],currentlist)
    elif feedback == "more games":
        defaultaiChoices.choicesAdd([8],currentlist)
    elif feedback == "less games":
        defaultaiChoices.choicesRemove([8],currentlist)
    elif feedback == "more goals":
        defaultaiChoices.choicesAdd([9],currentlist)
    elif feedback == "less goals":
        defaultaiChoices.choicesRemove([9],currentlist)
    elif feedback == "more gratitude":
        defaultaiChoices.choicesAdd([10],currentlist)
    elif feedback == "less gratitude":
        defaultaiChoices.choicesRemove([10],currentlist)
    



def checkFeedback(currentlist):
    numbergoup+=1
    if numbergoup %3 == 0:
        endinput = input("do you want to switch modes or finish? (y/n) ")
        if endinput == "yes" or endinput == "yeah" or endinput == "y":
            anyfeedback = input("do you have any feedback? ")
            if anyfeedback == "yes" or anyfeedback == "yeah" or anyfeedback == "y":
                    takeUserFeedback(currentlist)
            return("break")
            
        else:   
            anyfeedback = input("do you have any feedback while we're still going? ")
            if anyfeedback == "yes" or anyfeedback == "yeah" or anyfeedback == "y":
                    takeUserFeedback(currentlist) 

def energyenhance():
    lightsUp()
    numbergoup=0
    while True:
        aiChoices = defaultaiChoices.choicesRead()
        mylist = defaultaiChoices.populateChoices(0)
        aiChoices = aiChoices+mylist
        cmm(aiChoices)
        numbergoup+=1
        if numbergoup %3 == 0:
            breaking=checkFeedback(0)
            if breaking == "break":
                leave=input("which would you like to do: switch modes or finish? ")
                if leave=="finish" or leave == "Finish":
                    return("finish")
                else: 
                    return("switch")

def deeprelax():
    lightsDown()
    numbergoup=0
    while True:
        aiChoices = defaultaiChoices.choicesRead()
        mylist = defaultaiChoices.populateChoices(1)
        aiChoices = aiChoices+mylist
        cmm(aiChoices)
        numbergoup+=1
        if numbergoup %3 == 0:
            breaking=checkFeedback(0)
            if breaking == "break":
                leave=input("which would you like to do: switch modes or finish? ")
                if leave=="finish" or leave == "Finish":
                    return("finish")
                else: 
                    return("switch")


def focus():
    lightsDown()
    numbergoup=0
    while True:
        aiChoices = defaultaiChoices.choicesRead()
        mylist = defaultaiChoices.populateChoices(2)
        aiChoices = aiChoices+mylist
        cmm(aiChoices)
        numbergoup+=1
        if numbergoup %3 == 0:
            breaking=checkFeedback(0)
            if breaking == "break":
                leave=input("which would you like to do: switch modes or finish? ")
                if leave=="finish" or leave == "Finish":
                    return("finish")
                else: 
                    return("switch")


def happinessboost():
    lightsUp()
    numbergoup=0
    while True:
        aiChoices = defaultaiChoices.choicesRead()
        mylist = defaultaiChoices.populateChoices(3)
        aiChoices = aiChoices+mylist
        cmm(aiChoices)
        numbergoup+=1
        if numbergoup %3 == 0:
            breaking=checkFeedback(0)
            if breaking == "break":
                leave=input("which would you like to do: switch modes or finish? ")
                if leave=="finish" or leave == "Finish":
                    return("finish")
                else: 
                    return("switch")

        
def navigate():
    noreply=True
    while noreply:
        navigation=input('''Hello, this is Mimir.
              Would you like to:
              1. Find Your Mood
              2. Energy Enhance
              3. Deep Relaxation
              4. Focus 
              5. Happiness Boost
              ''')
        if(navigation==1):
            rmm()
            noreply=False
        elif(navigation==2):
            finish=energyenhance()
            if(finish=="finish"):
                noreply=False
        elif(navigation==3):
            finish=deeprelax()
            if(finish=="finish"):
                noreply=False
        elif(navigation==4):
            finish=focus()
            if(finish=="finish"):
                noreply=False
        elif(navigation==5):
            finish=happinessboost()
            if(finish=="finish"):
                noreply=False
        else:
            print("Sorry, I didn't catch that. Try again? ")


#long-term emotional tracking?
#factoryReset()
#user_mood, user_goal=rmm()
numbergoup=0
navigate()
print("goodbye! ")   
    
