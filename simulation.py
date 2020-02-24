import sched, time
import numpy as np
from lane import lane
from side import side
from intersection import intersection
from phase import phase

AUTO_VEHICLES = False
SIM_TIME = 3600
NUM_SIDES = 11

#####################################################################
# NORTH AVE / TECHWOOD PARAMETERS 
#####################################################################
NAVE_TECHWOOD_N_DEP_DISTS = [[1, 0, 0], [0, .5, 1]]
NAVE_TECHWOOD_N_LANES = [lane(NAVE_TECHWOOD_N_DEP_DISTS[0],AUTO_VEHICLES), lane(NAVE_TECHWOOD_N_DEP_DISTS[1],AUTO_VEHICLES)]
NAVE_TECHWOOD_N_ARR_DIST = [5, 1, [.5, .5]]

NAVE_TECHWOOD_E_DEP_DISTS = [[1, 0, 0], [0, 1, 0], [0, .5, 1]]
NAVE_TECHWOOD_E_LANES = [lane(NAVE_TECHWOOD_E_DEP_DISTS[0],AUTO_VEHICLES), lane(NAVE_TECHWOOD_E_DEP_DISTS[1],AUTO_VEHICLES), lane(NAVE_TECHWOOD_E_DEP_DISTS[2],AUTO_VEHICLES)]
NAVE_TECHWOOD_E_ARR_DIST = [16, 2, [.33, .33, .33]]

NAVE_TECHWOOD_S_DEP_DISTS = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
NAVE_TECHWOOD_S_LANES = [lane(NAVE_TECHWOOD_S_DEP_DISTS[0], AUTO_VEHICLES), lane(NAVE_TECHWOOD_S_DEP_DISTS[1],AUTO_VEHICLES), lane(NAVE_TECHWOOD_S_DEP_DISTS[2],AUTO_VEHICLES)]
NAVE_TECHWOOD_S_ARR_DIST = [2, 1, [.33, .33, .33]]

NAVE_TECHWOOD_W_DEP_DISTS = [[1, 0, 0], [0, 1, 0], [0, .5, 1]]
NAVE_TECHWOOD_W_LANES = [lane(NAVE_TECHWOOD_W_DEP_DISTS[0],AUTO_VEHICLES), lane(NAVE_TECHWOOD_W_DEP_DISTS[1],AUTO_VEHICLES), lane(NAVE_TECHWOOD_W_DEP_DISTS[2],AUTO_VEHICLES)]
NAVE_TECHWOOD_W_ARR_DIST = [13, 2, [.33, .33, .33]]



#####################################################################    
# NORTH AVE / LUCKIE ST PARAMETERS 
#####################################################################    
NAVE_LUCKIE_N_DEP_DISTS = [[1, 0, 0], [0, .5, 1]]
NAVE_LUCKIE_N_LANES = [lane(NAVE_LUCKIE_N_DEP_DISTS[0],AUTO_VEHICLES), lane(NAVE_LUCKIE_N_DEP_DISTS[1],AUTO_VEHICLES)]
NAVE_LUCKIE_N_ARR_DIST = [8, 1, [.5, .5]]

NAVE_LUCKIE_E_DEP_DISTS = [[.5, .5, 0], [0, .5, 1]]
NAVE_LUCKIE_E_LANES = [lane(NAVE_LUCKIE_E_DEP_DISTS[0],AUTO_VEHICLES), lane(NAVE_LUCKIE_E_DEP_DISTS[1],AUTO_VEHICLES)]
NAVE_LUCKIE_E_ARR_DIST = [5, 1, [.5, .5]]

NAVE_LUCKIE_S_DEP_DISTS = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
NAVE_LUCKIE_S_LANES = [lane(NAVE_LUCKIE_S_DEP_DISTS[0],AUTO_VEHICLES), lane(NAVE_LUCKIE_S_DEP_DISTS[1],AUTO_VEHICLES), lane(NAVE_LUCKIE_S_DEP_DISTS[2],AUTO_VEHICLES)]
NAVE_LUCKIE_S_ARR_DIST = [16, 2, [.33, .33, .33]]

