import removal

class nave_techwood:

    TIMERS = [10, 30, 10, 10, 30, 10]
	# 2d arrays for each road

	# 0 = straight and right
	# 1 = left
	techwood_north = [[],[]]

	# 0 = right
	# 1 = straight
	# 2 = left
	techwood_south = [[],[],[]]

	# 0 = straight and right
	# 1 = straight
	# 2 = left
	nave_west = [[],[],[]]

	# 0 = striaght and right
	# 1 = straight
	# 2 = left
	nave_east = [[],[],[]]

	#counter for which light to activate
	counter = 0

	def cycle:
	    #techwood South arrow and green
	    techwood_south[0] -= removal(techwood_south[0], 1, TIMERS[0])
	    techwood_south[1] -= removal(techwood_south[1], 1, TIMERS[0])
	    techwood_south[2] -= removal(techwood_south[2], 1, TIMERS[0])
	    techwood_north[0] += car_inflows(techwood_north[0], 1, 36, TIMERS[0])
	    techwood_north[1] += car_inflows(techwood_north[1], 1, 36, TIMERS[0])
	    if techwood_north[0] + techwood_north[1] > 72:
	        time.sleep(TIMERS[0])
	    else:
	        time.sleep(TIMERS[0])

        #techwood S and techwood N green
        techwood_south[0] -= removal(techwood_south[0], 1, TIMERS[1])
        techwood_south[1] -= removal(techwood_south[1], 1, TIMERS[1])
        techwood_north[0] -= removal(techwood_north[0], 1, TIMERS[1])

        time.sleep(TIMERS[1])

        #techwood N green and arrow
        techwood_north[0] -= removal(techwood_north[0], 1, TIMERS[2])
        techwood_north[1] -= removal(techwood_north[1], 1, TIMERS[2])

        time.sleep(TIMERS[2])

        #Nave W green and arrow
        nave_west[0] -= removal(nave_west[0], 1, TIMERS[3])
        nave_west[1] -= removal(nave_west[1], 1, TIMERS[3])
        nave_west[2] -= removal(nave_west[2], 1, TIMERS[3])

        time.sleep(TIMERS[3])

        #Nave W and Nave E green
        nave_east[0] -= removal(nave_east[0], 1, TIMERS[4])
        nave_east[1] -= removal(nave_east[1], 1, TIMERS[4])
        nave_west[0] -= removal(nave_west[0], 1, TIMERS[4])
        nave_west[1] -= removal(nave_west[1], 1, TIMERS[4])

        time.sleep(TIMERS[4])

        #Nave E green and arrow
        nave_east[0] -= removal(nave_east[0], 1, TIMERS[5])
        nave_east[1] -= removal(nave_east[1], 1, TIMERS[5])
        nave_east[2] -= removal(nave_east[2], 1, TIMERS[5])
        techwood_south[0] += car_inflows(techwood_south[0], 1, 38, TIMERS[5])
        techwood_south[1] += car_inflows(techwood_south[1], 1, 38, TIMERS[5])
        techwood_south[2] += car_inflows(techwwod_south[2], 1, 38, TIMERS[5])
        if techwood_south[0] + techwood_south[1] + techwood_south[2] > 114:
            time.sleep(TIMERS[5])
        else:
            time.sleep(TIMERS[5])

		#techwood South arrow and green
		if counter == 0:
			#remove cars from techwood S right and straight
			#remove cars from techwood S left

		#techwood S and Techwood N green
		if counter == 1:
			#remove cars from techwood S right and straight
			#remove cars from techwood N straight and right

		#techwood N green and arrow
		if counter == 2:
			#remove cars from techwood N right and straight
			#remove cars from techwood N left

		#Nave W green and arrow
		if counter == 3:
			#remove cars from nave w right and straight
			#remove cars from nave w straight
			#remove cars from nave w left

		#Nav W and Nave E Green
		if counter == 4:
			#remove cars nave w right and straight
			#remove cars nave w straight
			#remove cars nave e stright and right
			#remove cars nave e straight

		#Nave E green and arrow 
		if counter == 5:
			#remove cars nave e stright and right
			#remove cars nave e straight
			#remove cars nave e left

		counter = (counter + 1) % 6

		def get_cars:
			fill_nave_east()
			fill_nave_west()
			fill_techwood_north()
			fill_techwood_south()