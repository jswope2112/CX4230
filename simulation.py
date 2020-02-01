import sched, time
from lane import lane
from side import side
from intersection import intersection
from phase import phase

class Simulation():

    def __init__(self):
        self.nave_luckie = nave_luckie
        self.nave_techwood = nave_techwood
        self.s = sched.scheduler(time.time, time.sleep)
        s.enter(60, 1, lambda: nave_luckie.cycle(s))
        s.enter(60, 1, lambda: nave_techwood.cycle(s))
        s.run()
        
if __name__ == '__main__':

    #sim = Simulation()
    s = sched.scheduler(time.time, time.sleep)
    
    NAVE_LUCKIE_N_DEP_DISTS = [[1, 0, 0], [0, .5, .5]]
    NAVE_LUCKIE_N_LANES = [lane(NAVE_LUCKIE_N_DEP_DISTS[0]), lane(NAVE_LUCKIE_N_DEP_DISTS[1])]
    NAVE_LUCKIE_N_ARR_DIST = [.5, .5]
    NAVE_LUCKIE_N = side(s, "North/Luckie N", NAVE_LUCKIE_N_LANES, NAVE_LUCKIE_N_ARR_DIST)
   
    NAVE_LUCKIE_E_DEP_DISTS = [[.5, .5, 0], [0, .5, .5]]
    NAVE_LUCKIE_E_LANES = [lane(NAVE_LUCKIE_E_DEP_DISTS[0]), lane(NAVE_LUCKIE_E_DEP_DISTS[1])]
    NAVE_LUCKIE_E_ARR_DIST = [.5, .5]
    NAVE_LUCKIE_E = side(s, "North/Luckie E", NAVE_LUCKIE_E_LANES, NAVE_LUCKIE_E_ARR_DIST)
    
    NAVE_LUCKIE_S_DEP_DISTS = [[1, 0, 0], [0, 1, 0], [0, 1, 0]]
    NAVE_LUCKIE_S_LANES = [lane(NAVE_LUCKIE_S_DEP_DISTS[0]), lane(NAVE_LUCKIE_S_DEP_DISTS[1]), lane(NAVE_LUCKIE_S_DEP_DISTS[2])]
    NAVE_LUCKIE_S_ARR_DIST = [.33, .33, .33]
    NAVE_LUCKIE_S = side(s, "North/Luckie S", NAVE_LUCKIE_S_LANES, NAVE_LUCKIE_S_ARR_DIST)
    
    NAVE_LUCKIE_W_DEP_DISTS = [[1, 0, 0], [0, 1, 0], [0, .5, .5]]
    NAVE_LUCKIE_W_LANES = [lane(NAVE_LUCKIE_W_DEP_DISTS[0]), lane(NAVE_LUCKIE_W_DEP_DISTS[1]), lane(NAVE_LUCKIE_W_DEP_DISTS[2])]
    NAVE_LUCKIE_W_ARR_DIST = [.33, .33, .33]
    NAVE_LUCKIE_W = side(s, "North/Luckie W", NAVE_LUCKIE_W_LANES, NAVE_LUCKIE_W_ARR_DIST)
    
    NAVE_LUCKIE_PHASES = [phase([NAVE_LUCKIE_S],[[0,1,2]],30), #luckie green and arrow
        #luckie green and tech pkwy green
        phase([NAVE_LUCKIE_S,NAVE_LUCKIE_N],[[1,2],[1]],30),
        #tech pkwy green and arrow
        phase([NAVE_LUCKIE_N],[[0,1]],30),
        #nave west green and arrow
        phase([NAVE_LUCKIE_W],[[0,1,2]],30),
        #nave west green and nave east green
        phase([NAVE_LUCKIE_W,NAVE_LUCKIE_E],[[1,2],[1]],30)]
    
    NAVE_LUCKIE = intersection(s, "North/Luckie", [NAVE_LUCKIE_N, NAVE_LUCKIE_E, NAVE_LUCKIE_S, NAVE_LUCKIE_W], NAVE_LUCKIE_PHASES)

    for side in NAVE_LUCKIE.sides:
        print(side.name)
        s.enter(0, 1, side.arrival, [100])
    s.enter(1, 1, lambda: NAVE_LUCKIE.cycle())
    s.run()