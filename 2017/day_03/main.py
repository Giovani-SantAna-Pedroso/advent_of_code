import sys


input_val =None 
with open(sys.argv[1],'r') as file:
    input_val = int(file.read()[:-1])

ring=0
ring_pow=1

while True: 
    if ring_pow**2 >= input_val: 
        break 
    ring+=1
    ring_pow+=2

input_val=12
# input_val=21
max_val_ring=ring_pow**2
print(ring,ring_pow, max_val_ring) 

while True:
    # botton 
    if input_val <= max_val_ring and input_val >= (max_val_ring - ring_pow):
        ...
    # left
    elif input_val <= max_val_ring and input_val >= (max_val_ring - ring_pow):
        ...
    # top
    elif input_val <= max_val_ring and input_val >= (max_val_ring - ring_pow):
        ...
    #right
    elif input_val <= max_val_ring and input_val >= (max_val_ring - ring_pow):
        ...
