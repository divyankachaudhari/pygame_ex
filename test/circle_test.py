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

    def test_collideRect(self):
        msgt = "Expected True, rect should collide here"
        msgf = "Expected False, rect should not collide here"
        # ====================================================
        c = Circle(0, 0, 5)

        r1 = Rect(2, 2, 4, 4)
        r2 = Rect(10, 15, 43, 24)
        r3 = Rect(0, 4.9999999999999, 4, 4)

        # colliding single
        self.assertTrue(c.collideRect(r1), msgt)

        # not colliding single
        self.assertFalse(c.collideRect(r2), msgf)

        # barely colliding single
        self.assertTrue(c.collideRect(r3), msgt)

    
