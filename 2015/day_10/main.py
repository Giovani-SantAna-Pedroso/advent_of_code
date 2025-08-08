import sys


initial = '1113222113'
timesA = 40
timesB = 50

if '--test' in sys.argv:
    initial = '1'
    times = 5

crr = initial

ansA = 0
ansB = 0

for x in range(timesB):
    print(x)
    newValue = ""
    times_n_repeat = 1
    tmp = ''
    # print('Current val: ', crr)

    for i in range(len(crr)):

        if i != 0 and (crr[i] != crr[i-1]):
            tmp += ','
        tmp += crr[i]
        # print(crr[i])

    tmp = tmp.split(',')

    for i in tmp:
        newValue += f"{len(i)}{i[0]}"
    # print(newValue)
    crr = newValue

    if x == (timesA -1):
        ansA = len(crr)

# prv = 1
# for _ in range(timesA):
#     prv **=  1.303577
#
# print(prv)
# print(len(str(prv)))
    



print("ansA", ansA)

print("ansB", len(crr))


