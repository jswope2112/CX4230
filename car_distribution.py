import numpy as np

class Car_Distribution:
    """
    @hourly_cars: Numbers of cars entering intersection per hour
    @time_frame: Minutes per hour a new wave of cars arrive
    @standard_deviation: percentage representing standard deviation of car inflow
    @get_inflow(): Uses Gaussian distribution to select amount of cars for inflow
    """

    def __init__(self, hourly_cars = 600, time_frame = 2, standard_deviation = 0.1):
        time_segments = 60 / time_frame
        self.avg_cars = hourly_cars / time_segments
        self.standard_deviation = self.avg_cars * standard_deviation
    
    def get_inflow(self):
        return round(np.random.normal(self.avg_cars, self.standard_deviation))

        