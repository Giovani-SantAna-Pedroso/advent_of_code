import sys 
import copy
from    pprint import pprint as print

file_name = sys.argv[1]

class Node:
    def __init__(self,output, input1, input2, ) -> None:
        ...

        

def parse_node(line):
    node = { 'output':'','input1':"", 'input2':"", 'type':''}
    arr_line = line.split()
    size_arr = len(arr_line)

    if size_arr == 3:
        node['input1'] = arr_line[0]
        node['type'] = "ASING"

    elif size_arr == 4:

        node['input1'] = arr_line[1]
        node['type'] = "NOT"

    else:
        node['input1'] = arr_line[0]
        node['input2'] = arr_line[2]
        node['type'] = arr_line[1]

    
    node['output'] = arr_line[-1]
    return node



operations = {
        "OR": lambda val1, val2: int(val1) | int(val2),
        "AND": lambda val1, val2: int(val1) & int(val2),
        "NOT": lambda val1, _: ~(int(val1)) & 0xFFFF,
        "RSHIFT": lambda val1, val2: int(val1) >> int(val2),
        "LSHIFT": lambda val1, val2: int(val1) << int(val2),
        "ASING": lambda val1, _: int(val1) ,
        }

# def resolve_circuit(circuit):


with open(file_name, 'r') as file:
    lines =file.readlines()
    lines = list(map(lambda i: i.replace("\n",''), lines))
    entry = dict()
    entry_arr = []
    for i in lines:
        parsed_node = parse_node(i)
        entry[parsed_node['output']] = {**parsed_node}
        entry_arr.append({**parsed_node}
)
    entry_og = copy.deepcopy(entry)

    result_output = dict()
    while True :   
        initial_nodes =[]
        cp_entry = {**entry}

        for i in entry:
            is_input_1_num = str(entry[i]['input1']).isdigit()
            is_input_2_num_or_empty = str(entry[i]['input2']).isdigit() or entry[i]['input2'] == ""
            if is_input_2_num_or_empty and is_input_1_num :
                initial_nodes.append(entry[i])
                del cp_entry[i]
        entry = {**cp_entry}

        # print(initial_nodes)

        for i in initial_nodes: 
            # print(i)
            result_output[i['output']] = operations[i['type']](i['input1'], i['input2'])


        if len(entry) ==0:
            # print(result_output)
            break

        for i in entry:
            # print(i)
            if entry[i]['input1'] in result_output:
                entry[i]['input1'] = result_output[entry[i]['input1']]

            if entry[i]['input2'] in result_output:
                entry[i]['input2'] =   result_output[entry[i]['input2']]


        # print(entry)
    ansA = result_output['a']
    print(f"ansA: {result_output['a']}")

    
    result_output = dict()
    for i in entry_og:
        if entry_og[i]['input1'] == 'b':
            entry_og[i]['input1'] = str(ansA) 

        if entry_og[i]['input2'] == 'b':
            entry_og[i]['input2'] = str(ansA) 



    entry = copy.deepcopy(entry_og)

    result_output = dict()
    while True :   
        initial_nodes =[]
        cp_entry = {**entry}

        for i in entry:
            is_input_1_num = str(entry[i]['input1']).isdigit()
            is_input_2_num_or_empty = str(entry[i]['input2']).isdigit() or entry[i]['input2'] == ""
            if is_input_2_num_or_empty and is_input_1_num :
                initial_nodes.append(entry[i])
                del cp_entry[i]
        entry = {**cp_entry}

        # print(initial_nodes)

        for i in initial_nodes: 
            # print(i)
            result_output[i['output']] = operations[i['type']](i['input1'], i['input2'])


        if len(entry) ==0:
            # print(result_output)
            break

        for i in entry:
            # print(i)
            if entry[i]['input1'] in result_output:
                entry[i]['input1'] = result_output[entry[i]['input1']]

            if entry[i]['input2'] in result_output:
                entry[i]['input2'] =   result_output[entry[i]['input2']]


        # print(entry)
    ansA = result_output['a']
    print(f"ansB: {result_output['a']}")
#
        # break





