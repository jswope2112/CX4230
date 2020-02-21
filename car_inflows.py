#car arrival algorithms

def car_inflows(num_cars, car_flow,  max_car_allowed, time_allowed):
    time = 0
    cars_added = 0

    while num_cars > max_car_allowed:
        if time > time_allowed:
            return cars_added

        num_cars += car_flow
        cars_added += car_flow
        time += 1

    return cars_added
