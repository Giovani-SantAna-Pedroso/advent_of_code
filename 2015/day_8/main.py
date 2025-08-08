import sys
import ast

file_name = sys.argv[1]

with open(file_name, 'r') as file:
    ansA = 0

    ansB = 0
    for line in file:
        line = line.strip()
        


        converted_string = ast.literal_eval(line)
        # print(line, end=" -> ")
        # print(repr(line).replace('"', r'\"'), end=" -> ")
        # print(converted_string, end=" -> ")
        # print(len(converted_string))

        ansA += len(line) - len(converted_string) 
        ansB += len(repr(line).replace('"', r'\"')) - len(line)
    print("AnsA: ", ansA)
    print("AnsB: ", ansB)



