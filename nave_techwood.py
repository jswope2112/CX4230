class nave_techwood:

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