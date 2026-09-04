#Assignment operator
# The assignment operator(=) collects the value/data  from its r.h.s and assigns /stores in the variable to its l.h.s 
feild1 = 120
feild2 = 85
feild3 = 150
feild4 = 95
feild5 = 110

#--- Aritmatic Operators (+, -, *, /)
total = feild1 + feild2 + feild3 + feild4 +feild5
average = total / 5

print("Total harvest        :", total, "kg")
print("Average per field    :", average, "kg")

price_per_kg = 15
earnings = total * price_per_kg
price_per_kg("Total earnings     : tk.", earnings)

#----Floor division (//) and modulus (%)
bags = total // 25
leftover = total % 25

print("Full bags packed    :", bags)
print(" Left over grains   :", leftover, "kg")

