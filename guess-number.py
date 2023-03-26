import random

random_number = random.randrange(100)

correct_guess = False

while not correct_guess:
    user_input = input("Guess a number between 0 and 100: ")
    
    try:
      number = int(user_input)
      if random_number == number:
        correct_guess = True
      elif number > random_number:
        print("Your guess is too high.")
      elif number < random_number:
        print("Your guess is too low.")
    except:
      print("Error: Your guess must be a number.")

print("You guessed the right number!")