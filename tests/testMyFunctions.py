import pytest
import source.myFunctions as myFunctions


def testAdd():
    result = myFunctions.add(1, 4)
    assert result == 5


def testDivide():
    result = myFunctions.divide(10, 5)
    assert result == 2
