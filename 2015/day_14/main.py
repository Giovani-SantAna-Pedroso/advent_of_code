import sys

class Reideer:
    def __init__(self, speed, stamina, rest_time):
        self.speed = speed
        self.stamina_initial = stamina
        self.stamina_crr = stamina
        self.rest_time = rest_time
        self.time_to_continue = rest_time 
        self.distance_runned = 0
        self.points = 0 

    def run(self):
        if self.stamina_crr > 0:  # está correndo
            self.distance_runned += self.speed
            self.stamina_crr -= 1
            if self.stamina_crr == 0:
                self.time_to_continue = self.rest_time  # começa o descanso
        else:  # está descansando
            self.time_to_continue -= 1
            if self.time_to_continue == 0:  # descanso acabou, volta a correr
                self.stamina_crr = self.stamina_initial

    def add_point(self):
        self.points += 1

    def get_distance(self):
        return self.distance_runned

    def get_points(self):
        return self.points


time_of_race = int(sys.argv[1])

Comet =  Reideer(14, 10, 127)
Dancer =  Reideer(16, 11, 162)

i_d = 0
c_d = 0
d_d = 0
for i in  range(time_of_race):
    Comet.run()
    Dancer.run()
    distance_c = Comet.get_distance()
    distance_d = Dancer.get_distance()

    max_dist = max(distance_d,distance_c)

    if distance_c == max_dist:
        Comet.add_point()
    if distance_d == max_dist:
        Dancer.add_point()




print("Comet:", Comet.get_distance(), 'Km', Comet.get_points(), "Points")
print("Dancer:", Dancer.get_distance(), 'Km', Dancer.get_points(), "Points")

