check = True
while check:
    n = int(input())  # Input a number
    # Check for Armstrong number
    # An Armstrong number is a number that is equal to the sum of its digits raised to the power of k
    # For example, 153 = 1^3 + 5^3 + 3^3
    k = 0
    original_n = n

    # Count the number of digits in n
    while n != 0:
        k += 1
        n //= 10

    total = 0
    n = original_n

    # Calculate the sum of digits raised to the power of k
    while n != 0:
        digit = n % 10
        total += digit ** k
        n //= 10

    # Check if it is an Armstrong number
    if total == original_n:
        print(f'{original_n} is an Armstrong number')
        check = False


