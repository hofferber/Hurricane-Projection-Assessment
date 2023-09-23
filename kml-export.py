# Program to export data to KML file for visualization

def kmlexport():
    actualList = []
    advList = []


def display(actualList, advList, fname):
    f = open(fname, "x")
    f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
    f.write("<kml xmlns=\"http://www.opengis.net/kml/2.2\">\n    <Document>\n")
    f.write("    <name>"+ fname +"</name>\n\n\n")
    actualPin = ""
    projPin = ""
    actualPin = "<Style id=\"facilityPins\"> \n  <IconStyle>\n    <scale>1.5</scale>\n    <Icon>\n   <href>http://maps.google.com/mapfiles/kml/paddle/ylw-stars.png</href>\n      </Icon>\n          </IconStyle>\n   </Style>\n\n\n"
    projPin = "<Style id=\"satPins\"> \n  <IconStyle>\n    <scale>0.75</scale>\n    <Icon>\n   <href>http://maps.google.com/mapfiles/kml/paddle/blu-blank.png</href>\n      </Icon>\n          </IconStyle>\n   </Style>\n\n\n"
    advLineStyle = "<Style id=\"" + "adv" + "Line\"> \n  <LineStyle>\n    <color>" + "ff0000ff" + "</color>\n         " + "<width>2</width>" + "\n </LineStyle>\n   </Style>\n\n\n"
    actualLineStyle = "<Style id=\"" + "actual" + "Line\"> \n  <LineStyle>\n    <color>" + "ff00ff00" + "</color>\n         " + "<width>3</width>" + "\n </LineStyle>\n   </Style>\n\n\n"
    f.write(actualPin)
    f.write(projPin)

    while i < len(actualList):
            
            f.write("<Placemark>\n         <name>"+ actualList[i] +" (Facility)</name>\n")
            f.write("      <styleUrl>#facilityPins</styleUrl>\n")
            f.write("         <Point>\n")
            f.write("           <coordinates>"+ str(actualList[facIndex][1]/-100) + "," + str(actualList[facIndex][0]/100)+ ",0</coordinates>\n")
            f.write("         </Point>\n       </Placemark>\n\n")
            f.write(lineStyles[i])
            for n in nearCities:
                satIndex = 0 
                satIndex = cityList.index(n)
                #print("<Placemark>\n         <name>"+ str(cityList[satIndex]) +"</name>\n")
                f.write("<Placemark>\n         <name>"+ str(cityList[satIndex]) +"</name>\n")
                f.write("      <styleUrl>#satPins</styleUrl>\n")
                f.write("         <Point>\n")
                f.write("           <coordinates>"+ str(actualList[satIndex][1]/-100) + "," + str(actualList[satIndex][0]/100)+ ",0</coordinates>\n")
                f.write("         </Point>\n       </Placemark>\n\n")

                f.write("\n<Placemark>\n")
                f.write("      <styleUrl>#"+ facLineStyleName + "Line</styleUrl>\n")
                f.write("      <LineString>\n")
                f.write("         <extrude>1</extrude>\n")
                f.write("         <tessellate>1</tessellate>\n")
                f.write("           <coordinates>"+ str(actualList[satIndex][1]/-100) + "," + str(actualList[satIndex][0]/100)+ ",0  "+ str(actualList[facIndex][1]/-100) + "," + str(actualList[facIndex][0]/100)+ ",0</coordinates>\n")
                f.write("         </LineString>\n       </Placemark>\n\n")

            i += 1
        f.write("\n\n    </Document>\n</kml>")
    return None