import sys
import re

file_path = sys.argv[1]

def sum_num(row):
    nums = re.findall(r'-?\d*', row)
    nums = filter(lambda i: i != '', nums)
    nums = map(int, nums)
    return sum(nums)

with open(file_path, 'r') as file:
    ansA = 0
    ansB = 0

    for row in file:
        n_in_line =  sum_num(row) 
        ansA += n_in_line
        reds = re.findall(r'{.*red*.}',row)
        print(reds)
        for i in reds:
            print(i)
        sumReds = 0
        for j in reds:
           sumReds += sum_num(j) 
           print(sumReds)
        ansB += sum_num(row) - sumReds
        print(sumReds)

    print("AnsA: ", ansA)
    print("AnsB: ", ansB)
