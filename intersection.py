class intersection():
    
    def __init__(self, sched, name, sides, phases):
        self.sched = sched
        self.name = name
        self.sides = sides
        self.phases = phases
        self.cycle_length = 0
        for phase in phases:
            self.cycle_length += phase.length
            
        self.cycle_counter = 0
        
    def cycle(self, tf, event_output):
        
        t = 0
        for j, phase in enumerate(self.phases):
            # A phase consists of up to two sides. This inner loop schedules the departure events for both at the same time
            for i in range(0, len(phase.sides)):
                if self.cycle_counter * self.cycle_length + t < 3600:
                    self.sched.enter(t * tf, 1, phase.sides[i].depart, [self.sched, phase.length, phase.lanes[i], tf, event_output])
            t += phase.length