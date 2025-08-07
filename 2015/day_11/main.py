import sys

# passowords = ["hijklmmn", 'abbceffg', 'abbcegjk']
passowords = ['cqjxjnds', 'cqjxxyzz']
# passowords = ["abcdefgh", 'ghijklmn']

def firs_rule(password):
    for i in range(len(password) -2):
        if ord(password[i]) == (ord(password[i+1]) -1) == (ord(password[i+2])-2):
            return True
        ...

    return False

def sedond_rule(password):
    if 'i' in password or 'l' in password or 'o' in password:
        return False
        ...

    return True

def thrid_rule(password):
    # print("\n\n")
    # print(password)
    for i in range(len(password) -1):
        if password[i] == password[i+1]:
            # print("frist Pari", (password[i], password[i+1]))
            # print(password[i+2:])
            for j in  range( i+2, len(password) -1):
                if password[j] == password[j+1]:
                    # print("second Pari", (password[j], password[j+1]))
                    return True


    return False

# print(ord("z"))
def increase_password(string):
    arr_str = list(string)
    for i in range(len(arr_str) - 1, -1, -1):
        ascii_char = ord(arr_str[i])
        # print(arr_str)
        if ascii_char  <=121:

            arr_str[i] = chr(ascii_char +1)
            return "".join(arr_str)
        else: 
            arr_str[i] = 'a'

        # print(string[i], end="")

    return "".join(arr_str)


# print(increase_password('xzz'))

for i in passowords:
    aaaa = 0
    crr_pass = increase_password(i)

    while True:
        if firs_rule(crr_pass) and sedond_rule(crr_pass) and thrid_rule(crr_pass):
            print(i, "the next pass", crr_pass)
            break
        crr_pass = increase_password(crr_pass)


    # print(i, "-> first:", firs_rule(i), "- second:", sedond_rule(i), "- thrid:", thrid_rule(i))
