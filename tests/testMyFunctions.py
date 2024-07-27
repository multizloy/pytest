import pytest
import source.myFunctions as myFunctions


def testAdd():
    result = myFunctions.add(1, 4)
    assert result == 5


def testDivide():
    result = myFunctions.divide(10, 5)
    assert result == 2


def testDivideByZero():
    with pytest.raises(ValueError):
        myFunctions.divide(10, 0)


def testAddStrings():
    result = myFunctions.add("i like ", "burgers")
    assert result == "i like burgers"
