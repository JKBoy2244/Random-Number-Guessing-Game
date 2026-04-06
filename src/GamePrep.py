import random
import time
import re
import sys

class GamePrep(NumberOfPlayers):

   def __init__(self, number, username="", age=0): 

     super().__init__(number)
     self.username = username
     self.age = age

   def get_username(self) -> str:
     return self.username

   def set_username(self, username: str):
     self.username = username

   def get_age(self) -> int:
     return self.age

   def set_age(self, age: int):
     self.age = age

   usernameList = []
   ageList = []

   def Input(self):

     for i in range(self.number):

       maxAttempts = 3
       attempts = 0

       while (attempts != maxAttempts):

         print("Rules for choosing a username: ")
         print("1). Username must be between 10 and 20 characters long. ")
         print("2). There should be at least 1 number present. ")
         print("3). There should be at least 1 lower case letter and 1 upper case letter")
         print("4). There has to be minimum 1 special character present")
         print("5). Also, the username can't be the same as someone else's username to avoid confusion")

         time.sleep(2)

         username = input("According to the 5 conditions stated above, please state your username please!")
         attempts += 1

         if not username:

           if attempts == maxAttempts:
             sys.exit("Too many attempts.")

           print("Empty value isn't allowed, please try again!")
           print("You now have", maxAttempts-attempts, "left now!")
           continue

         elif not (10 <= len(username) <= 20):

           if attempts == maxAttempts:
             sys.exit("Too many attempts.")

           print("Sorry, username doesnt have the required number of characters, please try again")
           print("You now have", maxAttempts-attempts, "left now!")
           continue

         elif not (re.search("[a-z]", username) and re.search("[A-Z]", username) and 
                   re.search("[0-9]", username) and re.search("[^a-zA-Z0-9]", username)):

           if attempts == maxAttempts:
             sys.exit("Too many attempts.")

           print("Sorry, username doesnt meet all requirements from 2). to 4)., please try again")
           print("You now have", maxAttempts-attempts, "left now!")
           continue

         elif username in self.usernameList:

           if attempts == maxAttempts:
             sys.exit("Too many attempts.")

           print("Sorry, username is already taken, please try again")
           print("You now have", maxAttempts-attempts, "left now!")
           continue

         else:

           self.set_username(username)
           self.usernameList.append(username)
           print("You successfully entered a valid username")
           break 

   def ageInput(self):

     for i in range(self.number):

       maxAttempts = 3
       attempts = 0
       current_user = self.usernameList[i]

       while (attempts != maxAttempts):

         ageString = input(f"Hello {current_user}, how old are you (minimum age to play this game is 7): ")
         attempts += 1

         if not ageString:

           if attempts == maxAttempts:
             sys.exit("Too many attempts.")

           print("Empty value isn't allowed, please try again!")
           print("You now have", maxAttempts-attempts, "left now!")
           continue

         else:

           try:

             age = int(ageString)

             if age < 7:

               if attempts == maxAttempts:
                 sys.exit("Too many attempts.")

               print("Sorry, you can't play this game cos you're too young, please try again!")
               print("You now have", maxAttempts-attempts, "left now!")
               continue

             else:

              self.set_age(age)
              self.ageList.append(age)
              print("You successfully entered a valid age")
              break

           except ValueError:

             if attempts == maxAttempts:
               sys.exit("Too many attempts.")

             print("That's invalid input. Please try again")
             print("You now have", maxAttempts-attempts, "left now!")
             continue
