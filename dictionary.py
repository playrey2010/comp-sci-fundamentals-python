"""dictionary example:
keys go on the left,
values on the right
a dictionary is a collection of "key-value" pairs
"""

addresses = {
	"Ronnie": "Rockville",
	"Hemanuel": "Germantown",
	"Maria" : "London",
	"Carlos" : "San Juan",
}
print(addresses)
for x in addresses.keys():
	print(x)

for x in addresses.values():
	print(x)
	
for k in addresses.keys(): 
	print(k,"is in", addresses.get(k), end=".\n")
	print(k + " is in " + addresses.get(k) + ".")