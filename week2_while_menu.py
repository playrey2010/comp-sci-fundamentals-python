asking = True

while asking:
    print("Choices:\n1. Apple\n2. Orange\n3. Banana")
    choice = int(input("Please choose a fruit (1, 2, or 3): "))
    print(f"You chose #{choice}")

    if choice == 1 or choice == 2 or choice == 3:
        asking = False
    else:
        print("Please only type in 1, 2 or 3 >:(")
print("Thank you for making a valid choice!")
    
