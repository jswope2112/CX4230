class offramp:
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

	counter = 0

	def cycle:

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