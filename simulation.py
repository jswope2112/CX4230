import sched, time
from lane import lane
from side import side
from intersection import intersection
from phase import phase

s = sched.scheduler(time.time, time.sleep)

#####################################################################
# NORTH AVE / TECHWOOD PARAMETERS 
#####################################################################
NAVE_TECHWOOD_N_DEP_DISTS = [[1, 0, 0], [0, .5, 1]]
NAVE_TECHWOOD_N_LANES = [lane(NAVE_TECHWOOD_N_DEP_DISTS[0]), lane(NAVE_TECHWOOD_N_DEP_DISTS[1])]
NAVE_TECHWOOD_N_ARR_DIST = [.5, .5]
NAVE_TECHWOOD_N = side(s, "North/Techwood N", NAVE_TECHWOOD_N_LANES, NAVE_TECHWOOD_N_ARR_DIST, 0)

NAVE_TECHWOOD_E_DEP_DISTS = [[1, 0, 0], [0, 1, 0], [0, .5, 1]]
NAVE_TECHWOOD_E_LANES = [lane(NAVE_TECHWOOD_E_DEP_DISTS[0]), lane(NAVE_TECHWOOD_E_DEP_DISTS[1]), lane(NAVE_TECHWOOD_E_DEP_DISTS[2])]
NAVE_TECHWOOD_E_ARR_DIST = [.33, .33, .33]
NAVE_TECHWOOD_E = side(s, "North/Techwood E", NAVE_TECHWOOD_E_LANES, NAVE_TECHWOOD_E_ARR_DIST, 2)

NAVE_TECHWOOD_S_DEP_DISTS = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
NAVE_TECHWOOD_S_LANES = [lane(NAVE_TECHWOOD_S_DEP_DISTS[0]), lane(NAVE_TECHWOOD_S_DEP_DISTS[1]), lane(NAVE_TECHWOOD_S_DEP_DISTS[2])]
NAVE_TECHWOOD_S_ARR_DIST = [.33, .33, .33]
NAVE_TECHWOOD_S = side(s, "North/Techwood S", NAVE_TECHWOOD_S_LANES, NAVE_TECHWOOD_S_ARR_DIST, 1)

NAVE_TECHWOOD_W_DEP_DISTS = [[1, 0, 0], [0, 1, 0], [0, .5, 1]]
NAVE_TECHWOOD_W_LANES = [lane(NAVE_TECHWOOD_W_DEP_DISTS[0]), lane(NAVE_TECHWOOD_W_DEP_DISTS[1]), lane(NAVE_TECHWOOD_W_DEP_DISTS[2])]
NAVE_TECHWOOD_W_ARR_DIST = [.33, .33, .33]
NAVE_TECHWOOD_W = side(s, "North/Techwood W", NAVE_TECHWOOD_W_LANES, NAVE_TECHWOOD_W_ARR_DIST, 3)

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

#####################################################################    
# NORTH AVE / LUCKIE ST PARAMETERS 
#####################################################################    
NAVE_LUCKIE_N_DEP_DISTS = [[1, 0, 0], [0, .5, 1]]
NAVE_LUCKIE_N_LANES = [lane(NAVE_LUCKIE_N_DEP_DISTS[0]), lane(NAVE_LUCKIE_N_DEP_DISTS[1])]
NAVE_LUCKIE_N_ARR_DIST = [.5, .5]
NAVE_LUCKIE_N = side(s, "North/Luckie N", NAVE_LUCKIE_N_LANES, NAVE_LUCKIE_N_ARR_DIST, 0)

NAVE_LUCKIE_E_DEP_DISTS = [[.5, .5, 0], [0, .5, 1]]
NAVE_LUCKIE_E_LANES = [lane(NAVE_LUCKIE_E_DEP_DISTS[0]), lane(NAVE_LUCKIE_E_DEP_DISTS[1])]
NAVE_LUCKIE_E_ARR_DIST = [.5, .5]
NAVE_LUCKIE_E = side(s, "North/Luckie E", NAVE_LUCKIE_E_LANES, NAVE_LUCKIE_E_ARR_DIST, 1)

NAVE_LUCKIE_S_DEP_DISTS = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
NAVE_LUCKIE_S_LANES = [lane(NAVE_LUCKIE_S_DEP_DISTS[0]), lane(NAVE_LUCKIE_S_DEP_DISTS[1]), lane(NAVE_LUCKIE_S_DEP_DISTS[2])]
NAVE_LUCKIE_S_ARR_DIST = [.33, .33, .33]
NAVE_LUCKIE_S = side(s, "North/Luckie S", NAVE_LUCKIE_S_LANES, NAVE_LUCKIE_S_ARR_DIST, 2)

