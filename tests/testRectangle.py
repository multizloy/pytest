import pytest
import source.shapes as shapes


def testArea(myRectangle):
    assert myRectangle.area() == 10 * 20


def testPerimeter(myRectangle):
    assert myRectangle.perimeter() == (10 * 2) + (20 * 2)


def testNotEqual(myRectangle, weirdRectangle):
    assert myRectangle != weirdRectangle
