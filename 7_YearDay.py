'''inputMinutes = int(input("Please enter a number of minutes: "))
totalDays = int(inputMinutes/(60*24))
years = int(totalDays/365)
leftOverDays = int(totalDays - (years * 365))

print (inputMinutes, "is approximately", years, "years and", leftOverDays, "days")
'''

inputMinutes = int(input("Please enter a number of minutes: "))
totalDays = int(inputMinutes/(60*24))
years = int(totalDays//365)
leftOverDays = int(totalDays % 365)

print (inputMinutes, "is approximately", years, "years and", leftOverDays, "days")


