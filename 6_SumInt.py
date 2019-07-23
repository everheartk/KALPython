inputNumber = int(input("Please enter a number between 0 and 1000: "))

outputSum = 0

while (inputNumber >0):
    digit = inputNumber % 10
    outputSum = outputSum + digit
    inputNumber = inputNumber //10

print("The sum of the digits is", outputSum)
