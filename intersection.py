class intersection():
    
    def __init__(self, sched, name, sides, phases):
        self.sched = sched
        self.name = name
        self.sides = sides
        self.phases = phases
        self.cycle_length = 0
        for phase in phases:
            self.cycle_length += phase.length
        
    def cycle(self):
        
        t = 0
        for phase in self.phases:
            # A phase consists of up to two sides. This inner loop schedules the departure events for both at the same time
            for i in range(0, len(phase.sides)):
                self.sched.enter(t+phase.length, 1, phase.sides[i].depart, (phase.length, phase.lanes[i]))

            t += phase.length
        
        self.sched.enter(self.cycle_length, 1, self.cycle)