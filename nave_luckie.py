import removal
import car_inflows

class nave_luckie:

    TIMERS = [10, 30, 30, 30, 30]
	# 2d arrays for each road

	# 0 = straight and turn right
	# 1 = turn left
	tech_pkwy = [0, 0]

	# 0 = turn right
	# 1 = straight
	# 2 = left
	luckie = [0, 0, 0]

	# 0 = right and straight
	# 1 = straight
	# 2 = left
	nave_west = [[],[],[]]

	# 0 = straight and right
	# 1 = straight and left
	# 2 = left
	nave_east = [[],[]]
    
    north_destination
    east_destination
    south_destination
    west_destination

	# counter on which cycle it is on
	counter = 0

	def cycle(sched):
    
        #luckie green and arrow
        l, r, s -= removal(luckie[0], 1, TIMERS[0])
        east_destination.fill(
        luckie[1] -= removal(luckie[1], 1, TIMERS[0])
        luckie[2] -= removal(luckie[2], 1, TIMERS[0])
        tech_pkwy[0] += car_inflows(tech_pkwy[0], 4, 99, TIMERS[0])
        tech_pkwy[1] += car_inflows(tech_pkwy[1], 4, 99, TIMERS[0])
        if tech_pkwy[0] + tech_pkwy[1] > 198
            time.sleep(TIMERS[0])
        else:
            time.sleep(TIMERS[0])

        #luckie green and tech pkwy green
		luckie[0] -= removal(luckie[0], 1, TIMERS[1])
        luckie[1] -= removal(luckie[1], 1, TIMERS[1])
        tech_pkwy[0] -= removal(tech_pkwy[0], 1, TIMERS[1])
        tech_pkwy[1] -= removal(tech_pkwy[1], 1, TIMERS[1])
        nave_west[0] += car_inflows(nave_west[0], 8, 166, TIMERS[1])
        nave_west[1] += car_inflows(nave_west[1]. 8, 166, TIMERS[1])
        nave_west{2] += car_inflows(nave_west[2], 8, 166, TIMERS[1])
        if nave_west[0] + nave_west[1], nave_west[2] > 498:
            time.sleep(TIMERS[1])
        else:
            time.sleep(TIMERS[1])

        #tech pkwy green and arrow
        tech_pkwy[0] -= removal(tech_pkwy[0], 1, TIMERS[2])
        tech_pkwy[1] -= removal(tech_pkwy[1], 1, TIMERS[2])
        nave_west[0] += car_inflows(nave_west[0], 8, 166, TIMERS[2])
        nave_west[1] += car_inflows(nave_west[1]. 8, 166, TIMERS[2])
        nave_west{2] += car_inflows(nave_west[2], 8, 166, TIMERS[2])
        if nave_west[0] + nave_west[1], nave_west[2] > 498:
            time.sleep(TIMERS[2])
        else:
            time.sleep(TIMERS[2])

        #nave west green and arrow
        nave_west[0] -= removal(nave_west[0], 1, TIMERS[3])
        nave_west[1] -= removal(nave_west[1], 1, TIMERS[3])
        nave_west[2] -= removal(nave_west[2], 1, TIMERS[3])

        time.sleep(TIMERS[3])

        #nave west green and nave east green
        nave_west[0] -= removal(nave_west[0], 1, TIMERS[4])
        nave_west[1] -= removal(nave_west[1], 1, TIMERS[4])
        nave_east[0] -= removal(nave_east[0], 1, TIMERS[4])
        nave_east[1] -= removal(nave_east[1], 1, TIMERS[4])
        luckie[0] += car_inflows(luckie[0], 2, 89, TIMERS[4])
        luckie[1] += car_inflows(luckie[1], 2, 89, TIMERS[4])
        luckie[2] += car_inflows(luckie[2], 2, 89, TIMERS[4])
        if luckie[0] + luckie[1] + luckie[2] > 269
            time.sleep(TIMERS[4])
        else:
            time.sleep(TIMERS[4])

			#remove cars from luckie right
			#remove cars from luckie straight
			#remove cars from tech pkwy straight and right

		#luckie green and arrow
		if counter == 0:
			s.enter(0, 1, lambda: removal(

		#luckie green and tech pkwy green
		if counter == 1:
			#remove cars from luckie right
			#remove cars from luckie straight
			#remove cars from tech pkwy straight and right

		#tech pkwy green and arrow
		if counter == 2:
			#remove cars from tech parkway straight and right
			#remvoe cars from tech parkway left

		#nave west green and arrow
		if counter == 3:
			#remove cars from nave west straight and right
			#remove cars from nave west straight
			#remove cars from nave west left

		#nave west green and nave east green
		if counter == 4:
			#remove cars from nave west straight and right
			#remove cars from nave west straiht
			#remove cars from nave east straight and right
			#remove cars from nave east straight and left
				##this lane turns left and straight, decide on what to do with car blocking

		counter = (counter + 1) % 5



	def get_cars:
		fill_tech_pkwy()
		fill_luckie()
		fill_nave_west()
		fill_nave_east()