import sys

if len(sys.argv) > 1:
    script_name = sys.argv[0]
    numbers = sys.argv[1:]
    print("User provided input values:")
else:
    script_name = sys.argv[0]
    numbers = ["10", "21", "32", "45", "50"]
    print("No input given — using default values:")

numbers = [int(n) for n in numbers]

even_count = 0
odd_count = 0

for n in numbers:
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("\n--- Even and Odd Count ---")
print("Script Name:", script_name)
print("Numbers:", numbers)
print("Even Numbers Count:", even_count)
print("Odd Numbers Count:", odd_count)
