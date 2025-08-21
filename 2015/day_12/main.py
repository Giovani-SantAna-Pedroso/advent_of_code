import sys
import re
import os
os.system('clear')

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
        row = row.strip()
        n_in_line =  sum_num(row) 
        ansA += n_in_line


        left = [ i.span()[0] for i in re.finditer("{", row)]
        right = [ i.span()[0] for i in re.finditer("}", row)]
        left.reverse()
        if len(left) == 0:
            n_in_line_b = sum_num(row)
            ansB+= n_in_line_b

        for i in range(len(left)):
            part_to_analise =  row[left[i]:right[i]]
            print('og:', row,  end=' -> ' )

            if ':"red"' in part_to_analise:
                # print('has red')
                tmp = row[0:left[i]]
                tmp2 =row[right[i]+1:]
        #         print("left: ", tmp, end=' --- ')
        #         print("right: ", tmp2)
                # print('old row', row)
        #         # print('tmp', tmp)
                row = tmp + tmp2
        #
        print('new row',row)
        n_in_line_b = sum_num(row)
        ansB+= n_in_line_b

    print("AnsA: ", ansA)
    print("AnsB: ", ansB)

