def bottle_song(num=99):
	if num == 1:
		print("1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.")
	for i in range(num, 1, -1):
		if i == 2:
			print("2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.\n1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.")
		else:
			print(str(i) + " bottles of beer on the wall, " + str(i) + " bottles of beer.\nTake one down and pass it around, " + str(i - 1) + " bottles of beer on the wall.")


bottle_song()
