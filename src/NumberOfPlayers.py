import random
import time
import re
import sys

class NumberOfPlayers:

  def __init__(self, number=0):
    self.number = number

  def get_number(self) -> int:
    return self.number

  def set_number(self, number: int):
    self.number = number

  def Input(self, value=None):

    if value is not None:
        self.set_number(value)
        return "Successful"

    maxAttempts = 10
    attempts = 0

    while (attempts != maxAttempts):

        print("Minimum number of players is 4 and maximum number of players is 9: ")
        numberPlayers = input("How many players are playing the random number generator game?")
        attempts+=1

        if (not numberPlayers.strip()):

          if attempts == maxAttempts:
            sys.exit("Too many attempts.")

          print("Empty value isn't allowed, please try again!")
          print("You now have", maxAttempts-attempts, "left now!")
          continue

        else:

          try: 

            numberOfPlayer = int(numberPlayers)

            if not (4 <= numberOfPlayer <= 9):

              if attempts == maxAttempts:
                sys.exit("Too many attempts.")

              print("That's outside the restricted number of players. Please try again")
              print("You now have", maxAttempts-attempts, "left now!")
              continue

            else:

              self.set_number(numberOfPlayer)
              print("You successfully entered the correct number of players")
              return 

          except ValueError:

            if attempts == maxAttempts:
              sys.exit("Too many attempts.")

            print("That's invalid input. Please try again")
            print("You now have", maxAttempts-attempts, "left now!")
            continue
