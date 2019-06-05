# movies I saw in 2018 
movie_count = [3,5,10,7,4]
"""print("==========================")
print(movie_count[0]) #find out what is in list index 0.
print(movie_count[1]) #find out what is in list index 1. 
print(movie_count[2])
print(movie_count[0] > 4)"""
for i in range(len(movie_count)):
	if movie_count[i] > 4:
		print("You watched a lot of movies")
	else:
		print("You watched few movies...")