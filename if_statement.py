# Request full name from user
user_full_name = input ("Please enter your full name: \n")

# Validate the length of name is as expected
if len(user_full_name) == 0:
    print(f"You haven't entered anything. "
    f"Please enter your full name.")
elif len(user_full_name) < 4:
    print(f"You have entered less than 4 characters. "
    f"Please make sure you have entered your name and surname.")
elif len(user_full_name) > 25:
    print(f"You have entered more than 25 characters. "
    f"Please make sure that you have only entered your full name.")
else:
    print("Thank you for entering your name")
