from Hurricane import Hurricane
from kml_export import kmlexport


def main():
    hurricaneList = []
    
    Calvin = Hurricane
    Calvin.dataPointExtraction("Calvin")
    Calvin.distanceInaccuracy()
    kmlexport(Calvin.recordedPos, Calvin.projectedPos, Calvin, "Calvin")
    Don = Hurricane
    Don.dataPointExtraction("Don")
    Don.distanceInaccuracy()
    kmlexport(Don.recordedPos, Don.projectedPos, Don, "Don")
    Dora = Hurricane
    Dora.dataPointExtraction("Dora")
    Dora.distanceInaccuracy()
    kmlexport(Dora.recordedPos, Dora.projectedPos, Dora, "Dora")
    Franklin = Hurricane
    Franklin.dataPointExtraction("Franklin")
    Franklin.distanceInaccuracy()
    kmlexport(Franklin.recordedPos, Franklin.projectedPos, Franklin, "Franklin")
    Lee = Hurricane
    Lee.dataPointExtraction("Lee")
    Lee.distanceInaccuracy()
    kmlexport(Lee.recordedPos, Lee.projectedPos, Lee, "Lee")
    Margot = Hurricane
    Margot.dataPointExtraction("Margot")
    Margot.distanceInaccuracy()
    kmlexport(Margot.recordedPos, Margot.projectedPos, Margot, "Margot")

    return None

main()