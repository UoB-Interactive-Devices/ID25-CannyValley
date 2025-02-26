import random, time
user_mood = 0
user_goal = 0
import defaultaiChoices, usermoodTracking
#zero-shot model

def playmusic(number):
    print("playing music")

def dosensors():
    x=0
    y=0
    z=0
    return x,y,z

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
            print("Welcome to the "+str(hypeenvironments[thisenv][0]))
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
            print("Welcome to the "+str(calmenvironments[thisenv][0]))
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
    print(randomaff)
    number1 = myaffirmations[randomaff][0][0]
    number2 = myaffirmations[randomaff][0][1]
    print(myaffirmations[randomaff][0][0],number, myaffirmations[randomaff][0][1])
    if number1<=number<=number2:
        print("the affirmation in faaf: "+myaffirmations[randomaff][1])
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
        #say some hype shit idk
        elif theinput == "no" or theinput == "n" or theinput == "nah":
            print ("OK, we'll do something else.")
        else:
            print ("I didn't quite get that. Try again? ")
            positiveAffirmations(number)
    elif(number==2):
        theinput=input ("Let's get into it, time to shout back after me ")
        if theinput == "yes" or theinput == "yeah" or theinput == "y" or theinput == "OK":
            thisaff = findanaffirmation(number)
            print("the afirmation: ",thisaff)
            saytheaffirmation(thisaff, 0)
        #say some pretty hype shit
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
        #say some mildly hype shit
        elif theinput == "no" or theinput == "n" or theinput == "nah":
            print ("OK, we'll do something else.")
        else:
            print ("I didn't quite get that. Try again? ")
            positiveAffirmations(number)

def rmm ():
    userfeeling = input ("how are you feeling on a scale from -3 to 3 ")
    x,y,z=dosensors()
    user_mood = round((0.6*float(userfeeling))+(0.4*(x*y*z)))
    usergoal = input ("how do you want to be feeling on a scale from -3 to 3 ")
    usergoal = int(usergoal)
    return user_mood, usergoal



def cmm(currentmood, goalmood):
    aiChoices = defaultaiChoices
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
    
