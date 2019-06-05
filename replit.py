"""
SDM "Software Development Method" 
"define what you are going to do, before you do it"

objective:
- create a pogram which tells the user a little bit about the current day, weather, and maybe some other information or trivia that you deem relevant.

- example output: "Today is May 28th, 2019, and it is false that it is rainy."
"""

day = "Today"
day_of_week = "Tuesday"
day_of_month = 28
month = "May"
month_num = 5
birthday_month = 7
year = 2019
is_rainy = False
location = "Rockville"
is_am = False

def calc_month_difference(month_num, birthday_month):
  diff = birthday_month - month_num
  if diff < 0:
    return diff + 12
  else: 
      return diff

print(day, "is", month, day_of_month, year, ". In", location,"it is", is_rainy, "that is is rainy." )
#how to print out a formatted string, it gives the varuiables and not the braces written inside

print(f"{day} is {day_of_week}, {month} {day_of_month} {year}. In {location} it is {is_rainy} that it is rainy. It is { calc_month_difference(month_num, birthday_month)} months until my birthday.") 

if is_rainy and is_am: 
  print("\nPlease bring an umbrella")

#sleep and other effects time.sleep(1) with import sys and import time 
#Make a variable called words

"""for char in words:
  time.sleep(0.05)
  sys.stdout.write(char)
  sys.stdout.flush()
"""
