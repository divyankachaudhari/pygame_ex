import unittest
import math
import pygame
from pygame import circle, rect
class TestCircle(unittest.TestCase):
    """
    test area - done
    circumference - done
    diameter - done
    collidePoint
    collideCircle
    collideRect
    copy, move, update, contains
    union, union all
    """

    def test_area(self):
        """Ensures the area is calculated correctly."""
        c = Circle(0, 0, 1)

        self.assertEqual(c.area, math.pi)

    def test_circumference(self):
        """Ensures the circumference is calculated correctly."""
        c = Circle(0, 0, 1)

        self.assertEqual(c.circumference, math.tau)

    def test_diameter(self):
        """Ensures the diameter is calculated correctly."""
        c = Circle(0, 0, 1)

        self.assertEqual(c.diameter, 2.0)