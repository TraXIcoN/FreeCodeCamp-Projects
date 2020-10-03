"""
    Probem Task : Create a function that returns the Primorial of a number.
    Problem Link : https://edabit.com/challenge/fRjfrCYXWJAaQqFXF
"""

def is_prime(n: int):
  for i in range(2, n):
    if n % i == 0:
      return False
  return True


def primorial(i: int):
  iterations = 0  # number of times a prime number is multiplied to retval
  retval = 1  # return value
  seq = 2  # sequence of all numbers to find primes in

  while iterations < i:
    if is_prime(seq):
      retval *= seq
      iterations += 1
    seq += 1  # iterates through sequence of numbers
  return retval

