import csv
import os
import random
import math
import ast
import tkinter as tk

roomListNames = []
participantsList = []

class Participant(object):
    
    def __init__(self, name='', index = -1, metCount = {}):
        super().__init__()
        self.name = name
        self.metCount = metCount
        self.index = index
    def getParticipant(self):
        return self

def parseCSV(participants):
    with open('test.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        count = 0
        for row in reader:
            # print(', '.join(row))
            participants.append(Participant(row, count))
            count += 1
    return participants

def buildArray(participants):
    for i in range(0, len(participants)):
        for j in range(0, len(participants)):
            if(i == j):
                continue
            else:
                participants[i].metCount[participants[j]] = 0 
    return participants

# pick a random participant that hasn't been selected and pick
# a random participant that they've met the least times
def roomMakingUnique(participants, roomSize):
    rooms = int( math.ceil( len(participants) / roomSize ) )
    participantsList = participants
    roomOfRooms = []
    for i in range(0, roomSize +1):
        avenger = random.randint(0, len(participants)-1)
        assemble = participants[avenger]
        metNum = []
        dict(sorted(assemble.metCount.items(), key=lambda item: item[1]))
        count = 0
        level = 0
        metNum.append(assemble)
        for key, value in assemble.metCount.items():
            count += 1
            if(count > roomSize * 2):
                break
            metNum.append(key)       
            # if(count == 1):
            #     level = value
            # if(value == level):
            #     metNum.append(key)
            # elif(value > level):
            #     metNum.append   
        roomList = []
        capacity = 0
        while(capacity < roomSize and len(participants) > 0):
            chosen = random.randint(0, len(metNum)-1)
            roomList.append(metNum[chosen].name)
            capacity += 1
        roomOfRooms.append(roomList)
        for i in range(0, len(metNum)):
            if(metNum[i] in participants):
                participants.remove(metNum[i])
            for j in range(0, len(metNum)):
                if(i == j):
                    continue
                value = metNum[i].metCount.get(metNum[j])
                metNum[i].metCount[metNum[j]] = value + 1

    return roomOfRooms

def outputRoomList(roomList, file):
    with open(file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter = ' ', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
        count = 0
        writer.writerows(roomList)
        print(file)

    replaceAll = open(file, 'r')
    replaceAll = '\n'.join([i for i in replaceAll]).replace('[\'','').replace('\']', '').replace(' ', ', ')
    change = open(file, 'w')
    change.writelines(replaceAll)
    change.close()

    return 'success' if count > 1 else 'failure'
def saveData():
    with open('database.txt', 'w') as file:
        file.write(str(participantsList))
def retrieveData():
    with open('database.txt') as file:
      #return ast.literal_eval(file.read())
      print(file.read())
    return 'lol'
def main():
    print("")
    student = Participant()
    participants = []
    
    res = parseCSV(participants)
    res2 = buildArray(res)
    roomList = roomMakingUnique(res2, 6)
    outputRoomList(roomList,'outputoo.csv')
    saveData()

main()    