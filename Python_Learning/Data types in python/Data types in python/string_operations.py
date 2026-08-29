first_name = "Tashrif"
last_name = "Saeed"

msg = "Hello, Good Evening"

#first character of the msg string
print(f"First letter of the msg:{msg}={msg[0]}")
print(f"Fifth letter of the msg:{msg}={msg[5-1]}")

print(f"Slicing a String: First five letter of msg:{msg} = {msg[:5]}")
print(f"Slicing a String: Last five letter of msg:{msg} = {msg[12:]}")
print(f"Slicing a String: Middle four letter of msg:{msg} = {msg[7:11]}")

print(f"Submitted by :" + first_name + " " + last_name + " We call this: string concentration", sep=" ")

print(f"The last character of a string: {msg[-1]}")
print(f"Reversing a string: Main String-{msg}\nRevesed String-{msg[::-1]}")