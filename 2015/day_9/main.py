import sys 

file_name = sys.argv[1]

with open(file_name, 'r') as file:
    for line in file:
        line = line.strip()
        print(line)


