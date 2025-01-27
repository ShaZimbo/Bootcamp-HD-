# Read in the DOB.txt file.
dob_file = open('DOB.txt', 'r+')

lines = dob_file.readlines()

# Create two lists, one for names and one for birthdates.
names = []
birthdates = []

# Store the names and birthdates in separate lists.
for i in lines:
    list_words = i.strip().split()
    full_name = " ".join(list_words[0:2])
    date_of_birth = " ".join(list_words[2:5])
    names.append(full_name)
    birthdates.append(date_of_birth)

name_string = "\n".join(names)
birthdates_string = "\n".join(birthdates)
    
print("Name\n" + name_string + "\n")
print("Birthdate\n" + birthdates_string)

dob_file.close()
