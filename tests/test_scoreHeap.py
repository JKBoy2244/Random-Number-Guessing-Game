import pytest
from ScoresOrdering import ScoresOrdering

class TestScoresOrdering:

    def test_left_set(self):
        ordering = ScoresOrdering()
        randomNumbersList = [23, 4567, 566, 786, 145, 7896, 1134, 567]

        assert ordering.left_set(0, randomNumbersList) == 1
        assert ordering.left_set(1, randomNumbersList) == 3
        assert ordering.left_set(2, randomNumbersList) == 5

    def test_right_set(self):
        ordering = ScoresOrdering()
        randomNumbersList = [23, 4567, 566, 786, 145, 7896, 1134, 567]

        assert ordering.right_set(0, randomNumbersList) == 2
        assert ordering.right_set(1, randomNumbersList) == 4
        assert ordering.right_set(2, randomNumbersList) == 6
