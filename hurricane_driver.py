from Hurricane import Hurricane
from kml_export import kmlexport


def main():
    hurricaneList = []
    # Replace with reading folder names in HurricaneKMLfiles folder
    nameList = ["Calvin",  "Don"]
    # h = 0
    # for i in nameList:
    #     i = Hurricane
    #     hurricaneList[h] = i
    #     h += 1

    Calvin = Hurricane

    Calvin.dataPointExtraction()
    kmlexport(Calvin.projectedPos, Calvin.recordedPos, nameList[0])
    