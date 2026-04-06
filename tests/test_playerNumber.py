import pytest
from NumberOfPlayers import NumberOfPlayers

class TestPlayerNumber:

    def test_input(self):
        number = NumberOfPlayers()
        value = 4
        result = number.Input(value)

        assert result == "Successful"
