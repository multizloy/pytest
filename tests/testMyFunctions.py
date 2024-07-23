import pytest
import source.myFunctions as myFunctions


def testAdd():
    result = myFunctions.add(1, 4)
    assert result == 5
