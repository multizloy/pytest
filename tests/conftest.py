import pytest
import source.shapes as shapes


@pytest.fixture
def myRectangle():
    return shapes.Rectangle(10, 20)


@pytest.fixture
def weirdRectangle():
    return shapes.Rectangle(5, 6)
