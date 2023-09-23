# Program to export data to KML file for visualization

def kmlexport():
    actualList = ['-47.7,15.4', '-50.0,16.4', '-52.4,17.3', '-54.5,18.2', '-56.5,19.3', '-58.2,20.3', '-59.9,21.0', '-61.0,21.6', '-62.2,22.6', '-63.5,23.5', '-64.8,23.9', '-65.9,24.3', '-66.7,25.3', '-67.2,26.4', '-67.7,28.0', '-68.3,30.4', '-67.6,32.9', '-66.9,36.0', '-65.8,39.5', '-66.2,43.5', '-65.5,45.3', '-62.0,48.0']
    advList = ['-66.1,23.0', '-66.0,23.6', '-66.6,24.1', '-67.5,24.8', '-67.7,25.3', '-67.8,26.8', '-68.3,28.8', '-67.7,31.3', '-67.0,35.5', '-67.1,38.9', '-66.0,43.0', '-65.9,45.3', '-62.0,48.5', '-56.4,52.1', '-50.0,53.7', '-52.2,52.6', '-42.5,54.5', '-51.3,53.4', '-41.3,54.3', '-50.1,53.0', '-48.4,52.5', '-34.0,54.0']
    fname = "hurricane.kml"
    display(actualList, advList, fname)
    return None


def display(actualList, advList, fname):
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


kmlexport()