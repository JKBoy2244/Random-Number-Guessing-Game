# Random Number Guessing Game

# How the game works

- So, this game I made is a random number guessing game where a user has up to 10 guesses to guess a random number from 1 to 10000 and also, the user can ask up to 3 hints for what the random number the program is thinking of is which include how many digits and also the sum of digits for example. The score starts from 200 points however, the final score is calculated based on the number of guesses and also number of hints taken, so for example, if a user guesses with 1 go, the user gets 200 points (without looking at any hints obviously, but even 1 hint despite 1 guess, the player loses points). Minimum number of players is 4 and maximum number of players is 9. Also, minimum age to play this game is 7. 

- Also, just for fun, I implemented bubble sort and also heap sorting when comparing the scores in the list and also during the sorting process to determine the winner as well as the highest score, lowest score and the difference between both highest and lowest score.

- This program has extremely strong security involved to prevent millions of attempt for 1 question/prompt by enforcing a 3-attempt limit rule where if anywhere you bypass the attempt limit (at least before starting the game), the system automatically ends. Also, the game handles all kinds of invalid inputs very strongly in any way from empty inputs and out of range values to typing a string instead of a integer (not to mention robust regex checking).

- <img width="440" height="765" alt="image" src="https://github.com/user-attachments/assets/48400943-daee-46c2-a463-4d97019225a8" />

  <img width="440" height="765" alt="image" src="https://github.com/user-attachments/assets/66d5f34b-dd6e-4033-8add-302c5fdbc9e3" />

  <img width="680" height="300" alt="image" src="https://github.com/user-attachments/assets/a77a37d8-c865-4b34-8a1c-3a4416fd7081" />



# How to run the app

- First, you download the zip file first on github by clicking download zip

- Then, you extract the python file

- After that, if you haven't installed python, install python (otherwise, this won't work on terminal)

- Open terminal and type these 2 things in order:

        cd ~/Downloads/file-name

        python Main.py 
