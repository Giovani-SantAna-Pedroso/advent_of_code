import sys

file_path = sys.argv[1]

class Keypad:
    def __init__(self) -> None:
        self.keypad = [
                [1,2,3],
                [4,5,6],
                [7,8,9]
                ]
        self.password= ""
        self.current_pos = [1,1]

        self.keypad_real = [
                [' ', ' ', '1', ' ', ' '],
                [' ', '2', '3', '4', ' '],
                ['5', '6', '7', '8', '9'],
                [' ', 'A', 'B', 'C', ' '],
                [' ', ' ', 'D', ' ', ' '],
                ]
        self.password_real= ""
        self.current_pos_real = [2,0]

    def move_up(self):

        self.current_pos[0] += -1 if self.current_pos[0] != 0 else 0  
        if self.current_pos_real[0] == 0 or self.keypad_real[self.current_pos_real[0]-1][self.current_pos_real[1]] == " ":
            return

        # print('up')
        self.current_pos_real[0] -= 1
        ...
    def move_down(self):
        self.current_pos[0] -= -1 if self.current_pos[0] != 2 else 0  
        if self.current_pos_real[0] == 4 or self.keypad_real[self.current_pos_real[0]+1][self.current_pos_real[1]] == " ":

            return

        # print('down')
        self.current_pos_real[0] += 1

    def move_righ(self):
        self.current_pos[1] -= -1 if self.current_pos[1] != 2 else 0  
        if self.current_pos_real[1] == 4 or self.keypad_real[self.current_pos_real[0]][self.current_pos_real[1]+1] == " ":
            return
        # print('r')
        self.current_pos_real[1] += 1

    def move_left(self):
        self.current_pos[1] += -1 if self.current_pos[1] != 0 else 0  
        if self.current_pos_real[1] == 0 or self.keypad_real[self.current_pos_real[0]][self.current_pos_real[1]-1] == " ":
            return
        # print('l')
        self.current_pos_real[1] -= 1

    def get_digit(self, line):
 #        print(
 # str(self.keypad_real[self.current_pos_real[0]][self.current_pos_real[1]])
 #                )
 #        print()
 #
        for i in line:
            if i == "U":
                self.move_up()
            elif i == "D":
                self.move_down()
            elif i == "L":
                self.move_left()
            elif i == "R":
                self.move_righ()

 #            print(
 # str(self.keypad_real[self.current_pos_real[0]][self.current_pos_real[1]])
 #                )
        self.password += str(self.keypad[self.current_pos[0]][self.current_pos[1]])
        self.password_real += str(self.keypad_real[self.current_pos_real[0]][self.current_pos_real[1]])

        # print("######")
    def get_password(self):
        return self.password

    def get_password_real(self):
        return self.password_real


with open(file_path, 'r') as file:
    keypad = Keypad()
    for line in file:
        line = line.strip()
        keypad.get_digit(line)
        # print(line)



    print("AnsA: ", keypad.get_password())
    print("AnsB: ", keypad.get_password_real())







