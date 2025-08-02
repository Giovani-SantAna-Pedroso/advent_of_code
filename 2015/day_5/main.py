import sys

file_input = sys.argv[1]
print("Day 05\n")

def print_d(x, end=''):
    if "input.txt" not in sys.argv:
        print(x, end=end)


def three_vowels(line):
    vowels = ['a', 'e', 'i', 'o', 'u']
    amount_vowels = 0
    for i in line:
        if i in vowels:
            amount_vowels += 1
            if amount_vowels >= 3:
                return True
    return False

def double_letters(line):
    for i in range(len(line) -1):
        if line[i] == line [i+1]:
            return True
    return False

def does_not_have_forbbiden(line):
    forbbiden = ['ab', 'cd','pq','xy']
    for i in forbbiden:
        if i in line:
            return False
    return True

def two_paris(line):
    # print(line, "\n" )
    for i in range(len(line)-1):
        pair_to_search = line[i:i+2]
        what_search = line[i+2:]

        # print(f"searchin {pair_to_search} in {what_search}")
        if pair_to_search in what_search:
            # print("ok")
            return True
        # print()
        
    return False

def mirror(line):
    # return True
    for i in range(len(line)-2):
        if line[i] == line[i+2]:
            return True
    return False

with open(file_input, 'r') as file:
    amount_good_words_a = 0
    amount_good_words_b = 0
    for line in file:
        line = line.strip()

        if double_letters(line) and does_not_have_forbbiden(line) and three_vowels(line):
            amount_good_words_a += 1

        # print(line)

        if mirror(line) and two_paris(line) :
        # if two_paris(line) :
            amount_good_words_b += 1

    print("Answer A: ",amount_good_words_a)
    print("Answer B: ",amount_good_words_b)





