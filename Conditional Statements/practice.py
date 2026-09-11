""""
Python Executes code line by line from top ta bottom , e.g, line#1, line#2....
1 indentation = 4 spaces / 1 tab / 2 spaces
"""
number = int(input("Enter a Number:"))

if number > 0:
    print(f"{number} is Positive") #This is under the previous line condition because its intended
elif number < 0:
    print(f"{number} is negative")
else:  # there shoudnt any condition after else
    print(f"{number} is neutral")

print("Got Out of the conditional statement")    