NAVE_LUCKIE_W_DEP_DISTS = [[1, 0, 0], [0, 1, 0], [0, .5, 1]]
NAVE_LUCKIE_W_LANES = [lane(NAVE_LUCKIE_W_DEP_DISTS[0],AUTO_VEHICLES), lane(NAVE_LUCKIE_W_DEP_DISTS[1],AUTO_VEHICLES), lane(NAVE_LUCKIE_W_DEP_DISTS[2],AUTO_VEHICLES)]
NAVE_LUCKIE_W_ARR_DIST = [13, 2, [.33, .33, .33]]


#####################################################################    
# Off-Ramp PARAMETERS 
#####################################################################
OFFRAMP_249_DEP_DISTS = [[1,0,0],[0.5,0,1]]
OFFRAMP_249_LANES = [lane(OFFRAMP_249_DEP_DISTS[0],AUTO_VEHICLES), lane(OFFRAMP_249_DEP_DISTS[1],AUTO_VEHICLES)]
OFFRAMP_249_ARR_DIST = [6, 1, [0.5,0.5]]

OFFRAMP_WEST_DEP_DIST=[[0,1,0], [0,1,0]]
OFFRAMP_WEST_LANES = [lane(OFFRAMP_WEST_DEP_DIST[0],AUTO_VEHICLES), lane(OFFRAMP_WEST_DEP_DIST[1],AUTO_VEHICLES)]
OFFRAMP_WEST_ARR_DIST = [13, 2, [0.5,0.5]]

