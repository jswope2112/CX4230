import numpy as np

avg_travel_delay = [10, 10, 10]

#Represents one side of an intersection
class side():

    def __init__(self, sched, name, lanes, arrival_distribution, counter):
        self.sched = sched
        self.name = name
        #self.intersection = intersection # Points to the intersection this side is a part of (CURRENTLY NO LONGER NEEDED)
        self.lanes = lanes
        self.arrival_distribution = arrival_distribution
        self.destinations = [None, None, None]  # Points to the destination Side after going left, straight, or right, respectively
        self.counter = counter
        
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
        
        # For each departure direction, if the destination exists in our simulation, schedule the respective arrival event     
        if self.destinations[0] and l > 0:
            self.sched.enter(avg_travel_delay[0], 1, self.destinations[0].arrival, [l])           
        if self.destinations[1] and s > 0:
            self.sched.enter(avg_travel_delay[1], 1, self.destinations[1].arrival, [s])
        if self.destinations[2] and r > 0:
            self.sched.enter(avg_travel_delay[2], 1, self.destinations[2].arrival, [r])

    def arrival(self, cars_incoming):
    
        # Decide how many incoming cars to queue in each lane
        # TODO: Make this draw stochastically from arrival_distribution
        for lane in self.lanes:
            lane.queue += cars_incoming // len(self.lanes)
        
        print("{} cars arrived at {}. Queue is now {}".format(cars_incoming, self.name, self.queue_to_string()))

    def nave_luckie_dist(self):
        if self.counter == 0:
            return int(np.random.normal(451, 25))
        if self.counter == 1:
            return int(np.random.normal(299, 25))
        if self.counter == 2:
            return int(np.random.normal(953, 50))
        if self.counter == 3:
            return int(np.random.normal(800, 50))


    def nave_techwood_dist(self):
        if self.counter == 0:
            return int(np.random.normal(317, 25))
        if self.counter == 1:
            return int(np.random.normal(953, 25))
        if self.counter == 2:
            return int(np.random.normal(108, 50))
        if self.counter == 3:
            return int(np.random.normal(800, 50))

    def offramp_dist(self):
        if self.counter == 0:
            return int(np.random.normal(344, 25))
        if self.counter == 1:
            return int(np.random.normal(800, 50))
        if self.counter == 2:
            return int(np.random.normal(953, 50))
        
    def set_dests(self, destinations):
        self.destinations = destinations
        
    def queue_to_string(self):
        queue = []
        for lane in self.lanes:
            queue.append(lane.queue)
        return queue