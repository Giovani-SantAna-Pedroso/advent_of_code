import sys

print("Day 5")

path_file = sys.argv[1]


def getFileData(path_file):
    data = {}
    with open(path_file) as file: 
        content = file.read().split('\n\n')
        for i in content:
            key, values = i.split(":")
            values = values.split("\n")
            tmp = []
            for j in values:
                if j != "":
                    tmp2 = j.split(" ")
                    if "" in tmp2:
                        tmp2.remove("")
                    tmp2 = [int(item) for item in tmp2]
                    tmp.append(tmp2)
            data[key] =tmp
    return data

def sourceToDestination(source, mapSourceToLocation):
    for i in mapSourceToLocation:
        if  source >= i[1] and source <= (i[1] + i[2]):
            return i[0] + abs( i[1] - source )
    return source

def getLocationSeed(seed, data):
    soil = sourceToDestination(seed, data['seed-to-soil map'])
    fertilizer = sourceToDestination(soil, data['soil-to-fertilizer map'])
    water = sourceToDestination(fertilizer, data['fertilizer-to-water map'])
    light = sourceToDestination(water, data['water-to-light map'])
    temperature = sourceToDestination(light, data['light-to-temperature map'])
    humidity = sourceToDestination(temperature, data['temperature-to-humidity map'])
    location= sourceToDestination(humidity, data['humidity-to-location map'])

    return location

def answerPart1(data):
    seedsArr = data['seeds'][0]
    lowestLocation = None
    for i in seedsArr:
        locationActualSeed = getLocationSeed(i, data)
        if lowestLocation == None or locationActualSeed <lowestLocation:
            lowestLocation = locationActualSeed
    
    print(f"The answer for the first part is: {lowestLocation}")
        
    # 0 ok, 1 ok until the end, 2 ok 
    
def answerPart2(data):
    seedsArr = data['seeds'][0]
    lowestLocation = None
    
    print("The answer for the second part might be take some hours, so relax")    

    for i in range(0, len(seedsArr), 2):
        for j in range(seedsArr[i+1]):
            locationActualSeed = getLocationSeed(seedsArr[i]+j, data)
            if lowestLocation == None or locationActualSeed <lowestLocation:
                lowestLocation = locationActualSeed
        print(f"Progress {int(i/2)}/{int(len(seedsArr)/2)} -> lowest so far {lowestLocation}")

    print(f"The answer for the second part is: {lowestLocation}")
    
data = getFileData(path_file)

answerPart1(data)
answerPart2(data)


