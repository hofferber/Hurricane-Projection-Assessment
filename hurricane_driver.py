from Hurricane import Hurricane
from kml_export import kmlexport


def main():
    hurricaneList = []
    
    Calvin = Hurricane
    Don = Hurricane
    Dora = Hurricane
    Franklin = Hurricane 
    Lee = Hurricane
    Margot = Hurricane
    hurricaneList = [Calvin, Don, Dora, Franklin, Lee, Margot]
    for i in hurricaneList:
        i.dataPointExtraction(str(i))
        i.distanceInaccuracy()
        kmlexport(i.recordedPos, i.projectedPos, i, "Dora")

    return None