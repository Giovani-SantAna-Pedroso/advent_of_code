import re
import sys


def findMulsSum(content):
    x = re.findall(r"mul\((\d+),\s*(\d+)\)", content)
    a = [[int(i[0]) * int(i[1])] for i in x]

    ans = 0
    for i in a:
        ans += i[0]

    return ans


with open(sys.argv[1], "r") as file:
    content = file.read()

    print(f"the ans for the 1° part is: {findMulsSum(content)}")
    x = re.sub(r"don\'t\(\).*?do\(\)", "%%%%%%", content.replace('\n',''))
    print(f"the ans for the 2° part is: {findMulsSum(x)}")
