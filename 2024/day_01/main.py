import sys
import math


def getNumbersFromLine(line):
    tmp = line.split("   ")
    if "--debug" in sys.argv:
        print(tmp)

    # return {"num1": int(tmp[0])}
    return [int(tmp[0]), int(tmp[1].replace("\n", ""))]


def getLineInfo():
    lines = []

    with open(sys.argv[1], "r") as fs:
        lines = fs.readlines()
        return [getNumbersFromLine(i) for i in lines]


def getAnsPart1(col_1, col_2):
    col_1.sort()
    col_2.sort()

    ans = 0
    for i in range(len(col_1)):
        ans += abs(col_1[i] - col_2[i])

    return {"answer": ans, "sort_col_1": col_1, "sort_col_2": col_2}


def getAnsPart2(col_1, col_2):
    ans = 0
    col_1_set = set(col_1)

    if "--debug" in sys.argv:
        print(col_1_set)

    count_num = {}
    times_num_apear_col2 = {}

    for i in col_1_set:
        count_num[i] = col_1.count(i)
        times_num_apear_col2[i] = col_2.count(i)
        ans += col_1.count(i) * col_2.count(i) * i

    if "--debug" in sys.argv:
        print(count_num)
        print(times_num_apear_col2)
        print(ans)

    return {"answer": ans}


lines = getLineInfo()
col_1 = [i[0] for i in lines]
col_2 = [i[1] for i in lines]

part1 = getAnsPart1(col_1, col_2)
part2 = getAnsPart2(part1["sort_col_1"], part1["sort_col_2"])

print(f"The answer for the part 1° is: {part1['answer']}")
print(f"The answer for the part 2° is: {part2['answer']}")
