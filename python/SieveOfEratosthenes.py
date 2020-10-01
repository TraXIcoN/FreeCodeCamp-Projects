from math import sqrt, floor

def sieve_of_eratosthenes(n):
  # initially all numbers are assumed to be prime
  prime_array = [True]*n
  prime_array[0] = prime_array[1] = None
  
  # Find all the primes
  for i in range(2, floor(sqrt(n))+1):
    if prime_array[i]:
      # If a number is prime, it's multiples can't be prime
      for j in range(2*i, n, i):
        prime_array[j] = False
  
  count = 0
  numbers = []
  for i in range(n):
    if prime_array[i]:
      numbers.append(i)
      count+=1
  return (count, numbers)
  
n = int(input("Enter the value of n: "))
count, numbers = sieve_of_eratosthenes(n)
print("Total prime numbers upto n are", count)
print("Numbers: ", numbers)
