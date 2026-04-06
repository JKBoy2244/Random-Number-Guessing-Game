class Winner:

  def displayWinner(self, playerScoreList, playerList):

    if playerScoreList and isinstance(playerScoreList[0], str):
        playerScoreList, playerList = playerList, playerScoreList
      
    highestScore = playerScoreList[0]
    winnerIndex = 0
    for i in range(len(playerScoreList)):

      if playerScoreList[i] > highestScore:
        highestScore = playerScoreList[i]
        winnerIndex = i

    print("The highest score was", highestScore)
    print("The winner of the game is", playerList[winnerIndex])
    return playerList[winnerIndex]
