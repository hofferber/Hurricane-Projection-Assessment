import re
import math
import os

class Hurricane:
    recordedPos = []
    projectedPos = []
    distList = []
    h = 0
    def dataPointExtraction(nameOfHurricane):
        path = os.path.expanduser("HurricaneKMLfiles/Hurricane_" + nameOfHurricane)
        files = os.listdir(path)
        h = 0
        for f in files:
            Hurricane.h+=1
        for i in range(1,Hurricane.h*2,2):
            openfile = open(path + "/adv" + str(i) + ".kml", "r")
            k = 0
            for line in openfile:
                k += 1
                if k == 242:
                    Hurricane.recordedPos.append(re.findall(">[ |-]{2,3}\d{2,3}\.\d,-?\d{2,3}\.\d", line)[0][3:])
                    Hurricane.projectedPos.append(re.findall("-\d{2,3}\.\d,-?\d{2,3}\.\d,0 <", line)[0][:-4])
                    continue

    def distanceInaccuracy():
        def degtorad(deg):
            return deg * (math.pi / 180)

        distances = 0
        k = 0
        R = 6371 ##Km
        for i in range(Hurricane.h-10):
            lat1, long1 = float(Hurricane.recordedPos[i+10].split(',')[1]), float(Hurricane.recordedPos[i+10].split(',')[0])
            lat2, long2 = float(Hurricane.projectedPos[i].split(',')[1]), float(Hurricane.projectedPos[i].split(',')[0])
            changeLat = degtorad(lat1 - lat2)
            changeLong = degtorad(long1 - long2)
            a = math.pow(math.sin(changeLat/2), 2) + math.cos(degtorad(lat1)) * math.cos(degtorad(lat2)) * math.pow(math.sin(changeLong/2), 2)
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
            d = R * c
            k = k + 1
            Hurricane.distList.append(d)
            distances = distances + d
        averageDist = distances / k
        return averageDist ##Km
