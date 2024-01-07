import sys
import re

print("Day 1")

file = sys.argv[1]

def getFileData(file):
    with open(file, 'r') as file:
        content = file.read()[:-1].split('\n')
        return content

def getNumbersInLine(line):
    tmp = line
    num = re.sub(r'\D*', "", tmp)

    if len(num) == 1:
        return int(num + num)
    
    return int(num[0] + num[-1])

def getNumbersInLine2(line):
    tmp = line
    tmp= tmp.replace('one', 'o1e');
    tmp= tmp.replace('two', 't2o');
    tmp= tmp.replace('three', 't3e');
    tmp= tmp.replace('four', 'f4r');
    tmp= tmp.replace('five', 'f5e');
    tmp= tmp.replace('six', 's6x');
    tmp= tmp.replace('seven', 's7n');
    tmp= tmp.replace('eight', 'e8t');
    tmp= tmp.replace('nine', 'n9e');

    return getNumbersInLine(tmp)



content = getFileData(file)

ans = 0

try:
    for line in content:
        ans += getNumbersInLine(line)
    print(f"the answer for the first part is {ans}")
except:
    print("This file can't be used in the part 1") 


ans2 = 0
for line in content:
    ans2 += getNumbersInLine2(line)

print(f"the answer for the first part is {ans2}")

