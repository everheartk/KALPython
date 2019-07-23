outTemp = float(input("Please enter the temperature in Fahrenheit between -58 and 41 degrees: "))
speed = float(input("Please enter the wind speed in miles per hour: "))


windChill = 35.74 + (.6215 *outTemp) - (35.75 *(speed**.16)) + (.4275 * outTemp * (speed**.16))

print ("The wind chill is", round(windChill, 5))
