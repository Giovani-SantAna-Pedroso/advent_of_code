import sys
import math

file = sys.argv[1]

with open(file) as file:
    lines = file.readlines()


    ansA = 0
    ansB = 0

    for line in lines:
        sizes = list(map(int, line.split("x")))
        l, w, h = sizes

        areas = [l*w, w*h, l*h]
        ansA += sum(areas)* 2 + min(areas)
        
        rest_ribbon = math.prod(sizes)
        sizes.remove(max(sizes))
        perimeter = 2* sizes[0]+ 2* sizes[1]
        ansB += perimeter + rest_ribbon


        
    
    print("Answer A: ", ansA)
    print("Answer B: ", ansB)
        
