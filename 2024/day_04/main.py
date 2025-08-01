import sys
import time 
start_time = time.time()

def get_info_file(path):

    arr=[]
    x = 'aaaaaa'
    with open(path, 'r') as file:
        arr = [ list(i[:-1]) for i in file.readlines()]

    return {'arr':arr}


arr= get_info_file( sys.argv[1])['arr']



def find_xmax(arr, x, y, max_x, max_y,cp_arr):
    amount_xmax = 0
    # Vertical down 
    if y +3 < max_y:
        if arr[y+1][x] == "M" and arr[y+2][x] == 'A' and arr[y+3][x] == "S":
            # cp_arr[y][x] = "X" 
            # cp_arr[y+1][x] = "M" 
            # cp_arr[y+2][x] = 'A' 
            # cp_arr[y+3][x] = "S"
            amount_xmax += 1

    # Vertical Up 
    if y -3 >= 0:
        if arr[y-1][x] == "M" and arr[y-2][x] == 'A' and arr[y-3][x] == "S":
            # cp_arr[y][x] = "X" 
            # cp_arr[y-1][x] = "M" 
            # cp_arr[y-2][x] = 'A' 
            # cp_arr[y-3][x] = "S"
            amount_xmax += 1

    # Horizontal Righ 
    if x+3 < max_x:
        if arr[y][x+1] == "M" and arr[y][x+2] == 'A' and arr[y][x+3] == "S":
            # cp_arr[y][x] = "X" 
            # cp_arr[y][x+1] = "M" 
            # cp_arr[y][x+2] = 'A' 
            # cp_arr[y][x+3] = "S"
            amount_xmax += 1

    # Horizontal Left 
    if x-3 >= 0:
        if arr[y][x-1] == "M" and arr[y][x-2] == 'A' and arr[y][x-3] == "S":
            # cp_arr[y][x] = "X" 
            # cp_arr[y][x-1] = "M" 
            # cp_arr[y][x-2] = 'A' 
            # cp_arr[y][x-3] = "S"
            amount_xmax += 1

    # Vertial Righ Up 
    if x+3 < max_x and y-3 >=0:
        if arr[y-1][x+1] == "M" and arr[y-2][x+2] == 'A' and arr[y-3][x+3] == "S":
            # cp_arr[y][x] = "X" 
            # cp_arr[y-1][x+1] = "M" 
            # cp_arr[y-2][x+2] = 'A' 
            # cp_arr[y-3][x+3] = "S"
            amount_xmax += 1

    # Vertial left Up 
    if x-3 >= 0 and y-3 >=0:
        if arr[y-1][x-1] == "M" and arr[y-2][x-2] == 'A' and arr[y-3][x-3] == "S":
            # cp_arr[y][x] = "X" 
            # cp_arr[y-1][x-1] = "M" 
            # cp_arr[y-2][x-2] = 'A' 
            # cp_arr[y-3][x-3] = "S"
            amount_xmax += 1


    # Vertial left down 
    if x-3 >= 0 and y+3 <max_y:
        if arr[y+1][x-1] == "M" and arr[y+2][x-2] == 'A' and arr[y+3][x-3] == "S":
            # cp_arr[y][x] = "X" 
            # cp_arr[y+1][x-1] = "M" 
            # cp_arr[y+2][x-2] = 'A' 
            # cp_arr[y+3][x-3] = "S"
            amount_xmax += 1

    # Vertial right down 
    if x+3 < max_x and y+3 <max_y:
        if arr[y+1][x+1] == "M" and arr[y+2][x+2] == 'A' and arr[y+3][x+3] == "S":
            # cp_arr[y][x] = "X" 
            # cp_arr[y+1][x+1] = "M" 
            # cp_arr[y+2][x+2] = 'A' 
            # cp_arr[y+3][x+3] = "S"
            amount_xmax += 1
    return amount_xmax


def find_x_max(arr, x, y, max_x, max_y,cp_arr):
    if x +2 < max_x and y+ 2 < max_y:
        if arr[y+1][x+1] != "A":
            return 0

        # cp_arr[y+1][x+1] = "A"

        # print(f"""
        #       {cp_arr[y][x]}.{cp_arr[y][x+2]}
        #       .A. 
        #       {cp_arr[y+2][x]}.{cp_arr[y+2][x+2]}
        #       """)

        # Mas - mas
        if (arr[y][x] == "M" and  arr[y+2][x+2] == "S") and (arr[y+2][x] == "M" and  arr[y][x+2] == "S"):
            # cp_arr[y][x] = "M"
            return 1

        # Mas - sam
        if (arr[y][x] == "M" and  arr[y+2][x+2] == "S") and (arr[y+2][x] == "S" and  arr[y][x+2] == "M"):
            # cp_arr[y][x] = "M"
            return 1

        # Sam - mas
        if (arr[y][x] == "S" and  arr[y+2][x+2] == "M") and (arr[y+2][x] == "M" and  arr[y][x+2] == "S"):
            # cp_arr[y][x] = "S"
            return 1

        # Sam - sam
        if (arr[y][x] == "S" and  arr[y+2][x+2] == "M") and (arr[y+2][x] == "S" and  arr[y][x+2] == "M"):
            return 1


        else:
            return 0 
    return 0 

max_y =len(arr)
max_x =len(arr[0])
cp_arr_1 = [["."] * max_y for _ in range(max_x)] 
cp_arr_2 = [["."] * max_y for _ in range(max_x)] 
ans_part1 = 0
ans_part2 = 0

print("max y", max_y)
print("max x", max_x)

for i in range(max_y):
    for j in range(max_x):
        if arr[i][j] == "X":
            # print("X on x:", j , "Y on y", i)
            # print("X", end="")
            cp_arr_1[i][j]="*"
            ans_part1 += find_xmax(arr, j,i, max_x, max_y, cp_arr_1)
        elif arr[i][j] == "S" or  arr[i][j] == "M" :
            ...
            ans_part2 += find_x_max(arr, j, i, max_x, max_y, cp_arr_2)
            # print(".",end="")

# for i in range(len(cp_arr_1)):
#     for j in range( len(cp_arr_1[0])):
#         # print(cp_arr_1[i][j], end="")
#     # print(cp_arr[i][j], end="")
#     print()

print(f"The answer for the part 1 is: {ans_part1}")
print()


# for i in range(len(cp_arr_2)):
#     for j in range( len(cp_arr_2[0])):
#         print(cp_arr_2[i][j], end="")
#     # print(cp_arr[i][j], end="")
#     print()
print(f"The answer for the part 2 is: {ans_part2}")

print(f"It takes seconds {time.time() - start_time} to execute")
