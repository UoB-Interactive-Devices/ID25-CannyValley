import csv, random, time
defaultaiChoices = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
#do this on csv?
#should have functions to add/remove/alter defaultaiChoices on the csv file

#basically do this 4x, one for each cmm mode, with different, saved lists for each 

csv_file_path = 'myChoices.csv'

def choicesAdd(listToAdd,theint):
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file, escapechar='\\')
        data_list = [[],[],[],[]]
        k=0
        for row in csv_reader:
            for m in range(len(row)):
                data_list[k]+=(row[m])
            k+=1
    for i in range(len(data_list)):
        data_list[i] = [[int(x) for x in line.split()] for line in data_list[i]]
    for i in range(len(data_list)):
        for j in range(len(data_list[i])):
            data_list[i][j]=data_list[i][j][0]
    print(data_list)
    data_list[theint]=data_list[theint]+listToAdd
    with open(csv_file_path, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(data_list[0])
        csv_writer.writerow(data_list[1])
        csv_writer.writerow(data_list[2])
        csv_writer.writerow(data_list[3])

def choicesRemove(listToRemove,theint):
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file, escapechar='\\')
        data_list = [[],[],[],[]]
        k=0
        for row in csv_reader:
            for m in range(len(row)):
                data_list[k]+=(row[m])
            k+=1
    for i in range(len(data_list)):
        data_list[i] = [[int(x) for x in line.split()] for line in data_list[i]]
    for i in range(len(data_list)):
        for j in range(len(data_list[i])):
            data_list[i][j]=data_list[i][j][0]
    for i in range(len(listToRemove)):
        data_list[theint].remove(listToRemove[i])
    with open(csv_file_path, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(data_list[0])
        csv_writer.writerow(data_list[1])
        csv_writer.writerow(data_list[2])
        csv_writer.writerow(data_list[3])

def choicesRead():
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        data_list = []
        for row in csv_reader:
            print(row)
            data_list.append(row)
        for i in range(len(data_list)):
            for j in range(len(data_list[i])):
                data_list[i][j]=int(data_list[i][j][0])
    return data_list
#remember that python writer overwrited by default (i think)

def writeDefault():
    defaultaiChoices = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
    with open(csv_file_path, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(defaultaiChoices)
            
    #then overwrite that to the csv file

#this is arbitrary i just made it up for a thing
def populateChoices(number):
    if(number==0):
        return [1,1,11,8]
    elif number==1:
        return [1,2,3,5,6,7]
    elif number==2:
        return [9,1,2,12]
    elif number==3:
        return [1,10,4]
    else:
        return [1,2,3,4]
