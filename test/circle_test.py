#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import math
import pygame
from pygame.rect import Rect
from pygame.circle import Circle


class TestCircle(unittest.TestCase):

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

    def test_collidePoint(self):
        c = Circle(0, 0, 5)

        p1 = (3, 3)
        p2 = (10, 10)

        # colliding single

        self.assertTrue(c.collidePoint(p1),
                        'Expected True, point should collide here')

        # not colliding single

        self.assertFalse(c.collidePoint(p2),
                         'Expected False, point should not collide here'
                         )

    def test_collideCircle(self):
        c = Circle(0, 0, 5)
        c_same = c.copy()
        c2 = Circle(10, 0, 5)
        c3 = Circle(100, 100, 5)
        c4 = Circle(10, 0, 4.999999999999)
        c5 = Circle(0, 0, 2)

        c6 = Circle(10, 0, 7)

        # touching

        self.assertTrue(c.collideCircle(c2),
                        'Expected True, circles should collide here')

        # partly colliding

        self.assertTrue(c.collideCircle(c6),
                        'Expected True, circles should collide here')

        # self colliding

        self.assertTrue(c.collideCircle(c),
                        'Expected True, circles should collide with self'
                        )

        # completely colliding

        self.assertTrue(c.collideCircle(c_same),
                        'Expected True, circles should collide with self'
                        )

        # not touching

        self.assertFalse(c.collideCircle(c3),
                         'Expected False, circles should not collide here'
                         )

        # barely not touching

        self.assertFalse(c.collideCircle(c4),
                         'Expected False, circles should not collide here'
                         )

        # small circle inside big circle

        self.assertTrue(c.collideCircle(c5),
                        'Expected True, circles should collide here')

        # big circle outside small circle

        self.assertTrue(c5.collideCircle(c),
                        'Expected False, circles should collide here')

    def test_collideRect(self):
        msgt = 'Expected True, rect should collide here'
        msgf = 'Expected False, rect should not collide here'

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

    def test_copy(self):
        c = Circle(10, 10, 4)

        # check 1 arg passed

        with self.assertRaises(TypeError):
            c.copy(10)

        # check copied circle has the same attribute values

        c_2 = c.copy()
        self.assertEqual(c.x, c_2.x)
        self.assertEqual(c.y, c_2.y)
        self.assertEqual(c.r, c_2.r)

        # check c2 is not c

        self.assertIsNot(c_2, c)

    def test_move(self):
        """Ensures that moving the circle position correctly updates position"""

        c = Circle(0, 0, 3)

        new_c = c.move(5, 5)

        self.assertEqual(new_c.x, 5.0)
        self.assertEqual(new_c.y, 5.0)
        self.assertEqual(new_c.r, 3.0)

        new_c = new_c.move(-5, -10)

        self.assertEqual(new_c.x, 0.0)
        self.assertEqual(new_c.y, -5.0)

    def test_move_ip(self):
        """Ensures that moving the circle position correctly updates position"""

        c = Circle(0, 0, 3)

        c.move_ip(5, 5)

        self.assertEqual(c.x, 5.0)
        self.assertEqual(c.y, 5.0)
        self.assertEqual(c.r, 3.0)

        c.move_ip(-5, -10)
        self.assertEqual(c.x, 0.0)
        self.assertEqual(c.y, -5.0)

    def test_update(self):
        """Ensures that updating the circle position
        and dimension correctly updates position and dimension"""

        c = Circle(0, 0, 10)

        c.update(5, 5, 3)

        self.assertEqual(c.x, 5.0)
        self.assertEqual(c.y, 5.0)
        self.assertEqual(c.r, 3.0)

    def test_contains(self):
        """Ensures that the contains method correctly determines if a circle is
        contained within the circle"""

        c = Circle(10, 10, 4)
        c2 = Circle(10, 10, 2)
        c3 = Circle(100, 100, 5)
        c4 = Circle(16, 10, 7)

        # self

        self.assertTrue(c.contains(c))

        # contained circle

        self.assertTrue(c.contains(c2))

        # not contained circle

        self.assertFalse(c.contains(c3))

        # intersecting circle

        self.assertFalse(c.contains(c4))


if __name__ == '__main__':
    unittest.main()