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
        for phase in self.phases:
            # A phase consists of up to two sides. This inner loop schedules the departure events for both at the same time
            for i in range(0, len(phase.sides)):
                if self.cycle_counter * self.cycle_length + t + phase.length < 3600:
                    self.sched.enter((t+phase.length) * tf, 1, phase.sides[i].depart, [self.sched, phase.length, phase.lanes[i], tf, event_output])
            t += phase.length
            
        self.cycle_counter += 1
        if self.cycle_counter * self.cycle_length + self.cycle_length < 3600:
            self.sched.enter(self.cycle_length * tf, 1, self.cycle, [tf, event_output])