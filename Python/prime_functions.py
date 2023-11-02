import math
import functools


def is_prime(n):
    prime_core = math.factorial(n-1)
    prime_int = (prime_core + 1) / n
    return bool(math.floor(pow(math.cos(math.pi*prime_int), 2)))


@functools.cache
def isprime(n):
    prime_core = math.factorial(n-1)
    return bool((prime_core + 1) % n)
    # return bool(math.floor(pow(math.cos(math.pi*prime_int), 2)))
