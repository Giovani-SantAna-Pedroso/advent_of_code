import sys
from PIL import Image
from pprint import pprint 

import numpy as np

file_name = sys.argv[1]
# side_arr = 10
if file_name == "test2.txt":
    side_arr = 10
else:
    side_arr = 1000

def get_line_info(line):
    info = {"type":'', 'inital':[0,0] , 'final':[0,0]}
    line_splited = line.split()

    if 'on' in line:
        info['type'] = 'on'
        i = line_splited[2]
    elif 'off' in line:
        info['type'] = 'off'
        i = line_splited[2]
    else:
        info['type'] = 'toggle'
        i = line_splited[1]

    info['inital'] = list(map(int, i.split(',')))
    info['final']= list(map(int, line_splited[-1].split(',')))

    return info

def show_array_state(arr):
    array_np = np.array(arr, dtype=np.uint8)

    array_np = array_np * 255

    img = Image.fromarray(array_np).convert('1')
    img.show()
    # img.save('bw_output.png')

def change_lights(lights_arr, info):
    change_fun = None
    if info['type'] == 'on':
        change_fun = lambda i: 1
    elif info['type'] == 'off':
        change_fun = lambda i: 0
    else :
        change_fun = lambda i: 0 if i == 1 else 1 

    # print("i range: ", range(info['inital'][0], info['final'][0]))
    # print("j range: ", range(info['inital'][1], info['final'][1]+2))

    for i in range(info['inital'][0],  info['final'][0]):
        # print("i: ",i)
        for j in range(info['inital'][1], info['final'][1]):
            # print("j: ",j)
            lights_arr[i][j] = change_fun(lights_arr[i][j])


with open(file_name, 'r') as file:
    side_arr= 10
    lights_arr = [[0 for _ in range(side_arr)] for _ in range(side_arr)]
    show_array_state(lights_arr)
    ansA = 0 

    for line in file:
        line = line.strip()
        info = get_line_info(line)
        # lights_arr = change_lights(lights_arr, info)
        change_lights(lights_arr, info)

        # if test == final:
        # test += 1
        # pprint(lights_arr)
        # print(info)
        # show_array_state(lights_arr)


    show_array_state(lights_arr)
    for i in lights_arr:
        for j in i:
            ansA += j

    print("Answer A: ", ansA)

