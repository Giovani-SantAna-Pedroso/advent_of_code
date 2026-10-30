import hashlib
import sys

file_name = sys.argv[1]

with open(file_name) as file:
    secret = file.readline().strip()
    ansA = 0
    while True:
        keyNans = f"{secret}{ansA}"
        hashHext =  hashlib.md5(keyNans.encode('utf-8')).hexdigest()
        if hashHext[0:5] == "00000":
            break
        ansA += 1
    print("Answer A: ", ansA )

    ansB = 1
    while True:
        keyNans = f"{secret}{ansB}"
        hashHext =  hashlib.md5(keyNans.encode('utf-8')).hexdigest()
        # print(hashHext[0:6])
        if hashHext[0:6] == "000000":
            break
        ansB += 1
    print("Answer B: ", ansB )



