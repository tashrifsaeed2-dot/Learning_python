#Always an input function makes a value/data in string data type
name = input("Enter your real name, Agent: ")
gadget = input("Enter your favourite gadget: ")
age = input("Enter your age, Agent: ")

agent_number = 7
speed_rating = 9.5
mission_count = 12
height_m = 1.65
is_active = True

# We can check the data type by using type() function
print(f"Name: {name} -> type: {type(name)}")
print(f"Gadget: {gadget} -> type: {type(gadget)}")
print(f"Agents age: {age} -> type: {type(age)}")
print(f"Agent Number: {agent_number} -> type: {type(agent_number)}")
print(f"Speed Rating: {speed_rating} -> type: {type(speed_rating)}")
print(f"Mission Count: {mission_count} -> type: {type(mission_count)}")
print(f"Height (m): {height_m} -> type: {type(height_m)}")
print(f"Is Active: {is_active} -> type: {type(is_active)}")

# Part 4: Type casting all about converting one type of data to another
agent_number_text = str(agent_number)
mission_count_text = str(mission_count)
speed_rating_text = str(speed_rating)
status_text = str(is_active)

print(f"Agent Number as text: {agent_number_text} -> type: {type(agent_number_text)}")
print(f"Mission Count as text: {mission_count} -> type: {type(mission_count)}")
print(f"Speed Rating as text: {speed_rating_text} -> type: {type(speed_rating_text)}")
print(f"Status as text: {status_text} -> type: {type(status_text)}")