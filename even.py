import sys


if len(sys.argv) != 2:
    print("Usage: python even_odd_counter.py \"1 2 3 4 5\"")
    sys.exit(1)

numbers = list(map(int, sys.argv[1].split()))

even_count = 0
odd_count = 0

for n in numbers:
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)
