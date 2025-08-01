import sys

file = sys.argv[1]
print("Checking the file: ", file)

def get_new_possition(x, y, direction):
    if direction == "^":
        y +=1
    elif direction == "v":
        y -=1
    elif direction == ">":
        x +=1
    elif direction == "<":
        x -=1

    return (x , y)

with open(file, 'r') as fs:
    lines = fs.readlines()

    house_visited = {(0,0):0}
    current_pos_y = 0
    current_pos_x = 0

    for i in lines:
        for j in i:
            if j == "^":
                current_pos_y +=1
            elif j == "v":
                current_pos_y -=1
            elif j == ">":
                current_pos_x +=1
            elif j == "<":
                current_pos_x -=1
            house_visited[(current_pos_x,current_pos_y)] = 0

    n_house_visited = len(house_visited)
    print("Answer A: ", n_house_visited)


    # Part B
    house_visited_santa = {(0,0):0}
    house_visited_bot = {(0,0):0}

    current_pos_y_santa = 0
    current_pos_x_santa = 0

    current_pos_y_bot = 0
    current_pos_x_bot = 0

    for i in lines:
        for j in range(len(i)):
            if j % 2 ==0 :
                if i[j] == "^":
                    current_pos_y_santa +=1
                elif i[j] == "v":
                    current_pos_y_santa -=1
                elif i[j] == ">":
                    current_pos_x_santa +=1
                elif i[j] == "<":
                    current_pos_x_santa -=1
                house_visited_santa[(current_pos_x_santa,current_pos_y_santa)] = 0

            else:
                if i[j] == "^":
                    current_pos_y_bot +=1
                elif i[j] == "v":
                    current_pos_y_bot -=1
                elif i[j] == ">":
                    current_pos_x_bot +=1
                elif i[j] == "<":
                    current_pos_x_bot -=1
                house_visited_bot[(current_pos_x_bot,current_pos_y_bot)] = 0

    # print("santa: ", house_visited_santa)
    # print("bot: ", house_visited_bot)

    n_house_visited_bot_n_santa = set(house_visited_santa) | set(house_visited_bot)
    # print(n_house_visited_bot_n_santa)




    print("Answer B: ", len(n_house_visited_bot_n_santa))
