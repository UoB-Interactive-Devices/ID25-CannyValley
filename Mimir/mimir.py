import random, time
user_mood = 0
user_goal = 0
import defaultaiChoices, usermoodTracking
#zero-shot model

def playmusic(number):
    print("playing music")

def dosensors():
    x=0
    return x

def lightsUp():
    print("lights going up")
    pass
def lightsDown():
    print("lights going down")
    pass

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
        #do something else to bridge to next option
    elif input == "no" | input == "n" | input == "nah":
        print ("OK, we'll do something else.")
    else:
        print ("I didn't quite get that. Try again?")
        deepBreaths()

hypeenvironments = [[["Club"],["popping"],["lights","DJ"],["goes hard"]]]

calmenvironments = [[["Rainforest"], ["lush", "verdant", "vibrant", "glimmering"], ["river", "trees", "canopy", "forest floor", "sun"], ["flickers", "emanates", "shines", "flows"]]]
sentences = [["the","2","is","1"],["Watch as the","2","3","across the","0"], ["Imagine the","1","2","as it","3"]]

def factoryReset():
    defaultaiChoices.writeDefault()

def describeEnvironment(number):
    if(number>0):
        theinput = input("I'm going to create a space for you to get into it now, if that's alright? ") #this is waffle but its 1am and im tired
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
    elif(number<=0):
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

myaffirmations = [[[1,3],"Today is my day!"], [[-2,1], "I am enough"], [[-3,2], "I am loved"], [[-3,1], "Through positive thought, I transform obstacles into stepping stones"], [[3,3], "Let's Go!"]]

def findanaffirmation(number):
    randomaff = random.randint(0,len(myaffirmations)-1)
    number1 = myaffirmations[randomaff][0][0]
    number2 = myaffirmations[randomaff][0][1]
    if number1<=number<=number2:
        return (myaffirmations[randomaff][1])
    else:
        labouredaff=findanaffirmation(number)
        return labouredaff

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

def highhrquestions():
    q1R=0
    while q1R==0:
        q1 = input("Does your energy feel focused or scattered? ")
        if(q1 == "Focused" or q1 == "focused"):
            q1R=1
        elif (q1 == "Scattered" or q1 == "scattered"):
            q1R=2
        else:
            print("can we try that again? I didn't quite catch that.")
    q2R = 0
    while q2R==0:
        q2 = input("Is your energy driven by excitement or purpose? ")
        if(q2 == "Excitement" or q2 == "excitement"):
            q2R=1
        elif (q2 == "Purpose" or q2 == "purpose"):
            q2R=2
        else:
            print("can we try that again? I didn't quite catch that.")
    if q1R==1 and q2R==1:
        q3R = 0
        while q3R==0:
            q3 = input("Is your focus fueled by a sense of urgency or long-term ambition? ")
            if(q3 == "Urgency" or q3 == "urgency"):
                return(2)
            elif (q3 == "Ambition" or q3 == "ambition" or q3 == "Long-Term Ambition" or q3 == "long-term ambition"):
                return(1)
            else:
                print("can we try that again? I didn't quite catch that.")
    elif q1R==1 and q2R==2:
        q3R = 0
        while q3R==0:
            q3 = input("Are you actively working toward something or just feeling positive? ")
            if(q3 == "Working" or q3 == "working" or q3 == "Working Towards Something" or q3 == "working towards something"):
                return(2)
            elif (q3 == "Feeling Positive" or q3 == "feeling positive"):
                return(0)
            else:
                print("can we try that again? I didn't quite catch that.")
    elif q1R==2 and q2R==1:
        q3R = 0
        while q3R==0:
            q3 = input("Is your excitement more about movement or about looking forward to something? ")
            if(q3 == "looking forward" or q3 == "Looking Forward" or q3 == "Looking Forward To Something" or q3 == "looking forward to something"):
                return(1)
            elif (q3 == "Movement" or q3 == "movement"):
                return(3)
            else:
                print("can we try that again? I didn't quite catch that.")
    elif q1R==2 and q2R==2:
        q3R = 0
        while q3R==0:
            q3 = input("Is your energy making it hard to stay still or just making you feel the same?")
            if(q3 == "hard to stay still" or q3 == "Hard to Stay Still"):
                return(3)
            elif (q3 == "Feel the Same" or q3 == "feel the same"):
                return(0)
            else:
                print("can we try that again? I didn't quite catch that.")

