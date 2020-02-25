import numpy as np
import math
import TravelTime as tt

avg_travel_delay = [10, 10, 10]

nave_luckie_output = {"North/Luckie S": 0, "North/Luckie N": 0, "North/Luckie E": 0, "North/Luckie W": 0}
nave_techwood_output = {"North/Techwood N": 0, "North/Techwood E": 0, "North/Techwood S": 0, "North/Techwood W": 0}
offramp_output = {"Offramp West": 0, "Offramp East": 0, "Offramp 249": 0}

#Represents one side of an intersection
class side():

    def __init__(self, name, lanes, arrival_distribution, on_boundary, auto_vehicles):
        self.name = name
        #self.intersection = intersection # Points to the intersection this side is a part of (CURRENTLY NO LONGER NEEDED)
        self.lanes = lanes
        self.arrival_distribution = arrival_distribution
        self.destinations = [None, None, None]  # Points to the destination Side after going left, straight, or right, respectively
        self.auto_vehicles = auto_vehicles
        self.on_boundary = on_boundary                
        self.throughput = 0
        
    def depart(self, sched, time, lanes, tf, event_output):
            
        # Number of cars that end up turning in each direction
        l, s, r = 0, 0, 0
        
        # Each lane handles its own queue and keeps track of l/s/r to add to the total here
        for i in lanes:
            a, b, c = self.lanes[i].depart(time)
            l += a
            s += b
            r += c

        if (event_output):
            print("{} cars departed from {} ({} l / {} s / {} r). Queue is now {}".format(l+s+r, self.name, l, s, r, self.queue_to_string()))
            
        self.throughput += l+s+r

        # For each departure direction, if the destination exists in our simulation, schedule the respective arrival event  
        if self.destinations[0] and l > 0:
            travel_time_calculator = tt.TravelTime(self.auto_vehicles)
            travel_time = travel_time_calculator.calculateTravelTime(self.name, self.destinations[0].name, l)
            sched.enter(travel_time * tf, 1, self.destinations[0].arrival, [l, event_output])      
        if self.destinations[1] and s > 0:
            travel_time_calculator = tt.TravelTime(self.auto_vehicles)
            travel_time = travel_time_calculator.calculateTravelTime(self.name, self.destinations[1].name, s)
            sched.enter(travel_time * tf, 1, self.destinations[1].arrival, [s, event_output])
        if self.destinations[2] and r > 0:
            travel_time_calculator = tt.TravelTime(self.auto_vehicles)
            travel_time = travel_time_calculator.calculateTravelTime(self.name, self.destinations[2].name, r)
            sched.enter(travel_time * tf, 1, self.destinations[2].arrival, [r, event_output])

    def arrival(self, cars_incoming, event_output):
    
        # Decide how many incoming cars to queue in each lane

        #new array to stochastically alter arrival distribution
        changed = [0,0,0] # setting to self.arrival_distribution creates a shallow copy and changes it permanently
        #print("{} dist[2] BEFORE: {}".format(self.name, self.arrival_distribution[2]))
        if len(self.arrival_distribution[2]) == 3:
            changed[0] = np.random.normal(self.arrival_distribution[2][0], .05)
            changed[1] = np.random.normal(self.arrival_distribution[2][1], .05)
            changed[2] = 1 - changed[0] - changed[1]
        else:
            changed[0] = np.random.normal(self.arrival_distribution[2][0], .1)
            changed[1] = 1 - changed[0]

        #print("{} dist[2] AFTER: {}".format(self.name, self.arrival_distribution[2]))
        
        total = 0
        for num, lane in enumerate(self.lanes):
            lane.queue += math.ceil(cars_incoming * changed[num])
            total += math.ceil(cars_incoming * changed[num])
        if (event_output):
            print("{} cars arrived at {}. Queue is now {}".format(total, self.name, self.queue_to_string()))
        
    def set_dests(self, destinations):
        self.destinations = destinations
        
    def queue_to_string(self):
        queue = []
        for lane in self.lanes:
            queue.append(lane.queue)
        return queue