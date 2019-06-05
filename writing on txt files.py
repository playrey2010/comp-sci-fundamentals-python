name = "Rey"
day = "Thursday, May 30th"
message1 = f"My name is {name} and today is {day}."
message2 = "This is the 2nd line." # new
message3 = "This is the 3rd and final line." #new
messages = [message1, message2, message3] # new

filename = "poems1.txt" #new
#file = open(filename, "w") # note: w stands for write. This indicates we open the program in write mode.
#file.writelines(messages) # new
#file.close()

with open(filename, 'w') as f:
    for m in messages:
        f.write(f"{m}\n")
