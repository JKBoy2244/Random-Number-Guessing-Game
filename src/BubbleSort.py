class BubbleSort:

  def randomBubbleSort(self, randomNumbersList):

    x = len(randomNumbersList)
    for i in range(x-1):
        for j in range(x-i-1):
            if randomNumbersList[j] > randomNumbersList[j+1]:
              randomNumbersList[j], randomNumbersList[j+1] = randomNumbersList[j+1], randomNumbersList[j]

    print("Sorted random number list:", randomNumbersList)
    print("Highest random number I thought of was", randomNumbersList[x-1])
    print("Lowest random number I thought of was", randomNumbersList[0])
    maxDifference = abs(randomNumbersList[0] - randomNumbersList[x-1])
    print("Maximum difference between the highest and the lowest is", maxDifference)

  def playerBubbleSort(self, playerScoreList):

    x = len(playerScoreList)
    for i in range(x-1):
      for j in range(x-i-1):
          if playerScoreList[j] > playerScoreList[j+1]:
            playerScoreList[j], playerScoreList[j+1] = playerScoreList[j+1], playerScoreList[j]

    print("Sorted scores list:", playerScoreList)
    print("Highest number of points was", playerScoreList[x-1])
    print("Lowest number of points was", playerScoreList[0])
    maxDifference = abs(playerScoreList[0] - playerScoreList[x-1])
    print("Maximum difference between the highest and the lowest is", maxDifference)