OFFRAMP_EAST_DEP_DIST=[[0,1,0], [0,1,0]]
OFFRAMP_EAST_LANES = [lane(OFFRAMP_EAST_DEP_DIST[0],AUTO_VEHICLES), lane(OFFRAMP_EAST_DEP_DIST[1],AUTO_VEHICLES)]
OFFRAMP_EAST_ARR_DIST = [16, 2, [0.5,0.5]]

        
class Simulation():

    def __init__(self, time_factor, event_output, smart_lights, smart_cars, iterations):
    
        self.s = sched.scheduler(time.time, time.sleep)
        
        NAVE_LUCKIE_N = side("North/Luckie N", NAVE_LUCKIE_N_LANES, NAVE_LUCKIE_N_ARR_DIST, 0,AUTO_VEHICLES)
        NAVE_LUCKIE_E = side("North/Luckie E", NAVE_LUCKIE_E_LANES, NAVE_LUCKIE_E_ARR_DIST, 1,AUTO_VEHICLES)
        NAVE_LUCKIE_S = side("North/Luckie S", NAVE_LUCKIE_S_LANES, NAVE_LUCKIE_S_ARR_DIST, 2,AUTO_VEHICLES)
        NAVE_LUCKIE_W = side("North/Luckie W", NAVE_LUCKIE_W_LANES, NAVE_LUCKIE_W_ARR_DIST, 3,AUTO_VEHICLES)
        
        NAVE_LUCKIE_PHASES = [phase([NAVE_LUCKIE_S],[[0,1,2]],30), #luckie green and arrow
            #luckie green and tech pkwy green
            phase([NAVE_LUCKIE_S,NAVE_LUCKIE_N],[[1,2],[1]],30),
            #tech pkwy green and arrow
            phase([NAVE_LUCKIE_N],[[0,1]],30),
            #nave west green and arrow
            phase([NAVE_LUCKIE_W],[[0,1,2]],30),
            #nave west green and nave east green
            phase([NAVE_LUCKIE_W,NAVE_LUCKIE_E],[[1,2],[1]],30)]
            
        NAVE_TECHWOOD_N = side("North/Techwood N", NAVE_TECHWOOD_N_LANES, NAVE_TECHWOOD_N_ARR_DIST, 0, AUTO_VEHICLES)
        NAVE_TECHWOOD_E = side("North/Techwood E", NAVE_TECHWOOD_E_LANES, NAVE_TECHWOOD_E_ARR_DIST, 2)
        NAVE_TECHWOOD_S = side("North/Techwood S", NAVE_TECHWOOD_S_LANES, NAVE_TECHWOOD_S_ARR_DIST, 1,AUTO_VEHICLES)
        NAVE_TECHWOOD_W = side("North/Techwood W", NAVE_TECHWOOD_W_LANES, NAVE_TECHWOOD_W_ARR_DIST, 3,AUTO_VEHICLES)
        
        NAVE_TECHWOOD_PHASES = [phase([NAVE_TECHWOOD_S],[[0,1,2]],30), #techwood South arrow and green
            #techwood S and Techwood N green
            phase([NAVE_TECHWOOD_S,NAVE_TECHWOOD_N],[[1,2],[1]],30),
            #techwood N green and arrow
            phase([NAVE_TECHWOOD_N],[[0,1]],30),
            #Nave W green and arrow
            phase([NAVE_TECHWOOD_W],[[0,1,2]],30),
            #Nav W and Nave E Green
            phase([NAVE_TECHWOOD_W,NAVE_TECHWOOD_E],[[1,2],[1]],30),
            #Nave E green and arrow 
            phase([NAVE_TECHWOOD_E],[[0,1,2]],30)]

    
        OFFRAMP_249 = side("Offramp 249", OFFRAMP_249_LANES, OFFRAMP_249_ARR_DIST, 0,AUTO_VEHICLES)
        OFFRAMP_WEST = side("Offramp West", OFFRAMP_WEST_LANES, OFFRAMP_WEST_ARR_DIST, 1,AUTO_VEHICLES)
        OFFRAMP_EAST = side("Offramp East", OFFRAMP_EAST_LANES, OFFRAMP_EAST_ARR_DIST, 2,AUTO_VEHICLES)

        OFFRAMP_PHASES = [phase([OFFRAMP_WEST, OFFRAMP_EAST],[[0,1], [0,1]], 30), #Nave e and Nave w green light
            #off-ramp green lights
            phase([OFFRAMP_249], [[0,1]],30)]
                  
        # set up intersections
        nave_luckie = intersection(self.s, "North/Luckie", [NAVE_LUCKIE_N, NAVE_LUCKIE_E, NAVE_LUCKIE_S, NAVE_LUCKIE_W], NAVE_LUCKIE_PHASES)
        nave_techwood = intersection(self.s, "North/Techwood", [NAVE_TECHWOOD_N, NAVE_TECHWOOD_E, NAVE_TECHWOOD_S, NAVE_TECHWOOD_W], NAVE_TECHWOOD_PHASES)
        offramp = intersection(self.s, "Offramp", [OFFRAMP_249, OFFRAMP_EAST, OFFRAMP_WEST], OFFRAMP_PHASES)
        
        
        # interconnect them by setting destinations
        nave_luckie.sides[0].set_dests([nave_techwood.sides[3], None, None])
        nave_luckie.sides[2].set_dests([None, None, nave_techwood.sides[3]])
        nave_luckie.sides[3].set_dests([None, nave_techwood.sides[3], None])
        nave_techwood.sides[0].set_dests([offramp.sides[2], None, nave_luckie.sides[1]])
        nave_techwood.sides[1].set_dests([None, nave_luckie.sides[1], None])
        nave_techwood.sides[2].set_dests([nave_luckie.sides[1], None, offramp.sides[2]])
        nave_techwood.sides[3].set_dests([None,offramp.sides[2],None])
        offramp.sides[0].set_dests([None, None, nave_techwood.sides[1]])
        offramp.sides[1].set_dests([None, nave_techwood.sides[1], None])
        offramp.sides[2].set_dests([None, None, None])
        
        intersections = [nave_luckie, nave_techwood, offramp]
        
        self.intersections = intersections
        self.event_output = event_output
        self.time_factor = time_factor
        self.smart_lights = smart_lights
        self.smart_cars = smart_cars
        self.iterations = iterations
        
        self.auto_cycle_counter = 0
       

    def run(self):
        
        self.auto_arrivals()
        
        t = 0
        for intersection in self.intersections:
            self.s.enter(t * self.time_factor, 1, intersection.cycle, [self.time_factor, self.event_output])
            t += 5
        self.s.run()
        
    def auto_arrivals(self):
        t = 0
        for intersection in self.intersections:
            for side in intersection.sides:
                if side.on_boundary:
                    self.s.enter(t * self.time_factor, 1, side.arrival, [int(np.random.normal(side.arrival_distribution[0], side.arrival_distribution[1])), self.event_output])
                    t += 1
        if (self.event_output):
            print("****************** 05:{} PM ******************".format(self.auto_cycle_counter))
        self.auto_cycle_counter += 1
        if self.auto_cycle_counter < 60:
            self.s.enter(60 * self.time_factor, 1, lambda: self.auto_arrivals())
            
    def get_results(self):
        results = []
        for intersection in self.intersections:
            for side in intersection.sides:
                results.append(side.throughput) 
        return results
                
    def print_results(self):
        for intersection in self.intersections:
            for side in intersection.sides:
                print("{}: {}".format(side.name, side.throughput))


        
