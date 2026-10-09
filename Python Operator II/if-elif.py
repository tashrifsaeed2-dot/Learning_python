# Smart School Day Planner

print("=== Smart School Day Planner ===")
print("Answer 3 question and i will planeyour day!\n")

day = input("What day is it? (Monday To Sunday): ").strip().capitalize()
weather = input("What is the weather? (sunny / rainy / cloudy): ").strip().lower()
homework = input("Is your homework done? (yes / no): ").strip().lower()

print()
print(f"=== Your Plan for {day} ===")
print("-" * 35)

cond1 = day in ("Saturday", "Sunday")

if cond1:
    print("Day type     : Weekend - enjoy your free time!")
elif day == "Monday":
    print("Day type     : First day of the week. Pack your weekly planner")    
elif day == "Friday":
    print("Day type     : Last school day. Return the library books today.")    
elif day == ("Tuesday", "Wednesday", "Thursday"):
    print("Day type     : Regular school days. Stay focused!")
else:
    print("Day type     : Day not recognized. Please check the spelling.")


if weather == 'sunny' and homework == "yes":
    print("After school: Head to the the park - great weather and homework is done!")

if weather == "rainy" or weather == "cloudy":
    print("Weather tip: Pack your unbrella - it may get wet outside")

if not (homework == "yes"):
    print("Homework: Not doone yet. Do it before going out!")


if weather == "rainy" and not (homework == "yes"):
    print("Best plan: Stay in, finish your homework, then watch your favourite show.")
elif weather == "sunny" and homework == "yes" and not (day in("Saturday", "Sunday")):
    print("Best plan: All set for a freat school day - you are prepared!")
elif day in ("Saturday", "Sunday") and weather == "sunny":
    print("Nest plan: Perfect weekend weather - head outside and have fun!")
else:
    print("Best plan: Take it one step at a time - you have got this!")

print()
print("Plan completed! Have a wonderful day!")