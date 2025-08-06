import sys 

file_name = sys.argv[1]


operations = {
        "OR": lambda val1, val2: val1 | val2,
        "AND": lambda val1, val2: val1 & val2,
        "NOT": lambda val1: ~(val1) & 0xFFFF,
        "RSHIFT": lambda val1, val2: val1 >> val2,
        "LSHIFT": lambda val1, val2: val1 << val2,
        }

def convert_to_int(n):
    if n.isdigit():
        return int(n)
    return 0

with open(file_name, 'r') as file:
    dic_values = {}
    line =0 
    for row in file:
        row = row.strip()
        # print(line)
        arr_row = row.split()

        # print(arr_row)
        # print(arr_row)
        arr_len = len(arr_row)
        val_to_change = arr_row[-1]

        # Put a value into a variable
        if arr_len == 3:

            val = convert_to_int(arr_row[0]) if arr_row[0] not in dic_values else dic_values[arr_row[0]] 
            # arr_row[0])
            dic_values[val_to_change]= val
        elif arr_len == 4:
            val = convert_to_int(arr_row[1]) if arr_row[1] not in dic_values else dic_values[arr_row[1]] 
            dic_values[val_to_change] = operations["NOT"](val)
        else:
            val1 = convert_to_int(arr_row[0]) if arr_row[0] not in dic_values else dic_values[arr_row[0]] 
            val2 = convert_to_int(arr_row[2]) if arr_row[2] not in dic_values else dic_values[arr_row[2]] 
            dic_values[val_to_change] = operations[arr_row[1]](val1,val2)

        # sorted(dic_values, key=lambda)
        dic_values = dict(sorted(dic_values.items()))

        # for i,j in dic_values.items():
        #     print(i, j)

        line += 1

    print(dic_values['a'])
        
