import pytest
import source.myFunctions as myFunctions
import time


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


@pytest.mark.slow
def testVerySlow():
    time.sleep(5)
    result = myFunctions.divide(10, 5)
    assert result == 2


@pytest.mark.skip(reason="This feature is currently broken")
def testAdd():
    assert myFunctions.add(10, 5) == 3


@pytest.mark.xfail(reason="we know ew cannot divide by zero")
def testDivideZeroBroken():
    myFunctions.divide(4, 0)
