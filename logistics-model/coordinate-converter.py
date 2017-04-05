import csv

stationsCSV = open('stations-raw.csv', 'r')
stations = csv.reader(stationsCSV, delimiter=',', quotechar='"')
stationsFile = open('stations.csv', 'w')
stationsWriter = csv.writer(stationsFile, delimiter=',', quotechar='|',
                         quoting=csv.QUOTE_MINIMAL)
stationData = []

junctionsCSV = open('junctions-raw.csv', 'r')
junctions = csv.reader(junctionsCSV, delimiter=',', quotechar='"')
junctionsFile = open('junctions.csv', 'w')
junctionsWriter = csv.writer(junctionsFile, delimiter=',', quotechar='|',
                         quoting=csv.QUOTE_MINIMAL)
junctionData = []

padding = 2
minLat = float('inf')
maxLat = 0.0
minLon = float('inf')
maxLon = 0.0

for station in stations:
    lat = float(station[0])
    lon = float(station[1])
    stationData.append([lon, lat, station[2]])
    junctionData.append([lon, lat, station[2]])
    if lat < minLat:
        minLat = lat
    if lat > maxLat:
        maxLat = lat
    if lon < minLon:
        minLon = lon
    if lon > maxLon:
        maxLon = lon

for junction in junctions:
    lat = float(junction[0])
    lon = float(junction[1])
    junctionData.append([lon, lat, junction[2]])
    if lat < minLat:
        minLat = lat
    if lat > maxLat:
        maxLat = lat
    if lon < minLon:
        minLon = lon
    if lon > maxLon:
        maxLon = lon

scaleFactor = min(60.0 / (maxLat - minLat), 60.0 / (maxLon - minLon))
botLeftLat = minLat - padding / scaleFactor
botLeftLon = minLon - padding / scaleFactor
topRightLat = botLeftLat + 60.0 / scaleFactor
topRightLon = botLeftLon + 60.0 / scaleFactor
print("Bottom Left: " + str(botLeftLat) + ", " + str(botLeftLon))
print("Top Right: " + str(topRightLat) + ", " + str(topRightLon))

for i in range(len(stationData)):
    stationData[i][0] = (stationData[i][0] - minLon) * scaleFactor + padding
    stationData[i][1] = (stationData[i][1] - minLat) * scaleFactor + padding

for i in range(len(junctionData)):
    junctionData[i][0] = (junctionData[i][0] - minLon) * scaleFactor + padding
    junctionData[i][1] = (junctionData[i][1] - minLat) * scaleFactor + padding

for station in stationData:
    stationsWriter.writerow(station)

for junction in junctionData:
    junctionsWriter.writerow(junction)

stationsCSV.close()
stationsFile.close()
junctionsCSV.close()
junctionsFile.close()
