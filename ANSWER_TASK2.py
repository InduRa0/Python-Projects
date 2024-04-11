def get_non_primes(start, end):
    # ensure start and end are positive integers
    if not isinstance(start, int) or not isinstance(end, int) or start <= 0 or end <= 0:
        raise ValueError("Error: start and end must be positive integers")

    # swap start and end if necessary
    if start > end:
        start, end = end, start

    non_primes = []
    for num in range(start, end+1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    non_primes.append(num)
                    break

    return non_primes


while True:
    try:
        start = int(input("Enter a positive integer: "))
        end = int(input("Enter another positive integer: "))
        break
    except ValueError:
        print("Error: invalid input. Please enter two positive integers.")

try:
    non_primes = get_non_primes(start, end)
except ValueError as e:
    print(e)
    exit()

print("Non-primes between", start, "and", end, ":")
for i, num in enumerate(non_primes):
    if i % 10 == 0:
        print()
    print(num, end=" ")
print()
