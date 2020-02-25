# CX4230
CX4230 Simulation Project

Once loaded in the PACE cluster run <br>
**{module load python/3.6}** <br>

To return the default simulation results (10 runs each of each configuration), run: <br>
**{python3 simulation.py}** <br>
This will print the configurations of: <br>
smart_lights = False, smart_cars = False <br>
smart_lights = True, smart_cars = False <br>
smart_lights = False, smart_cars = True <br>
smart_lights = True, smart_cars = True <br>

To print out the events in a traffic simulation the format is: <br>
run_sim(time_factor, smart_lights, smart_cars) <br>
where time_factor = 1 means real time, 0.1 = 10% of real time, etc... <br>
where smart_lights is a boolean <br>
where smart_cars is a boolean <br>

Examples: <br>
Very fast simulation with smart_lights = True and smart_cars = True **[Recommended]** <br>
**{python3 -c 'from simulation import *; run_sim(0.001, True, True)'}** <br>

Fast simulation with smart_lights = False and smart_cars = True <br>
**{python3 -c 'from simulation import *; run_sim(0.01, False, True)'}** <br>

Lastly, to just run the tests and get metrics: <br>
run_tests(num, smart_lights, smart_cars, verbose) <br>
where num is the amount of iterations <br>
where smart_lights is a boolean <br>
where smart_cars is a boolean <br>
where verbose is a boolean for more verbose printing <br>

Examples: <br>
**{python3 -c 'from simulation import *; run_tests(10, False, True, False)'}** <br>