if __name__ == '__main__':

    results = np.zeros((10, NUM_SIDES))
    for i in range(0, 10):
        sim = Simulation(.0001, False, False, False, SIM_TIME)
        sim.run()
        print("SIMULATION {} THROUGHPUT RESULTS".format(i+1))
        sim.print_results()
        results[i] = sim.get_results()
        
    j = 0
    for intersection in sim.intersections:
            for side in intersection.sides:
                print("{}: {} MEAN: {} STDV: {}".format(side.name, results[:,j], np.mean(results[:,j]), np.std(results[:,j])))
                j += 1
    
'''    
    nave_luckie = intersection(s, "North/Luckie", [NAVE_LUCKIE_N, NAVE_LUCKIE_E, NAVE_LUCKIE_S, NAVE_LUCKIE_W], NAVE_LUCKIE_PHASES)
    nave_techwood = intersection(s, "North/Techwood", [NAVE_TECHWOOD_N, NAVE_TECHWOOD_E, NAVE_TECHWOOD_S, NAVE_TECHWOOD_W], NAVE_TECHWOOD_PHASES)
    offramp = intersection(s, "Offramp", [OFFRAMP_249, OFFRAMP_EAST, OFFRAMP_WEST], OFFRAMP_PHASES)
    
    nave_luckie.sides[0].set_dests([nave_techwood.sides[3], None, None])
    nave_luckie.sides[2].set_dests([None, None, nave_techwood.sides[3]])
    nave_luckie.sides[3].set_dests([None, nave_techwood.sides[3], None])

    nave_techwood.sides[0].set_dests([offramp.sides[2], None, nave_luckie.sides[1]])
    nave_techwood.sides[1].set_dests([None, nave_luckie.sides[1], None])
    nave_techwood.sides[2].set_dests([nave_luckie.sides[1], None, offramp.sides[2]])
    nave_techwood.sides[3].set_dests([None,offramp.sides[2],None])
    
    offramp.sides[0].set_dests([None, None, nave_techwood.sides[1]])
    offramp.sides[1].set_dests([None, nave_techwood.sides[1], None])
    offramp.sides[2].set_dests([None, None, None])
    
    intersections = [nave_luckie, nave_techwood, offramp]
    
    for intersection in intersections:
        for side in intersection.sides:
            print("{} dist[2]: {}".format(side.name, side.arrival_distribution[2]))
    
    
    #for side in nave_luckie.sides:
    #    s.enter(0, 1, side.arrival, [side.nave_luckie_dist()])
    s.enter(5, 1, lambda: nave_luckie.cycle())
    #for side in nave_techwood.sides:
    #    s.enter(1, 1, side.arrival, [side.nave_techwood_dist()])
    s.enter(10, 1, lambda: nave_techwood.cycle())
    #for side in offramp.sides:
    #    s.enter(0,1,side.arrival,[side.offramp_dist()])
    s.enter(15, 1, lambda: offramp.cycle())
    s.run()
'''    
    
