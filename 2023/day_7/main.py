import sys
print("Day 7")

ranksOfCards = {'A':'12','K':'11','Q':'10','J':'9','T':'8','9':'7',
                '8':'6','7':'5','6':'4','5':'3','4':'2','3':'1','2':'0'}

file = sys.argv[1]
# print(file)
def getFileData(filePath):
    with open(filePath, 'r') as file:
        content = file.read().split('\n')[:-1]
        handNbits = list(map(lambda item: item.split(" "), content))
        # print(content)
        # print(handNbits)
    # print(filePath)
    return {'content':content, 'handNbits':handNbits}

# the kinds are Five of a kind= 6, Four of a kind = 5 so on 
def getTypeOfHand(hand):
    #find the unique values
    unique = set(hand)
    kinds = []
    for i in unique:
       cardsInHand = hand.count(i)
       kinds.append(cardsInHand)
    # print(kinds)

    if 5 in kinds:
        return '6'
    elif 4 in kinds:
        return '5'
    elif 3 in kinds and 2 in kinds:
        return '4'
    elif 3 in kinds:
        return '3'
    elif kinds.count(2) == 2:
        return '2'
    elif 2 in kinds:
        return '1'
    return '0'

def getPoinstNtypeOfHand(hand):
    typeHand = getTypeOfHand(hand)
    points = "" + str(typeHand)

    for i in hand:
        points += ranksOfCards[i]

    return {'points':int(points), 'type':typeHand}

def getHandsWbitsWpoints(hands):
    tmp = []
    for i in hands:
        typeNpoinst = getPoinstNtypeOfHand(i[0])
        # print(f"{i[0]} points {typeNpoinst['points']}")
        tmp.append({'hand':i[0], 'bits':int(i[1]),
                    'type':typeNpoinst['type'] ,'points':typeNpoinst['points'],})
    return tmp


data = getFileData(file)
# print(data)

# typeOfHand = getTypeOfHand(data['handNbits'][0][0])

handsWbitsWpoints = getHandsWbitsWpoints(data['handNbits'])

print(handsWbitsWpoints)
