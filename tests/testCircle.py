import pytest
import source.shapes as shapes
import math


class testCircle:
    def setupMethod(self, method):
        print(f"Setting up {method}")
        self.circle = shapes.Circle(10)

    def teardownMethod(self, method):
        print(f"Tearing down {method}")


    def testArea(self):
        assert self.circle.area() == math.pi * self.circle.radius**2
