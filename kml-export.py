# Program to export data to KML file for visualization

def kmlexport():
    coordList = []
    advList = []


def createLineStyle(colourSel, adv):
    colours = ["ff0000ff", "ff00ffff", "ffff0000", "ff00ff00", "ff800080", "ff0080ff", "ff336699", "ffff00ff"]
    width = "<width>3</width>"
    facCity = "".join(facCity.split())
    
    if colourSel >= len(colours):
        colourSel = colourSel%len(colours)
    
    lineStyle = "<Style id=\"" + adv + "Line\"> \n  <LineStyle>\n    <color>" + colours[colourSel] + "</color>\n         " + width + "\n </LineStyle>\n   </Style>\n\n\n"
    if colourSel == len(colours):
        colourSel = 0
    return lineStyle

def display(coordlist, advList, fname):
    f = open(fname, "x")
    f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
    f.write("<kml xmlns=\"http://www.opengis.net/kml/2.2\">\n    <Document>\n")
    f.write("    <name>"+ fname +"</name>\n\n\n")
    facilityPin = ""
    satPin = ""
    facilityPin = "<Style id=\"facilityPins\"> \n  <IconStyle>\n    <scale>1.5</scale>\n    <Icon>\n   <href>http://maps.google.com/mapfiles/kml/paddle/ylw-stars.png</href>\n      </Icon>\n          </IconStyle>\n   </Style>\n\n\n"
    satPin = "<Style id=\"satPins\"> \n  <IconStyle>\n    <scale>0.75</scale>\n    <Icon>\n   <href>http://maps.google.com/mapfiles/kml/paddle/blu-blank.png</href>\n      </Icon>\n          </IconStyle>\n   </Style>\n\n\n"
    colourSel = 0
    i = 0
    lineStyles = []
    f.write(facilityPin)
    f.write(satPin)

    while i < len(facilities):
            lineStyles.append(createLineStyle(i, facilities[i]))
            facLineStyleName = "".join(facilities[i].split())
            facIndex = cityList.index(facilities[i])
            nearCities = []
            nearCities = nearestCities(facilities[i], facilities, cityList, distanceList)
            f.write("<Placemark>\n         <name>"+ facilities[i] +" (Facility)</name>\n")
            f.write("      <styleUrl>#facilityPins</styleUrl>\n")
            f.write("         <Point>\n")
            f.write("           <coordinates>"+ str(coordList[facIndex][1]/-100) + "," + str(coordList[facIndex][0]/100)+ ",0</coordinates>\n")
            f.write("         </Point>\n       </Placemark>\n\n")
            f.write(lineStyles[i])
            for n in nearCities:
                satIndex = 0 
                satIndex = cityList.index(n)
                #print("<Placemark>\n         <name>"+ str(cityList[satIndex]) +"</name>\n")
                f.write("<Placemark>\n         <name>"+ str(cityList[satIndex]) +"</name>\n")
                f.write("      <styleUrl>#satPins</styleUrl>\n")
                f.write("         <Point>\n")
                f.write("           <coordinates>"+ str(coordList[satIndex][1]/-100) + "," + str(coordList[satIndex][0]/100)+ ",0</coordinates>\n")
                f.write("         </Point>\n       </Placemark>\n\n")

                f.write("\n<Placemark>\n")
                f.write("      <styleUrl>#"+ facLineStyleName + "Line</styleUrl>\n")
                f.write("      <LineString>\n")
                f.write("         <extrude>1</extrude>\n")
                f.write("         <tessellate>1</tessellate>\n")
                f.write("           <coordinates>"+ str(coordList[satIndex][1]/-100) + "," + str(coordList[satIndex][0]/100)+ ",0  "+ str(coordList[facIndex][1]/-100) + "," + str(coordList[facIndex][0]/100)+ ",0</coordinates>\n")
                f.write("         </LineString>\n       </Placemark>\n\n")

            i += 1
        f.write("\n\n    </Document>\n</kml>")
    return None