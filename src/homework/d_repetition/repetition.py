def get_factorial(num):
    """Returns the factorial of a given number."""
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

def sum_odd_numbers(num):
    """Returns the sum of odd numbers up to the given number."""
    sum_odds = 0
    i = 1
    while i <= num:
        if i % 2 != 0:
            sum_odds += i
        i += 1
    return sum_odds
