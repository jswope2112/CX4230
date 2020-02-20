import numpy as np
import TravelTime as tt

avg_travel_delay = [10, 10, 10]

nave_luckie_output = {"North/Luckie S": 0, "North/Luckie N": 0, "North/Luckie E": 0, "North/Luckie W": 0}
nave_techwood_output = {"North/Techwood N": 0, "North/Techwood E": 0, "North/Techwood S": 0, "North/Techwood W": 0}
offramp_output = {"Offramp West": 0, "Offramp East": 0, "Offramp 249": 0}

#Represents one side of an intersection
class side():

    def __init__(self, sched, name, lanes, arrival_distribution, counter, auto_vehicles = False):
        self.sched = sched
        self.name = name
        #self.intersection = intersection # Points to the intersection this side is a part of (CURRENTLY NO LONGER NEEDED)
        self.lanes = lanes
        self.arrival_distribution = arrival_distribution
        self.destinations = [None, None, None]  # Points to the destination Side after going left, straight, or right, respectively
        self.counter = counter
        self.auto_vehicles = auto_vehicles
        
    def depart(self, time, lanes):
    
        # Number of cars that end up turning in each direction
        l, s, r = 0, 0, 0
        
        # Each lane handles its own queue and keeps track of l/s/r to add to the total here
        for i in lanes:
            a, b, c = self.lanes[i].depart(time)
            l += a
            s += b
            r += c

        print("{} cars departed from {} ({} l / {} s / {} r). Queue is now {}".format(l+s+r, self.name, l, s, r, self.queue_to_string()))
        if self.name[0] == 'O':
            offramp_output[self.name] = offramp_output[self.name] + l + s + r
            print("output of {} is {}".format(self.name[:7], sum(offramp_output.values())))
        elif self.name[6] == 'T':
            nave_techwood_output[self.name] = nave_techwood_output[self.name] + l + s + r
            print("output of {} is {}".format(self.name[:14], sum(nave_techwood_output.values())))
        else:
            nave_luckie_output[self.name] = nave_luckie_output[self.name] + l + s + r
            print("output of {} is {}".format(self.name[:12], sum(nave_luckie_output.values())))
        
        
        # For each departure direction, if the destination exists in our simulation, schedule the respective arrival event     
        if self.destinations[0] and l > 0:
            travel_time_calculator = tt.TravelTime(self.auto_vehicles)
            travel_time = travel_time_calculator.calculateTravelTime(self.name, self.destinations[0].name, l)
            self.sched.enter(travel_time, 1, self.destinations[0].arrival, [l])      
        if self.destinations[1] and s > 0:
            travel_time_calculator = tt.TravelTime(self.auto_vehicles)
            travel_time = travel_time_calculator.calculateTravelTime(self.name, self.destinations[1].name, s)
            self.sched.enter(travel_time, 1, self.destinations[1].arrival, [s])
        if self.destinations[2] and r > 0:
            travel_time_calculator = tt.TravelTime(self.auto_vehicles)
            travel_time = travel_time_calculator.calculateTravelTime(self.name, self.destinations[2].name, r)
            self.sched.enter(travel_time, 1, self.destinations[2].arrival, [r])

    def arrival(self, cars_incoming):
    
        # Decide how many incoming cars to queue in each lane
        # TODO: Make this draw stochastically from arrival_distribution

        #new array to stochastically alter arrival distribution
        changed = self.arrival_distribution
        if len(self.arrival_distribution) == 3:
            changed[0] = np.random.normal(self.arrival_distribution[0], .05)
            changed[1] = np.random.normal(self.arrival_distribution[1], .05)
            changed[2] = 1 - changed[0] - changed[1]
        else:
            changed[0] = np.random.normal(self.arrival_distribution[0], .1)
            changed[1] = 1 - changed[0]

        for num, lane in enumerate(self.lanes):
            lane.queue += int(cars_incoming * changed[num])
        
        print("{} cars arrived at {}. Queue is now {}".format(cars_incoming, self.name, self.queue_to_string()))


    def nave_luckie_dist(self):
        if self.counter == 0:
            return int(np.random.normal(8, 1))
        if self.counter == 1:
            return int(np.random.normal(5, 1))
        if self.counter == 2:
            return int(np.random.normal(16, 2))
        if self.counter == 3:
            return int(np.random.normal(13, 2))


    def nave_techwood_dist(self):
        if self.counter == 0:
            return int(np.random.normal(5, 1))
        if self.counter == 1:
            return int(np.random.normal(16, 2))
        if self.counter == 2:
            return int(np.random.normal(2, 1))
        if self.counter == 3:
            return int(np.random.normal(13, 2))

    def offramp_dist(self):
        if self.counter == 0:
            return int(np.random.normal(6, 1))
        if self.counter == 1:
            return int(np.random.normal(13, 2))
        if self.counter == 2:
            return int(np.random.normal(16, 2))
        
    def set_dests(self, destinations):
        self.destinations = destinations
        
    def queue_to_string(self):
        queue = []
        for lane in self.lanes:
            queue.append(lane.queue)
        return queue