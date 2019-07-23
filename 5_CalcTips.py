total = float(input("Please enter the bill total:  "))
rate = float(input("Please enter the gratuity rate:  "))

gratuity = (rate * .01)* total
totalBill = total + gratuity

print ("The gratuity is ", (round(gratuity, 2)))
print("The total bill is ", (round(totalBill,2)))
