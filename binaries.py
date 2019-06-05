# 1. Give the user a quiz question to 
# convert a decimal number to a binary number
#such as: 'convert decimal 5 to binary:'  and 
# theu user would write '101' to get the answer
# correct. The program will tell the user if they go the correct answer or not. 

binaries = {
0:0,
1:1,
2:10,
3:11,
4:100,
5:101,
6:110,
7:111,
8:1000,
9:1001,
10:1010,
11:1011,
12:1100,
13:1101,
14:1110,
15:1111
}
answer = int(input("Convert 5 to decimals"))
if answer == binaries.get(5):
	print("Correct")
else:
	print("Sorry, that is incorrect")