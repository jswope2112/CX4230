import removal

class offramp:

    TIMERS = [30, 30]
	# double arrays for each road 

	# 0 = right and left
	# 1 = left
	offramp_249 = [[],[]]

	# 0 = straight
	# 1 = straight
	nave_west = [[],[]]

	# 0 = straight
	# 1 = straight
	nave_east = [[],[]]

    east_destination
    west_destination

	counter = 0

	def cycle:
	    #Nave e and Nave w green light
	    nave_west[0] -= removal(nave_west[0], 1, TIMERS[0])
        nave_west[1] -= removal(nave_west[1], 1, TIMERS[0])
        nave_east[0] -= removal(nave_east[0], 1, TIMERS[0])
        nave_east[1] -= removal(nave_east[1], 1, TIMERS[0])
        offramp_249[0] += car_inflows(offramp_249[0], 8, 96, TIMERS[0])
        offramp_249[1] += car_inflows(offramp_249[1], 8, 96, TIMERS[0])
        if offramp_249[0] + offramp_249[1] > 192:
        	time.sleep(TIMERS[0])
        else:
            time.sleep(TIMERS[0])

        #offramp green light
        offramp_249[0] -=removal(offramp_249[0], 1, TIMERS[1])
        offramp_249[1] -=removal(offramp_249[1], 1, TIMERS[1])
        nave_east[0] += car_inflows(nave_east[0], 6, 111, TIMERS[1])
        nave_east[1] += car_inflows(nave_east[1], 6, 111, TIMERS[1])
        if nave_east[0] + nave_east[1] > 223:
            time.sleep(TIMERS[1])
        else:
            time.sleep(TIMERS[1])

		#Nave e and Nave w green light
		if counter == 0:

			#remove cars from both nave e straight lanes
			#remove cars from both nave w straight lanes

		if counter == 1:

			#remove cars from offramp left and right
			#remove cars from oframp right

		counter = (counter + 1) % 3

	def get_cars:
		fill_nave_east()
		fill_nave_west()
		fill_offramp()