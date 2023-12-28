#Write a program to print twin primes less than 1000. If two consecutive  odd numbers are both prime then they are known as twin primes.

def is_prime(n):
   for i in range(2, n):
      if n % i == 0:
         return False
   return True

def generate_twins(start, end):
   for i in range(start, end):
      j = i + 2
      if(is_prime(i) and is_prime(j)):
          print(i, "and", j)
          
print("\nTwin primes less than 1000:")
generate_twins(2, 1000)