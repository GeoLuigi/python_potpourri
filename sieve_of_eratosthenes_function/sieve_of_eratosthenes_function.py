'''
Eratosthenes sieve function
'''
def eratosthenes_sieve(objective_number: int):
    '''
    Implements the Sieve of Eratosthenes algorithm to find all prime numbers
    up to the objective number.

    Args:
        objective_number (int): The objective number to find prime numbers up to.

    Returns:
        None. Prints the prime numbers found.

    '''
    primes = []
    discard = set()

    for number in range(2, objective_number + 1):
        if number not in discard:
            primes.append(number)
            for j in range(number, objective_number // number + 1):
                discard.add(number * j)

    return print(f'\nPrime numbers between 1 and {objective_number}:\n{primes}')
