import sys


def getLines():
    with open(sys.argv[1], "r") as file:
        return [[int(j) for j in i.replace("\n", "").split()] for i in file.readlines()]


def isLineSafe(line):
    direction = line[0] > line[1]

    if direction:
        for i in range(1, len(line)):
            if line[i - 1] - line[i] not in [1, 2, 3]:
                return {"isSafe": False, "n": i, "n-1": i - 1}
    else:
        for i in range(1, len(line)):
            if line[i - 1] - line[i] not in [-1, -2, -3]:
                return {"isSafe": False, "n": i, "n-1": i - 1}
        ...

    return {"isSafe": True}


def printDebug(x, msg=""):
    if "--debug" in sys.argv:
        print(f"{msg} {x}")


def getAnsPart1(lines):
    ans = 0
    for line in lines:
        if isLineSafe(line)["isSafe"]:
            ans += 1
        printDebug(f"is the {line} safe: {isLineSafe(line)}")
    return {"ans": ans}


def getAnsPart2(lines):
    ans = 0
    for line in lines:
        if isLineSafe(line)["isSafe"]:
            # print("This line is safe no altereation", line)
            ans += 1
            continue

        for i in range(len(line)):

            new_line = line[0:i] + line[i + 1 :]
            if isLineSafe(new_line)["isSafe"]:
                ans += 1

                # print("This line is safe with altereation", line)
                break

        ...
    return {"ans": ans}


lines = getLines()
ans1 = getAnsPart1(lines)
print(f"the answer for the 1° part is: {ans1['ans']}")

print(f"------------")
ans2 = getAnsPart2(lines)
print(f"the answer for the 2° part is: {ans2['ans']}")
