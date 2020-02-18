import numpy as numpy

class TravelTime():
    
    #Base limit is 45mph, we assume most drivers go over this limit
    adjustedSpeedLimit = 50
    
    #assumptions about more cars driving == more delays
    avg_added_delay_per_car = 0.5
    std_per_car = 0.25
    
    travel_destinations = [
            [("North/Luckie","North/Techwood"), 1270],
            [("North/Techwood","Offramp"), 406],
            [("North/Techwood","North/Luckie"), 1270],
            [("Offramp","North/Techwood"), 406]
            ]
        
    def __init__(self, auto_vehicles = False):
        self.auto_vehicles = auto_vehicles
        
        
    def calculateTravelTime(self, start, destination, num_cars):
        if (start is None or destination is None):
            return 0
        distancekey = (start.split()[0], destination.split()[0])
        distance = 0
        
        for travel_destination in self.travel_destinations:
            if distancekey == travel_destination[0]:
                distance = travel_destination[1]
                break
        
        #something went wrong if the distance is 0
        if distance == 0:
            return "Error"
        
        base_travel_time = average_travel_time(distance, self.adjustedSpeedLimit)
        
        #If there are no autonomous vehicles, we do not add extra delay due to more vehicles
        if (not self.auto_vehicles):
            added_delay = numpy.random.normal(self.avg_added_delay_per_car, self.std_per_car, num_cars)
            total_added_delay = sum(x for x in added_delay if x > 0)
            base_travel_time += total_added_delay
        
        return round(base_travel_time, 2)
        
        
#The formula used for distance traveled while accelerating or decelerating is
#d = vt + 0.5*a*t^2 (kinematic equation)
#Deceleration + reaction times source : https://nacto.org/docs/usdg/vehicle_stopping_distance_and_time_upenn.pdf
#Acceleration source : https://hypertextbook.com/facts/2001/MeredithBarricella.shtml
def average_travel_time(distance, mph_speed):
    assumed_acceleration_m_s = 3.5
    fps_speed = 1.467 * mph_speed
    assumed_acceleration_fps = 3.28 * assumed_acceleration_m_s
    assumed_deceleration_fps = 15
    assumed_reaction_recognition_time = 2
    
    stopping_time = fps_speed/assumed_deceleration_fps
    stopping_distance = fps_speed * stopping_time - 0.5 * assumed_deceleration_fps * stopping_time ** 2
    
    acceleration_time = fps_speed/assumed_acceleration_fps + assumed_reaction_recognition_time
    acceleration_distance = 0.5 * assumed_acceleration_fps * acceleration_time ** 2
    
    rest_of_distance = distance - stopping_distance - acceleration_distance
    
    #if the rest of the distance is too short, this algorithm doesn't work as
    #there was not enough time to accelerate to full speed, so we recursively
    #call this algorithm until we determine a new "top" speed works
    if (rest_of_distance < 0):
        return average_travel_time(distance, mph_speed - 1)
    
    rest_of_distance_time = rest_of_distance / fps_speed
    
    total_time = stopping_time + acceleration_time + rest_of_distance_time
    
    return total_time