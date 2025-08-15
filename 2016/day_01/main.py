import sys

file_path = sys.argv[1]

class Me:
    def __init__(self):
        self.x = 0
        self.y = 0
        # N = 0, E =1, S=2, W=3
        self.crr_direction = 0
        self.HQ_location = None
        self.locaitions_visited= set()
    
    def walk(self, turn_direction, steps):
        if turn_direction == "R":
            self.crr_direction += 1 if self.crr_direction != 3 else -3
        if turn_direction == "L":
            self.crr_direction -= 1 if self.crr_direction != 0 else -3

        if self.crr_direction == 0:
            for i in range(self.x, self.x+steps):
                self.add_locations(i, self.y)
                # print(i, self.y, end=" | ")
            self.x += steps

        # not
        elif self.crr_direction == 2:
            for i in range( self.x,self.x-steps, -1):
                self.add_locations(i, self.y)
                # print(i, self.y, end=" | ")
            self.x -= steps

        if self.crr_direction == 1:
            for i in range(self.y, self.y+steps):
                self.add_locations(self.x, i)
                # print(self.x, i, end=" | ")
            self.y += steps

        #not
        elif self.crr_direction == 3:
            for i in range( self.y,self.y-steps, -1):
                self.add_locations(self.x, i)
                # print(self.x, i, end=" | ")
            self.y -= steps
        # print()

    def add_locations(self, x,y):
        # print((x, y), end="->")
        if self.HQ_location == None:
            location = (x, y)
            # print(location)
            # print(self.locaitions_visited)
            
            if location not in self.locaitions_visited:
                self.locaitions_visited.add(location)
            else:
                self.HQ_location = {'x':x, 'y':y}

    def get_distance_of_base(self):
        # print('x', self.x)
        # print('y', self.y)
        return abs(self.x) + abs(self.y)
        # print(self.HQ_location)
        return self.locaitions_visited

    def get_HQ_distance(self):
        # return None
        return abs(self.HQ_location['x']) + abs(self.HQ_location['y'])



with open(file_path, 'r') as file:
    line = file.readline()
    line = line.replace(' ', '').strip().split(',')
    me = Me()
    for i in line:
        direction = i[0]
        steps = int(i[1:])
        me.walk(direction, steps)
    print("AnsA:",me.get_distance_of_base()) 
    print("AnsB:",me.get_HQ_distance()) 


