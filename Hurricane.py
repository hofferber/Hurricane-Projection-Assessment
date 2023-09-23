import re

class Hurricane:
    risk = 0.0
    windspeed = 0
    recordedPos = []
    projectedPos = []

    def filesIN(_risk):
        for i in range(10): ##CHANGE NUMBER
            file = "rec."
            file[3] = i
            f = open(file + ".kml", 'r')
            for k in range(242):## CHANGE NUMBER
                text = f.readline()
                if k == 241: ## CHANGE NUMBER
                    ##REGEX
                    Hurricane.recordedPos.append(re.findall(">.{12}", text)[0][3:])
                    Hurricane.projectedPos.append(re.findall(".{13}<",text)[0][:10])
                    break
