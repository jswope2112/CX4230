#car removal from queue should take into account propagation delay 
#along with time to advance to the "starting" position, travel_delay

import numpy as np
import math as math

avg_reaction_delay = 0.5
std_reaction_delay = 0.25
avg_travel_delay = 0.75

def removal(num_cars, num_left_lanes, num_right_lanes, num_straight_lanes, time_allowed):
    left_counter = 0
    right_counter = 0
    straight_counter = 0
    time = 0
    cars_through = 0
    
    #either all the cars have passed through a green light and the event ends or
    #the cars run out of time and get stuck to wait for the next cycle
    while cars_through < num_cars:
        if time > time_allowed:
            print("right, left, straight", (right_counter, left_counter,straight_counter))
            return cars_through
        
        #we assume average  reaction delay as a normal random variable
        reaction_delay = np.random.normal(avg_reaction_delay, std_reaction_delay)
        decision = get_car_decision()
        
        #our calculation of travel_delay varies per lane
        #currently calculated by how many cars are before a vehicle * a factor
        #i.e. on a two straight lane road, the third (overall) car is only behind
        #one car, the same goes for the fourth.
        #this assumes people fill in lanes about evenly
        #TODO: obviously cars in the back should have a higher multiplicative effect
        if decision == "straight":
            travel_delay = avg_travel_delay * math.floor(straight_counter / num_straight_lanes)
            straight_counter += 1
            time += reaction_delay + travel_delay
        elif decision == "left":
            travel_delay = avg_travel_delay * math.floor(left_counter / num_left_lanes)
            left_counter += 1
            time += reaction_delay + travel_delay
        else:
            travel_delay = avg_travel_delay * math.floor(right_counter / num_right_lanes)
            right_counter += 1
            time += reaction_delay + travel_delay
        
        cars_through += 1
    print("right, left, straight", (right_counter, left_counter,straight_counter))
    print("time elapsed", time)
    return cars_through


def get_car_decision():
    
    # generate a uniform random variable to determine which way the car is going
    # TODO: base this off real data from the intersection
    
    random_num = np.random.uniform()
    if random_num < 0.2:
        return "left"
    if random_num < 0.8:
        return "straight"
    else:
        return "right"