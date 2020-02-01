import numpy as np

avg_reaction_delay = 0.5
std_reaction_delay = 0.25
avg_travel_delay = 0.75


class lane():

    def __init__(self, departure_distribution):
        self.queue = 0
        self.departure_distribution = departure_distribution
        
    def depart(self, time_allowed):
    
        l, s, r, time = 0, 0, 0, 0
        
        while self.queue > 0:
            if time > time_allowed:
                #print("right, left, straight", (right_counter, left_counter,straight_counter))
                return l, s, r
            
            #we assume average  reaction delay as a normal random variable
            reaction_delay = np.random.normal(avg_reaction_delay, std_reaction_delay)
            decision = self.get_car_decision()
            
            #our calculation of travel_delay varies per lane
            #currently calculated by how many cars are before a vehicle * a factor
            #i.e. on a two straight lane road, the third (overall) car is only behind
            #one car, the same goes for the fourth.
            #this assumes people fill in lanes about evenly
            #TODO: obviously cars in the back should have a higher multiplicative effect
            if decision == "l":
                travel_delay = avg_travel_delay * l
                l += 1
                time += reaction_delay + travel_delay
            elif decision == "s":
                travel_delay = avg_travel_delay * s
                s += 1
                time += reaction_delay + travel_delay
            else:
                travel_delay = avg_travel_delay * r
                r += 1
                time += reaction_delay + travel_delay
            
            self.queue -= 1
            
        #print("right, left, straight", (right_counter, left_counter,straight_counter))
        #print("time elapsed", time)
        return l, s, r


    def get_car_decision(self):
        
        # generate a uniform random variable to determine which way the car is going
        # TODO: base this off real data from the intersection (departure_distribution)
        
        random_num = np.random.uniform()
        if random_num < 0.2:
            return "l"
        if random_num < 0.8:
            return "s"
        else:
            return "r"