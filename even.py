import sys

# If no argument or empty string is passed → use default
if len(sys.argv) < 2 or sys.argv[1].strip() == "":
    nums = "1 2 3 4 5"    # default values
    print("No input provided. Using default values:", nums)
else:
    nums = sys.argv[1]
    print("User provided input values:", nums)

# Convert only if there are valid numbers
numbers = [int(n) for n in nums.split() if n.strip() != ""]

even_count = 0
odd_count = 0

for n in numbers:
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Numbers:", numbers)
print("Even Count:", even_count)
print("Odd Count:", odd_count)
