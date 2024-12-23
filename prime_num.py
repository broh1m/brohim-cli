def is_prime(number):
  """Check is a number is a prime number."""
  if number  <= 1:
    return False
  for i in range(2, int(number**0.5) + 1):
    if number % i == 0:
      return False
  return True
  
def print_primes(start, end):
  """Print all prime numb ers between staert and end."""
  print(f"Prime numbers between {start} and {end}:")
  for num in range(start, end + 1):
    if is_prime(num):
      print(num, end=" ")
  print() # Print a newline at the end.