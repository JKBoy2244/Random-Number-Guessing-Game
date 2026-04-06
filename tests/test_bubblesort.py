import pytest
from BubbleSort import BubbleSort

class TestBubbleSort:

  def testRandomSort(self):

    sort = BubbleSort()
    values1 = [23, 4567, 566, 786, 145, 7896, 1134, 567]
    sort.randomBubbleSort(values1)

    assert values1 == [23, 145, 566, 567, 786, 1134, 4567, 7896]
    assert max(values1) == 7896
    assert min(values1) == 23

 def testPlayerSort(self):

    sort = BubbleSort()
    values2 = [0, 10, 30, 200, 150, 10, 190, 40]
    sort.playerBubbleSort(values2)

    assert values2 == [0, 10, 10, 30, 40, 150, 190, 200]
    assert max(values2) == 200
    assert min(values2) == 0

    