NAVE_LUCKIE_W_DEP_DISTS = [[1, 0, 0], [0, 1, 0], [0, .5, 1]]
NAVE_LUCKIE_W_LANES = [lane(NAVE_LUCKIE_W_DEP_DISTS[0]), lane(NAVE_LUCKIE_W_DEP_DISTS[1]), lane(NAVE_LUCKIE_W_DEP_DISTS[2])]
NAVE_LUCKIE_W_ARR_DIST = [.33, .33, .33]
NAVE_LUCKIE_W = side(s, "North/Luckie W", NAVE_LUCKIE_W_LANES, NAVE_LUCKIE_W_ARR_DIST, 3)

NAVE_LUCKIE_PHASES = [phase([NAVE_LUCKIE_S],[[0,1,2]],30), #luckie green and arrow
    #luckie green and tech pkwy green
    phase([NAVE_LUCKIE_S,NAVE_LUCKIE_N],[[1,2],[1]],30),
    #tech pkwy green and arrow
    phase([NAVE_LUCKIE_N],[[0,1]],30),
    #nave west green and arrow
    phase([NAVE_LUCKIE_W],[[0,1,2]],30),
    #nave west green and nave east green
    phase([NAVE_LUCKIE_W,NAVE_LUCKIE_E],[[1,2],[1]],30)]

#####################################################################    
# Off-Ramp PARAMETERS 
#####################################################################
OFFRAMP_249_DEP_DISTS = [[1,0,0],[0.5,0,1]]
OFFRAMP_249_LANES = [lane(OFFRAMP_249_DEP_DISTS[0]), lane(OFFRAMP_249_DEP_DISTS[1])]
OFFRAMP_249_ARR_DIST = [0.5,0.5]
OFFRAMP_249 = side(s, "OFFRAMP 249", OFFRAMP_249_LANES, OFFRAMP_249_ARR_DIST, 0)

OFFRAMP_WEST_DEP_DIST=[[0,1,0], [0,1,0]]
OFFRAMP_WEST_LANES = [lane(OFFRAMP_WEST_DEP_DIST[0]), lane(OFFRAMP_WEST_DEP_DIST[1])]
OFFRAMP_WEST_ARR_DIST = [0.5,0.5]
OFFRAMP_WEST = side(s, "Offramp West", OFFRAMP_WEST_LANES, OFFRAMP_WEST_ARR_DIST, 1)

OFFRAMP_EAST_DEP_DIST=[[0,1,0], [0,1,0]]
OFFRAMP_EAST_LANES = [lane(OFFRAMP_EAST_DEP_DIST[0]), lane(OFFRAMP_EAST_DEP_DIST[1])]
OFFRAMP_EAST_ARR_DIST = [0.5,0.5]
OFFRAMP_EAST = side(s, "Offramp East", OFFRAMP_EAST_LANES, OFFRAMP_EAST_ARR_DIST, 2)

OFFRAMP_PHASES = [phase([OFFRAMP_WEST, OFFRAMP_EAST],[[0,1], [0,1]], 30), #Nave e and Nave w green light
                  #off-ramp green lights
                  phase([OFFRAMP_249], [[0,1]],30)]


        
class Simulation():

    def __init__(self):
        self.nave_luckie = nave_luckie
        self.nave_techwood = nave_techwood
        self.offramp = offramp
        self.s = sched.scheduler(time.time, time.sleep)
        s.enter(60, 1, lambda: nave_luckie.cycle(s))
        s.enter(60, 1, lambda: nave_techwood.cycle(s))
        s.enter(60, 1, lambda: offramp.cycles(s))
        s.run()
        
if __name__ == '__main__':
    
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
    
    for side in nave_luckie.sides:
        s.enter(0, 1, side.arrival, [side.nave_luckie_dist()])
    s.enter(5, 1, lambda: nave_luckie.cycle())
    for side in nave_techwood.sides:
        s.enter(1, 1, side.arrival, [side.nave_techwood_dist()])
    s.enter(10, 1, lambda: nave_techwood.cycle())
    for side in offramp.sides:
        s.enter(0,1,side.arrival,[side.offramp_dist()])
    s.enter(15, 1, lambda: offramp.cycle())
    s.run()