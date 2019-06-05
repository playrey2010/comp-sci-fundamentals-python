colors = ["gray", "red", "blue", "orange", "yellow", "green", "blue", "orange", "orange", "red"]
print("Third item of colors: ", colors[2])	#print a specific item from list
sum = 0
for f in colors:		
	if f == "orange":
		print("found")
		sum += 1
print("Oranges: ",sum)
print("colors:", colors)
print(colors.count("oranges"))