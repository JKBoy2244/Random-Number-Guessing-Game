import random
import time
import re
import sys

from Intro import Intro
from NumberOfPlayers import NumberOfPlayers
from GamePrep import GamePrep
from StartGame import StartGame
from ScoresOrdering import ScoresOrdering
from Winner import Winner
from BubbleSort import BubbleSort
from Farewell import Farewell

class Main:

  def playGame(self):
    
    game_intro = Intro()
    game_intro.welcome()
    print("-" * 50)

    player_count = NumberOfPlayers(0)
    player_count.Input()
    total_players = player_count.get_number()
    print("-" * 50)

    prep = GamePrep(total_players)
    prep.Input()
    print("-" * 50)
    prep.ageInput()
    print("-" * 50)

    game = StartGame()
    game.play(prep.usernameList)
    print("-" * 50)

    print("\n--- Binary Heap Demonstration for the game ---")
    heap_logic = ScoresOrdering()
    index = 0
    heap_logic.left_set(index, game.randomNumbersList)
    heap_logic.right_set(index, game.randomNumbersList)
    
    print("\n🥁🥁🥁 AND THE RESULTS ARE IN 🥁🥁🥁\n")
    game_winner = Winner()
    game_winner.displayWinner(game.playerScoreList, prep.usernameList)
    print("-" * 50)

    print("\n--- Fun Game Statistics ---")
    sorter = BubbleSort()

    print("Number Stats:")
    sorter.randomBubbleSort(game.randomNumbersList.copy())
    print("\nScore Stats:")
    sorter.playerBubbleSort(game.playerScoreList.copy())
    print("-" * 50)
    
    goodbye = Farewell()
    goodbye.Farewell()

if __name__ == "__main__":
  
    app = Main()
    app.playGame()
