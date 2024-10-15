# Pre-set 5 numbers
num1 = 35
num2 = 68
num3 = 13
num4 = 96
num5 = 59

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
