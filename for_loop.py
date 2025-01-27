# Print a pattern of stars in an arrow shape using a for loop.
max_stars = 10
total_lines = max_stars*2

for i in range(1, total_lines):
    if i <= max_stars:
        print(i * "*")
    else:
        print("*" * (total_lines - i))
