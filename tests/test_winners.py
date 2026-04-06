import pytest
from Winner import Winner

class TestWinner:

  def testWinner(self):

    winner = Winner()
    playerList = ["ABCDE@45671b", "ABCDE@45671d","ABCDE@45671f","ABCDE@45671h","ABCDE@45671k", "ABCDE@45671o"] 
    scoreList = [0, 140, 120, 190, 200, 40]
    result = winner.displayWinner(playerList, scoreList)

    assert result == playerList[scoreList.index(max(scoreList))]
    assert result == "ABCDE@45671k"
