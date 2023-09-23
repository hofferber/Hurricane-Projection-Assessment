import re

class Hurricane:
    recordedPos = []
    projectedPos = []

    def dataPointExtraction():
        for i in range(3):  ##CHANGE NUMBER
            file = "rec" + str(i)
            f = open("HurricaneKMLfiles/" + file + ".kml", 'r')
            for k in range(242):  ## CHANGE NUMBER
                text = f.readline()
                if k == 241:  ## CHANGE NUMBER
                    ##REGEX
                    Hurricane.recordedPos.append(re.findall(">.{12}", text)[0][3:])
                    Hurricane.projectedPos.append(re.findall(".{13}<", text)[0][:10])
                    break
