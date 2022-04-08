##========================== Study for Final ============================##
import urllib.request
import json

def printResults(data):
    # use JSON module to load string data in a dictionary:
    theJSON = json.loads(data)
    # to access the contents of the JSON:
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])
    
    # output: the number of events, the magnitude of each event name
    count = theJSON["metadata"]["count"]
    print(str(count) + " event recorded")
    print("============================")
    #for each event, prind the place where it occured:
    count = 0
    for i in theJSON["features"]:
        place = (i["properties"]["place"])
        print("{:0>3d}) {} " .format(count, place))
        count+=1
    print("-------------------\n")
    
    # filter results to print events over magnitude 4:
    print("Events that were over magnitude 4: \n\n")
    for i in theJSON["features"]:
        if i["properties"]["mag"] >=4.0:
            print("{:2.1f} {:s}" .format(i["properties"]["mag"], i["properties"]["place"]))
    print("-------------------\n")
    
    # filter events to print events where at least 
    # one person reported feeling the earthquake:
    print("Events that were reported:\n\n")
    for i in theJSON["features"]:
        feltReports = i["properties"]["felt"]
        if(feltReports != None):
            if(feltReports > 0):
                print(" %2.1f" % i["properties"]["mag"], i["properties"]["place"], " reported: " + str(feltReports) + " times")
                
    
def main():
    # for online json reader: https://jsoneditoronline.org/
    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    # to open URL and read data:
    webUrl = urllib.request.urlopen(urlData)
    print("result code: " + str(webUrl.getcode()))   # should be 200
    print("=====================================")
    
    # 200 = default for 'OK' 
    if(webUrl.getcode() == 200):
        data = webUrl.read().decode("utf-8")    # if external = webUrl'GETDATA'
        printResults(data)
    else:
        print("Received an error, cannot retrieve results" + str(webUrl.getcode()))
        
if __name__ == "__main__":
    main()





    
    

