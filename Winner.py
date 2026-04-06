class Winner:

  def displayWinner(self, playerScoreList, playerList):

    highestScore = playerScoreList[0]
    winnerIndex = 0
    for i in range(len(playerScoreList)):

      if playerScoreList[i] > highestScore:
        highestScore = playerScoreList[i]
        winnerIndex = i

    print("The highest score was", highestScore)
    print("The winner of the game is", playerList[winnerIndex])
