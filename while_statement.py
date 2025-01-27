# Set the number of user tries and total of intergers to 0
counter = 0
number = 0

user_input = int(input("Please enter a number (-1 to exit): "))

# If the number inputted is not -1
while number != -1:
    if user_input != -1:
        number += user_input
        counter += 1
        user_input = int(input("Please enter a number (-1 to exit): "))

# If the number inputted is -1
    else:
        print(round(number / counter, 2))
        break