def lowhrquestions():
    q1R=0
    while q1R==0:
        q1 = input("Do you feel more calm or tired? ")
        if(q1 == "Calm" or q1 == "calm"):
            q1R=1
        elif (q1 == "Tired" or q1 == "tired"):
            q1R=2
        else:
            print("can we try that again? I didn't quite catch that.")
    q2R = 0
    while q2R==0:
        q2 = input("Do you think you have a normal amount of energy, or lower than normal? ")
        if(q2 == "Normal" or q2 == "normal"):
            q2R=1
        elif (q2 == "Lower" or q2 == "lower" or q2 == "Lower than Normal" or q2 == "lower than normal"):
            q2R=2
        else:
            print("can we try that again? I didn't quite catch that.")
    if q1R==1 and q2R==1:
        q3R = 0
        while q3R==0:
            q3 = input("Do you feel satisfied or there could be small improvements? ")
            if(q3 == "Satisfied" or q3 == "satisfied"):
                return(-1)
            elif (q3 == "Small Improvements" or q3 == "small improvements"):
                return(0)
            else:
                print("can we try that again? I didn't quite catch that.")
    elif q1R==1 and q2R==2:
        q3R = 0
        while q3R==0:
            q3 = input("Do you feel a quiet sense of happiness or more at ease? ")
            if(q3 == "Happiness" or q3 == "happiness" ):
                return(-1)
            elif (q3 == "At Ease" or q3 == "at ease"):
                return(-2)
            else:
                print("can we try that again? I didn't quite catch that.")
    elif q1R==2 and q2R==1:
        q3R = 0
        while q3R==0:
            q3 = input("Do you feel drained or could you carry on with your current activity? ")
            if(q3 == "Drained" or q3 == "drained"):
                return(-3)
            elif (q3 == "I can carry on" or q3 == "Carry On" or q3 == "carry on"):
                return(0)
            else:
                print("can we try that again? I didn't quite catch that.")
    elif q1R==2 and q2R==2:
        q3R = 0
        while q3R==0:
            q3 = input("Do you feel like not doing any activity or simply being present in the moment?")
            if(q3 == "Not doing any activity" or q3 == "Not Doing any Activity"):
                return(-3)
            elif (q3 == "Just Being Present" or q3 == "just being present"):
                return(-1)
            else:
                print("can we try that again? I didn't quite catch that.")

def rmm ():
    heartrate=dosensors()
    if(heartrate>50):
        userfeeling=highhrquestions()
    elif(heartrate<=50):
        userfeeling=lowhrquestions()
    user_mood = round((0.6*float(userfeeling))+(0.4*(heartrate)))
    usergoal = input ("how do you want to be feeling on a scale from -3 to 3 ")
    usergoal = int(usergoal)
    return user_mood, usergoal


def cmm(currentmood, goalmood):
    aiChoices = defaultaiChoices.defaultaiChoices
    if(currentmood<goalmood):
        lightsUp()
        aiChoices = defaultaiChoices.choicesRead()
        mylist = defaultaiChoices.populateChoices(goalmood)
        aiChoices = aiChoices+mylist
        
    elif currentmood < goalmood:
        lightsDown()
        aiChoices = defaultaiChoices.choicesRead()
        mylist = defaultaiChoices.populateChoices(goalmood)
        aiChoices = aiChoices+mylist
    
    elif currentmood == goalmood:
        aiChoices = defaultaiChoices.choicesRead()
        mylist = defaultaiChoices.populateChoices(goalmood)
        aiChoices = aiChoices+mylist
        

    aiDecision = random.choice(aiChoices)
    if(aiDecision == 1):
        playmusic(goalmood)
    elif aiDecision == 2:
        deepBreaths()
    elif aiDecision == 3:
        describeEnvironment(goalmood)
    elif aiDecision == 4:
        positiveAffirmations(goalmood)

def takeUserFeedback():
    feedback=input ("give me input > ")
    #sentiment analyse feedback somehow
    if feedback == "more music":
        defaultaiChoices.choicesAdd([1])
    elif feedback == "less music":
        defaultaiChoices.choicesRemove([1])
    elif feedback == "more breaths" or feedback == "more breathing":
        defaultaiChoices.choicesAdd([2])
    elif feedback == "less breaths" or feedback == "less breathing":
        defaultaiChoices.choicesRemove([2])
    elif feedback == "more description" or feedback == "more describing":
        defaultaiChoices.choicesAdd([3])
    elif feedback == "less description" or feedback == "less describing":
        defaultaiChoices.choicesRemove([3])
    elif feedback == "more affirmations" or feedback == "more affirming":
        defaultaiChoices.choicesAdd([4])
    elif feedback == "less affirmations" or feedback == "less affirming":
        defaultaiChoices.choicesRemove([4])

#long-term emotional tracking?
#factoryReset()
user_mood, user_goal=rmm()
numbergoup=0
while True:
    cmm(user_mood, user_goal)
    numbergoup+=1
    if numbergoup %3 == 0:
        endinput = input("do you feel like you have met your goal? ")
        if endinput == "yes" or endinput == "yeah" or endinput == "y":
            anyfeedback = input("do you have any feedback? ")
            if anyfeedback == "yes" or anyfeedback == "yeah" or anyfeedback == "y":
                    takeUserFeedback()
            print("goodbye")
            break
        else:   
            anyfeedback = input("do you have any feedback while we're still going? ")
            if anyfeedback == "yes" or anyfeedback == "yeah" or anyfeedback == "y":
                    takeUserFeedback()      
    
