import sys
from PIL import Image
import numpy as np

file_name = sys.argv[1]

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
:
def change_lights(lights_arr, info):
    if info['type'] == 


with open(file_name, 'r') as file:
    
    lights_arr = [[0 for _ in range(1000)] for _ in range(1000)]
    show_array_state(lights_arr)

    for line in file:
        line = line.strip()
        info = get_line_info(line)
        print(info)
