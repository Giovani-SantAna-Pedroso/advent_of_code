import re

import sys

path_file = sys.argv[1]

def getSym(path_file):
    with open(path_file) as file:
        line = file.read()
        line =re.sub(r'[\d\n.]', '', line) 
        sym = set(line)
        sym = list(sym)

        return sym

def file2dArray(path_file):
    with open(path_file) as file:
        line = file.read()
        # print(line)
        array1D = line.split('\n')
        y = len(array1D)
        x =0
        arrya2D = []
        for i in array1D[:-1]:
        # for i in array1D[:2]:
            tmp = list(i)
            x = len(tmp)
            arrya2D.append(tmp)
            # print(list(i))
        # print(arrya2D)
        return {'arr':arrya2D, 'shape':(x,y)}

def findSymPositons(array2D, sym_to_search):
    positions = []
    # print(array2D)
    for i in enumerate(array2D):
        for j in enumerate( i[1]):
            # print(j)
            if j[1] in sym_to_search:
                # print(j)
                positions.append({'sym':j[1], 'pos':(i[0],j[0])})
    # print(positions)
    return positions

def findNumbersForASym(symbol, arr):
    # (-1,-1)  ( 0, -1) ( 1,-1)
    # (-1, 0)  symbol   ( 1, 0) 
    # (-1, 1)  ( 0, 1)  ( 1, 1)
    pos_to_search = [[-1,-1], [ 0, -1], ( 1,-1), (-1, 0), ( 1, 0), (-1, 1), ( 0, 1), ( 1, 1)]

    numbres = []
    arr_content = arr['arr']
    arr_size = arr['shape']

    for i in pos_to_search:
        x = symbol['pos'][0] + i[0]
        y = symbol['pos'][1] + i[1]
        # print(len(arr))
        # if x <0 or y<0 or x> arr.shape[0] or y >arr.shape[1]:
            # continue
        val = arr_content[x][y]
        
        if val.isdigit():
            num = ''
            #get the digits on the left
            pos_x = y
            start = f'{pos_x}'
            end = start
            while (pos_x) >= 0 and arr_content[x][pos_x].isdigit() :
                num =  arr_content[x][pos_x] + num
                
                start=f'{pos_x}'
                pos_x -= 1

            pos_x = y+1
            while (pos_x) <= (arr_size[0] -1) and arr_content[x][pos_x].isdigit() :
                # print(f'{ arr[pos_x][y]} is a digit: {arr[pos_x][y].isdigit()}')
                # print(f'is {pos_x} bigger or equel 0: {(pos_x) >= 0 }')
                num +=  arr_content[x][pos_x]
                end=f'{pos_x}'
                pos_x += 1

            numbres.append({'num':{int(num)}, 'pos':f'{x}-{start}-{end}'})

    # remove the repeated numbers
    tmp = []
    # print(numbres)
    for i in numbres:
        tmp.append( i['pos'])

    unique_pos = set(tmp)
    # print(f'unique_pos {unique_pos}')
    unique_numbers = []
    for i in unique_pos:
        # print(i)
        for j in numbres:
            if j['pos'] == i:
                # print(j['num'].pop())
                # print(type(j['num'][0]))
                unique_numbers.append(j['num'].pop())
                break
    # print(f'unique numss {unique_numbers}')
    return {'nums':unique_numbers, 'sym':symbol['sym'], 'sym_pos':symbol['pos'] }


def removeRepeatNumbers(numbers):
    # get the positions unique positions
    tmp = []
    print(numbers)
    for i in numbers['nums']:
        tmp.append( i['pos'])

    unique_pos = set(tmp)
    # print(unique_pos)
    
    unique_numbers = []
    for i in unique_pos:
        # print(i)
        for j in numbers:
            if j['pos'] == i:
                # print(j['num'].pop())
                # print(type(j['num'][0]))
                unique_numbers.append(j['num'].pop())
                break
    return unique_numbers

def answerPart1(nums):
    ans = 0 
    for i in nums:
        for j in i['nums']:
            # print(j)
            ans += j

    print(f"the answer for the part 1 is {ans}")

def answerPart2(nums):
    ans = 0 
    # print(nums)
    for i in nums:
        if i['sym']=="*":
            if len(i['nums']) ==1:
                continue
            tmp = 1
            # print(f"* {i['nums']}")
            for j in i['nums']:
                # print(j)
                tmp *= j
            # print(tmp)
            ans += tmp

    print(f"the answer for the part 2 is {ans}")

symbols = getSym(path_file)
arrData = file2dArray(path_file)
symbols_pos = findSymPositons(arrData['arr'], symbols)

numbers = []
for sym in symbols_pos:
    tmp = findNumbersForASym(sym, arrData)
    numbers.append(tmp)

answerPart1(numbers)
answerPart2(numbers)




