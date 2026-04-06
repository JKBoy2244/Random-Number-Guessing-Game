import random
import time

class StartGame:

   def play(self, usernameList):

       self.playerScoreList = []
       self.randomNumbersList = []

       for current_user in usernameList:
         print(f"\n--- Now it is {current_user}'s turn to play! ---")

         maxGuesses = 10
         guesses = 0
         maxHints = 3
         hints = 0
         points = 220

         number = random.randint(1, 10000)

         while (guesses != maxGuesses):

           print("You start with 200 points. If you can guess the number correctly without any hints, you get 100 points otherwise any wrong guess including 1 guess but you clicked at least 1 hint, your score drops!")
           time.sleep(3)
           numberGuessString = input("Please guess the number the program is thinking of, or if you really don't know, type hint to get one although if you do, your score will decrease")

           guesses += 1
           points -= 15


           if not numberGuessString:


             if guesses == maxGuesses:

               self.randomNumbersList.append(number)
               self.playerScoreList.append(points)
               print("Game over, you used all 10 guesses")
               time.sleep(2)
               print("The random number I thought of was", number)
               break

             print("Sorry, you didn't type anything, please try again")
             print("You have ", maxGuesses - guesses, "left!")

           elif numberGuessString.lower() == "hint":


             if hints == maxHints:

               print("Sorry, I gave you all 3 hints, I can't give you anymore")
               continue

             else: 

               hints += 1
               points -= 10
               match hints:

                case 1:

                 print("The number I am thinking of has", len(str(number)), "digits")
                 continue

                case 2:

                  sum_of_values = 0
                  for char in str(number):
                    sum_of_values += int(char)

                  print("All of the digits in this number add up to", sum_of_values)
                  continue

                case 3:

                 if (number % 2 == 0):
                   print("The number I am thinking of is even")
                 else:
                   print("The number I am thinking of is even")
                 continue

           else:

             try:

               numberGuess = int(numberGuessString)

               if (numberGuess != number):

                 if (numberGuess < number):

                   if (abs(number-numberGuess) >= 1000):

                     if guesses == maxGuesses:

                        self.randomNumbersList.append(number)
                        self.playerScoreList.append(points)
                        print("Game over, you used all 10 guesses")
                        time.sleep(2)
                        print("The random number I thought of was", number)
                        break

                     print("The number you said of is way below what I am thinking off")
                     print("You have ", maxGuesses - guesses, "left!")
                     continue

                   elif (500 <= abs(number-numberGuess) < 999):

                     if guesses == maxGuesses:

                         self.randomNumbersList.append(number)
                         self.playerScoreList.append(points)
                         print("Game over, you used all 10 guesses")
                         time.sleep(2)
                         print("The random number I thought of was", number)
                         break

                     print("The number you said of is somewhat far off what I am thinking off")
                     print("You have ", maxGuesses - guesses, "left!")
                     continue

                   elif (1 <= abs(number-numberGuess) < 499):

                     if guesses == maxGuesses:

                        self.randomNumbersList.append(number)
                        self.playerScoreList.append(points)
                        print("Game over, you used all 10 guesses")
                        time.sleep(2)
                        print("The random number I thought of was", number)
                        break

                     print("The number you said of is below but really close what I am thinking off")
                     print("You have ", maxGuesses - guesses, "left!")
                     continue

                 elif (numberGuess > number):

                  if (abs(numberGuess-number) >= 1000):

                    if guesses == maxGuesses:

                      self.randomNumbersList.append(number)
                      self.playerScoreList.append(points)
                      print("Game over, you used all 10 guesses")
                      time.sleep(2)
                      print("The random number I thought of was", number)
                      break

                    print("The number you said of is way above what I am thinking off")
                    print("You have ", maxGuesses - guesses, "left!")
                    continue

                  elif (500 <= abs(number-numberGuess) < 999):

                    if guesses == maxGuesses:

                       self.randomNumbersList.append(number)
                       self.playerScoreList.append(points)
                       print("Game over, you used all 10 guesses")
                       time.sleep(2)
                       print("The random number I thought of was", number)
                       break

                    print("The number you said of is somewhat far above what I am thinking off")
                    print("You have ", maxGuesses - guesses, "left!")
                    continue

                  elif (1 <= abs(number-numberGuess) < 499):

                    if guesses == maxGuesses:

                      self.randomNumbersList.append(number)
                      self.playerScoreList.append(points)
                      print("Game over, you used all 10 guesses")
                      time.sleep(2)
                      print("The random number I thought of was", number)
                      break

                 print("The number you said of is above but really close what I am thinking off")
                 print("You have ", maxGuesses - guesses, "left!")
                 continue

               else:

                 self.randomNumbersList.append(number)
                 self.playerScoreList.append(points)
                 print("You guessed the number successfully!")
                 time.sleep(2)
                 print("The number I thought off was", number)
                 break


             except ValueError:

               if guesses == maxGuesses:

                  self.randomNumbersList.append(number)
                  self.playerScoreList.append(points)
                  print("Game over, you used all 10 guesses")
                  time.sleep(2)
                  print("The random number I thought of was", number)
                  break

               print("Sorry, that's an invalid input, please try again")
               print("You have ", maxGuesses - guesses, "left!")
               continue
