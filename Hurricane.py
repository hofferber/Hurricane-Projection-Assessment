import re

class Hurricane:
    recordedPos = []
    projectedPos = []

    def dataPointExtraction():
        for i in range(1,50,2):  ##CHANGE NUMBER
            file = "adv" + str(i)
            f = open("HurricaneKMLfiles/" + file + ".kml", 'r')
            for k in range(242):  ## CHANGE NUMBER
                text = f.readline()
                if k == 241:  ## CHANGE NUMBER
                    ##REGEX
                    Hurricane.recordedPos.append(re.findall(">.{12}", text)[0][3:])
                    Hurricane.projectedPos.append(re.findall(".{13}<", text)[0][:10])
                    break

    def distanceInaccuracy():
        def degtorad(deg):
            return deg * (math.pi / 180)

        distances = 0
        k = 0
        R = 6371 ##Km
        for i in range(Hurricane.x-10):
            lat1, long1 = float(Hurricane.recordedPos[i+10].split(',')[1]), float(Hurricane.recordedPos[i+10].split(',')[0])
            lat2, long2 = float(Hurricane.projectedPos[i].split(',')[1]), float(Hurricane.projectedPos[i].split(',')[0])
            changeLat = degtorad(lat1 - lat2)
            changeLong = degtorad(long1 - long2)
            a = math.pow(math.sin(changeLat/2), 2) + math.cos(degtorad(lat1)) * math.cos(degtorad(lat2)) * math.pow(math.sin(changeLong/2), 2)
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
            d = R * c
            k = k + 1
            distances = distances + d
        averageDist = distances / k
        return averageDist ##Km
