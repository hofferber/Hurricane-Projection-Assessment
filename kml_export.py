# Program to export data to KML file for visualization
from Hurricane import Hurricane

def kmlexport(_actualList, _advList, _hurri, _fname):
    actualList = _actualList
    advList = _advList
    fname = _fname
    hurri = _hurri
    display(actualList, advList, hurri, fname + ".kml")
    return None

def description(title, val):
    descriptor = "  <ExtendedData>\n"
    # CHANGE TO LISTS LATER TO SIMPLIFY
    # for i in range(len(title)):
    #     for j in range(len(val)):
    descriptor = descriptor+"       <Data name="+title+">\n"
    descriptor = descriptor+"           <value>"+str(val)+"</value>\n"
    descriptor = descriptor+"       </Data>\n"
    
    descriptor = descriptor+"  </ExtendedData>\n"
    return descriptor
     
def display(actualList, advList, hurri, fname):
    f = open(fname, "x")
    f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
    f.write("<kml xmlns=\"http://www.opengis.net/kml/2.2\">\n    <Document>\n")
    f.write("    <name>"+ fname +"</name>\n\n\n")
    actualPin = ""
    projPin = ""
    actualPin = "<Style id=\"actualPin\"> \n  <IconStyle>\n    <scale>1.5</scale>\n    <Icon>\n   <href>https://maps.google.com/mapfiles/kml/paddle/red-stars.png</href>\n      </Icon>\n          </IconStyle>\n   </Style>\n\n\n"
    projPin = "<Style id=\"projPin\"> \n  <IconStyle>\n    <scale>0.75</scale>\n    <Icon>\n   <href>https://maps.google.com/mapfiles/kml/paddle/pink-blank.png</href>\n      </Icon>\n          </IconStyle>\n   </Style>\n\n\n"
    advLineStyle = "<Style id=\"" + "adv" + "Line\"> \n  <LineStyle>\n    <color>" + "ff0000ff" + "</color>\n         " + "<width>2</width>" + "\n </LineStyle>\n   </Style>\n\n\n"
    actualLineStyle = "<Style id=\"" + "actual" + "Line\"> \n  <LineStyle>\n    <color>" + "ff00ff00" + "</color>\n         " + "<width>3</width>" + "\n </LineStyle>\n   </Style>\n\n\n"
    compLineStyle = "<Style id=\"" + "comp" + "Line\"> \n  <LineStyle>\n    <color>" + "ffffffff" + "</color>\n         " + "<width>2</width> \n         " + "\n </LineStyle>\n   </Style>\n\n\n"
    f.write(actualPin)
    f.write(projPin)
    f.write(advLineStyle)
    f.write(actualLineStyle)
    f.write(compLineStyle)
    
    i = 0



    while i < len(actualList):

           
            f.write("<Placemark>\n         <name> Actual Track "+ str(i) +"</name>\n")
            f.write("      <styleUrl>#actualPin</styleUrl>\n")
            f.write("         <Point>\n")
            f.write("           <coordinates>"+ str(actualList[i])+ ",0</coordinates>\n")
            f.write("         </Point>\n       </Placemark>\n\n")
           
            f.write("<Placemark>\n         <name> 120 Hour Projection from "+ str(i) +"</name>\n")
            f.write("      <styleUrl>#projPin</styleUrl>\n")
            # try:  
            #     f.write(description("Distance to Acutal from Estimate", hurri.distList[i]))
            # except IndexError:
            #      pass
            f.write("         <Point>\n")
            f.write("           <coordinates>"+ str(advList[i])+ ",0</coordinates>\n")
            f.write("         </Point>\n       </Placemark>\n\n")

            if len(actualList) > i + 1:
                f.write("\n<Placemark>\n")
                f.write("      <styleUrl>#actualLine</styleUrl>\n")
                f.write("      <LineString>\n")
                f.write("         <extrude>1</extrude>\n")
                f.write("         <tessellate>1</tessellate>\n")
                f.write("           <coordinates>"+ str(actualList[i])+ ",0  "+ str(actualList[i+1])+ ",0</coordinates>\n")
                f.write("         </LineString>\n       </Placemark>\n\n")

            # f.write("\n<Placemark>\n")
            # f.write("      <styleUrl>advLine#</styleUrl>\n")
            # f.write("      <LineString>\n")
            # f.write("         <extrude>1</extrude>\n")
            # f.write("         <tessellate>1</tessellate>\n")
            # f.write("           <coordinates>"+ str(actualList[i]) + ",0  " + str(advList[i]) + ",0</coordinates>\n")
            # f.write("         </LineString>\n       </Placemark>\n\n")
            
            if len(actualList) > i+11:
                f.write("\n<Placemark>\n")
                f.write("      <styleUrl>#compLine</styleUrl>\n")
                f.write("      <LineString>\n")
                f.write("         <extrude>1</extrude>\n")
                f.write("         <tessellate>1</tessellate>\n")
                f.write("           <coordinates>"+ str(actualList[i+10]) + ",0  "+ str(advList[i])+ ",0</coordinates>\n")
                f.write("         </LineString>\n       </Placemark>\n\n")
            
            i += 1
    
    f.write("\n\n    </Document>\n</kml>")
    return None

# Dora = Hurricane 
# Dora.dataPointExtraction("Dora")
# print(Dora.recordedPos, Dora.projectedPos)
# kmlexport(Dora.recordedPos, Dora.projectedPos, Dora, "Dora")