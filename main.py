import os
import random

# define the function
def secure_code_challenger():
  print("Secure Code Challenger")
  num_of_guesses = 0
  secure_code = int(input("Enter the secure code: "))
  while True:
    code_guess = random.randint(0000, 9999)
    print("code tried:", code_guess)
    os.system("clear")
    num_of_guesses = num_of_guesses + 1
    if code_guess == secure_code:
      print("The secure code is", code_guess)
      print("Number of guesses:", num_of_guesses)
      break

# run the function
secure_code_challenger()