# Ask the user to input 5 numbers
num1 = int(input("Input the 1st number (any range): "))
num2 = int(input("Input the 2nd number (any range): "))
num3 = int(input("Input the 3rd number (any range): "))
num4 = int(input("Input the 4th number (any range): "))
num5 = int(input("Input the 5th number (any range): "))

# Initialize 'highest with the first number
highest = num1

# Compare the other number with the 'highest
if num2 > highest:
    highest = num2
if num3 > highest:
    highest = num3
if num4 > highest:
    highest = num4
if num5 > highest:
    highest = num5

# Print the highest number
print(f"The highest number is: {highest}")
