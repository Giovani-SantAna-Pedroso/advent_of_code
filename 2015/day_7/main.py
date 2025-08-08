import sys 

file_name = sys.argv[1]

class Node:
    def __init__(self,output, input1, input2, ) -> None:
        ...

        

def parse_node(line):
    node = {'input1':"", 'input2':"", 'output':'', 'type':''}
    arr_line = line.split()
    size_arr = len(arr_line)
    print(arr_line)

    if size_arr == 3:
        node['input1'] = arr_line[0]
        node['type'] = "asign"

    if size_arr == 4:
        node['input1'] = arr_line[1]
        node['type'] = "NOT"

    else 
        node['input1'] = arr_line[1]
        node['type'] = "NOT"

    
    node['output'] = arr_line[-1]
    return node



operations = {
        "OR": lambda val1, val2: val1 | val2,
        "AND": lambda val1, val2: val1 & val2,
        "NOT": lambda val1: ~(val1) & 0xFFFF,
        "RSHIFT": lambda val1, val2: val1 >> val2,
        "LSHIFT": lambda val1, val2: val1 << val2,
        }

with open(file_name, 'r') as file:
    lines =file.readlines()
    lines = list(map(lambda i: i.replace("\n",''), lines))
    for i in lines:
        parse_node(i)
    ...
        
