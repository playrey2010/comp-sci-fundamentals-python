Coca_cola = 3
sushi_plates = 10

price1 = 2.50 
price2 = 6.40

print("=================================")
print("Coca-Cola: $" + str(Coca_cola * price1))
print("Sushi plates: $" + str(sushi_plates * price2))

Total = (Coca_cola * price1) + (sushi_plates * price2)
print("Total without tip: $"+ str(Total))
tip = Total * 15/100 
print("Tip: $"+ str(tip))
print("Total with tip: $"+ str(Total + tip))
print("=================================")

# math operators: */+-% 
# to do:
# 1. Make a total which holds the entire cost of the meal.
# 2. Calculate the tip (15, 18, 20%)
# 3. Add the tip to the total
"""pay amount and print this last 
value out like so:... 
""" 