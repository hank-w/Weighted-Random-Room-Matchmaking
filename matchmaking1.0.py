import csv
import os
import random
import math
import tkinter as tk

roomListNames = []
participantsList = []

class Participant(object):
    
    def __init__(self, name='', index = -1, metCount = []):
        super().__init__()
        self.name = name
        self.metCount = metCount
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
                participants[i].metCount.append(j)
    return participants

def roomMaking(participants, roomSize):
    rooms = int( math.ceil( len(participants) / roomSize ) )
    print(rooms)
    roomList = []
    for i in range(0, rooms +1):
        capacity = 0
        roomList.append([])
        roomListNames.append([])
        while(capacity < roomSize and len(participants) > 0):
            select = random.randint(0, len(participants)-1)
            roomList[i].append(participants[select])
            roomListNames[i].append(participants[select].name)
            participants.pop(select)
            capacity += 1

    return roomList

def outputRoomList(roomList, file):
    with open(file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter = ' ', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
        count = 0
        # roomListNames =( (o.name for o in roomList) ) 
        # writer.writerows(roomListNames)
        # count = 1
        # roomListNames1 = []
        # for i in range(0,len(roomListNames)):
        #     roomListNames1.append([])
        #     for j in range(0, len(roomListNames[i])):
        #         roomListNames1[i].append(roomListNames[i][j])

        writer.writerows(roomListNames)

    replaceAll = open('output.csv', 'r')
    replaceAll = '\n'.join([i for i in replaceAll]).replace('[\'','').replace('\']', '').replace(' ', ', ')
    change = open('output.csv', 'w')
    change.writelines(replaceAll)
    change.close()

        # for i in roomListNames:
        #     writer.writerow([i])
        #     count += 1
    return 'success' if count > 1 else 'failure'

def main():
    print("")
    student = Participant()
    participants = []
    res = parseCSV(participants)
    res2 = buildArray(res)
    roomList = roomMaking(res2, 6)
    outputRoomList(roomList,'output.csv')

main()    