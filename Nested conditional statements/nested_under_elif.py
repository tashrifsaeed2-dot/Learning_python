"""

Robi checks the weather on Saturday morning:

Sunny → Go to the beach 🌞

Rainy → Stay in and read a book ☔

Anything else (snow, fog, hail...) → Stay home — and then he decides what to do inside based on whether he has homework!

"""

weather = input("What's the weather? (sunny/rainy/other): ").lower()

if weather == "sunny":
    print("Beach day! Grab  your sunglasses.")

elif weather == "rainy":
    print("Cozy day - read a book with hot cocoa.")
else:
    print("Stay home today.")

    homework = input("Do you have homework? (yes/no): ").lower()
    if homework == "yes":
        print("Finish homework first, then relax.")
    elif homework == "no":
        print("Game marathon time!")
    else:
        print("Hm, double-check your backpack!")

print(" Have a good weekend.")