import sys
print("Day 7")

ranksOfCards = {'A':'13','K':'12','Q':'11','J':'10','T':'09','9':'08',
                '8':'07','7':'06','6':'05','5':'04','4':'03','3':'02','2':'01', }

ranks_of_cards_q2 = {'A':'13','K':'12','Q':'11','T':'10','9':'09',
                '8':'08','7':'07','6':'06','5':'05','4':'04','3':'03','2':'02','J':'01', }

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

def getTypeOfHand2(hand):
    #find the unique values
    jokers = hand.count("J")
    unique = set(hand)
    kinds = []


    for i in unique:
       cardsInHand = hand.count(i) + jokers
       kinds.append(cardsInHand)

    if jokers == 5:
        return '6'

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

def getPoinstNtypeOfHand(hand, type_game):
    typeHand = None
    if type_game == 1:
        typeHand = getTypeOfHand(hand)
    elif type_game == 2:
        typeHand = getTypeOfHand2(hand)
    points = "" + str(typeHand)

    for i in hand:
        if type_game == 1:
            points += ranksOfCards[i]
        elif type_game == 2:
            points += ranks_of_cards_q2[i]

    return {'points':int(points), 'type':typeHand}

def getHandsWbitsWpoints(hands, type_game):
    tmp = []
    for i in hands:
        typeNpoinst = getPoinstNtypeOfHand(i[0], type_game)
        # print(f"{i[0]} points {typeNpoinst['points']}")
        tmp.append({'hand':i[0], 'bits':int(i[1]),
                    'type':typeNpoinst['type'] ,'points':typeNpoinst['points'],})
    return tmp

def rearenge_hands_weaks_t_strong(hands):
    # print("Rearenge")
    # print(hands)
    rearenge_hands_t = sorted(hands, key=lambda x: x['points'], reverse=False)
    return rearenge_hands_t

def get_ans_part_1(rearenge_hands_t):
    ans = 0
    rank = 1
    for i in rearenge_hands_t:
        ans += i['bits'] * rank
        rank += 1
    print(ans)


data = getFileData(file)
# handsWbitsWpoints = getHandsWbitsWpoints(data['handNbits'], 1)
# rearenge_hands = rearenge_hands_weaks_t_strong(handsWbitsWpoints)
# get_ans_part_1(rearenge_hands)


handsWbitsWpoints_q2= getHandsWbitsWpoints(data['handNbits'], 2)
rearenge_hands_2 = rearenge_hands_weaks_t_strong(handsWbitsWpoints_q2)
get_ans_part_1(rearenge_hands_2)

