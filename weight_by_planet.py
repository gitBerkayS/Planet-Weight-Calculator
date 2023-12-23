print("Keep track of your weight by planet!!\n")
weight = float(input("Whats your weight?\n"))

print("I have information for the following planets:\n")
print("""1. Venus   2. Mars    3. Jupiter
4. Saturn  5. Uranus  6. Neptune\n""")
planet = int(input("Which planet do you want the weight for?\n"))

#variables corresponding to their relative gravity.
gravity_venus = .91
gravity_mars = .38
gravity_jupiter = 2.34
gravity_saturn = 1.06
gravity_uranus = .92
gravity_neptune = 1.19

# Weight = Mass * Gravity
if planet == 1:
  print("You've selected Venus. Your weight is:", gravity_venus * weight)
elif planet == 2:
  print("You've selected Mars. Your weight is:", gravity_mars * weight)
elif planet == 3:
  print("You've selected Jupiter. Your weight is:", gravity_jupiter * weight)
elif planet == 4:
  print("You've selected Saturn. Your weight is:", gravity_saturn * weight)
elif planet == 5:
  print("You've selected Uranus. Your weight is:", gravity_uranus * weight)
elif planet == 6:
  print("You've selected Neptune. Your weight is:", gravity_neptune * weight)

