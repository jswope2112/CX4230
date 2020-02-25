import numpy as np

avg_reaction_delay = 2.3
std_reaction_delay = 0.46
avg_travel_delay = 2
std_travel_delay = 0.45


class lane():

    def __init__(self, departure_distribution, auto_vehicles):
        self.queue = 0
        self.departure_distribution = departure_distribution
        self.auto_vehicles = auto_vehicles
        
    def depart(self, time_allowed):
    
        l, s, r, time = 0, 0, 0, 0
        
        while self.queue > 0:
            if time > time_allowed:
                #print("right, left, straight", (right_counter, left_counter,straight_counter))
                return l, s, r
            
            #we assume average  reaction delay as a normal random variable
            #if there are autonomous vehicles, there are no reaction delays
            if (self.auto_vehicles):
                reaction_delay = 0
            else:
                reaction_delay = np.random.normal(avg_reaction_delay, std_reaction_delay)
            decision = self.get_car_decision()
            
            if decision == "l":
                travel_delay = np.random.normal(avg_travel_delay, std_travel_delay)
                l += 1
                time += reaction_delay + travel_delay
            elif decision == "s":
                travel_delay = np.random.normal(avg_travel_delay, std_travel_delay)
                s += 1
                time += reaction_delay + travel_delay
            else:
                travel_delay = np.random.normal(avg_travel_delay, std_travel_delay)
                r += 1
                time += reaction_delay + travel_delay
            
            self.queue -= 1
            
        #print("right, left, straight", (right_counter, left_counter,straight_counter))
        #print("time elapsed", time)
        return l, s, r


    def get_car_decision(self):
        
        # generate a uniform random variable to determine which way the car is going
        random_num = np.random.uniform()

        for idx, val in enumerate(self.departure_distribution):
            if random_num < val:
                if idx == 0:
                    return "l"
                if idx == 1:
                    return "s"
                if idx == 2:
                    return "r"
