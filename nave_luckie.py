class nave_luckie:

	# 2d arrays for each road

	# 0 = straight and turn right
	# 1 = turn left
	tech_pkwy = [[],[]]

	# 0 = turn right
	# 1 = straight
	# 2 = left
	luckie = [[],[],[]]

	# 0 = right and straight
	# 1 = straight
	# 2 = left
	nave_west = [[],[],[]]

	# 0 = straight and right
	# 1 = straight and left
	# 2 = left
	nave_east = [[],[]]

	# counter on which cycle it is on
	counter = 0

	def cycle:

		#luckie green and arrow
		if counter == 0:
			#remove cars from luckie right
			#remove cars from luckie straight
			#remove cars from luckie left

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