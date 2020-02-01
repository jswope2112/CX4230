# Represents a single phase of traffic on a given Side of an Intersection
class phase:

    def __init__(self, sides, lanes, length):
        self.sides = sides
        self.lanes = lanes
        self.length = length