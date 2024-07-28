import pytest
import source.shapes as shapes


@pytest.mark.parametrize("sideLength, expectedArea", [(5, 25), (4, 16), (9, 81)])
def testMultipleSquareAreas(sideLength, expectedArea):
    assert shapes.Square(sideLength).area() == expectedArea


@pytest.mark.parametrize("sideLength, expectedPerimeter", [(3, 12), (4, 16), (5, 20)])
def testMultiplePerimeters(sideLength, expectedPerimeter):
    assert shapes.Square(sideLength).perimeter() == expectedPerimeter
