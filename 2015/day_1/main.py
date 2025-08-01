import sys
import time

start = time.time()

file = f"./{sys.argv[1]}"
print("testing file: ", file)

with open(f"./{sys.argv[1]}", 'r') as file:

    lines = file.readlines()

    ans1 = 0
    ans2 = 0 
    stepts = 0 
    print(lines)

    for i in lines:
        for j in range(len(i.strip())):
            ans1 += 1 if i[j] == "(" else -1
            # print(ans1)
            if ans1 < 0 and ans2 == 0:
                ans2 = j+1
            # print(ans1, j)

    print("\033[7m\033[34mAnswer A:\033[0m ", ans1)
    print("\033[7m\033[34mAnswer B:\033[0m ", ans2)


    
print(f"It took {time.time() - start} to run")


