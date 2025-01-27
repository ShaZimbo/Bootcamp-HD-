# Below is a syntax error.
# The quotation marks weren't closed.
user_number = int(input("Enter a number above 100: \n))
# Below is a logical error.
# If user follows directions this will always be true.
if user_number > 100:
    print ("Count is greater than 100")
# Below is a runtime error.
# The input is an integer and cannot be checked against a string.
elif user_number > "200":
# Below is a syntax error.
# There are no perentheses.
    print "Count is greater than 200"
elif user_number > 300:
    print ("Count is greater than 300")
else:
    print ("That is a large number")
