import csv, random, time
defaultaiChoices = [1,2,3,4]
#do this on csv?
#should have functions to add/remove/alter defaultaiChoices on the csv file

csv_file_path = 'userMood.csv'

def moodAdd(listToAdd):
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file, escapechar='\\')
        data_list = []
        for row in csv_reader:
            data_list=(row)
    data_list = [int(x) for x in data_list]
    data_list=data_list+listToAdd
    with open(csv_file_path, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(data_list)

def moodRemove(listToRemove):
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        data_list = []
        for row in csv_reader:
            data_list=(row)
    data_list = [int(x) for x in data_list]
    for i in range(len(listToRemove)):
        data_list.remove(listToRemove[i])
    with open(csv_file_path, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(data_list)

def moodRead():
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        data_list = []
        for row in csv_reader:
            data_list=(row)
    return data_list
#this is more complicated than i gave it credit for, mostly re: the actual use case of the thing -- will need to look more in-depth
#into temporal tracking etc i think

def writeDefault():
    defaultMood = []
    with open(csv_file_path, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(defaultMood)
            
    #then overwrite that to the csv file

#this is arbitrary i just made it up for a thing
def populateChoices(number):
    if(number<0):
        return [1,2,2,3,3,4]
    elif number==0:
        return [1,2,3,4]
    elif number>0:
        return [1,3,3,4,4]