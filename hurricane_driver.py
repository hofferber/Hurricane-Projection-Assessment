# from Hurricane import Hurricane
# from kml_export import kmlexport


# def main():
    
#     Calvin = Hurricane
#     Calvin.dataPointExtraction("Calvin")
#     Calvin.distanceInaccuracy("Calvin")
#     kmlexport(Calvin.recordedPos, Calvin.projectedPos, Calvin, "Calvin")
#     Don = Hurricane
#     Don.resetClass()
#     Don.dataPointExtraction("Don")
#     Don.distanceInaccuracy("Don")
#     kmlexport(Don.recordedPos, Don.projectedPos, Don, "Don")
#     Dora = Hurricane
#     Dora.resetClass()
#     Dora.dataPointExtraction("Dora")
#     Dora.distanceInaccuracy("Dora")
#     kmlexport(Dora.recordedPos, Dora.projectedPos, Dora, "Dora")
#     Franklin = Hurricane
#     Franklin.resetClass()
#     Franklin.dataPointExtraction("Franklin")
#     Franklin.distanceInaccuracy("Franklin")
#     kmlexport(Franklin.recordedPos, Franklin.projectedPos, Franklin, "Franklin")
#     Lee = Hurricane
#     Lee.resetClass()
#     Lee.dataPointExtraction("Lee")
#     Lee.distanceInaccuracy("Lee")
#     kmlexport(Lee.recordedPos, Lee.projectedPos, Lee, "Lee")
#     Margot = Hurricane
#     Margot.resetClass()
#     Margot.dataPointExtraction("Margot")
#     Margot.distanceInaccuracy("Margot")
#     kmlexport(Margot.recordedPos, Margot.projectedPos, Margot, "Margot")

#     return None

# main()

from Hurricane import Hurricane
from kml_export import kmlexport


Calvin = Hurricane("Calvin")
Calvin.dataPointExtraction()
Calvin.distanceInaccuracy()
kmlexport(Calvin.recordedPos, Calvin.projectedPos, Calvin, "Calvin")

Don = Hurricane("Don")
Don.dataPointExtraction()
Don.distanceInaccuracy()
kmlexport(Don.recordedPos, Don.projectedPos, Don,  "Don")

Dora = Hurricane("Dora")
Dora.dataPointExtraction()
Dora.distanceInaccuracy()
kmlexport(Dora.recordedPos, Dora.projectedPos, Dora, "Dora")

Franklin = Hurricane("Franklin")
Franklin.dataPointExtraction()
Franklin.distanceInaccuracy()
kmlexport(Franklin.recordedPos, Franklin.projectedPos, Franklin, "Franklin")

Lee = Hurricane("Lee")
Lee.dataPointExtraction()
Lee.distanceInaccuracy()
kmlexport(Lee.recordedPos, Lee.projectedPos, Lee, "Lee")

Margot = Hurricane("Margot")
Margot.dataPointExtraction()
Margot.distanceInaccuracy()
kmlexport(Margot.recordedPos, Margot.projectedPos, Margot, "Margot")
