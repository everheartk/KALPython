waterVolume = float(input("Please enter the amount of water in kg: "))
initTemp = float(input("Please enter the beginning temperature of the water: "))
finalTemp = float(input("Please enter the desired final temperature of the water: "))

energy = (waterVolume * (finalTemp - initTemp) * 4184)

print ("The number of joules required to heat the water from", initTemp, "degrees to", finalTemp, "degrees is", energy, " joules.") 
                       
