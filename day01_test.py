import unittest
import day01

class Test(unittest.TestCase):

    def test_get_safe_position_exceptions(self):
        with self.assertRaises(ValueError):
            day01.get_safe_position(0, "")

        with self.assertRaises(ValueError):
            day01.get_safe_position(0, "J")

        with self.assertRaises(ValueError):
            day01.get_safe_position(0, "L")

        with self.assertRaises(ValueError):
            day01.get_safe_position(0, "R")

        with self.assertRaises(ValueError):
            day01.get_safe_position(0, "RABC")

        with self.assertRaises(ValueError):
            day01.get_safe_position(0, "LABC")

        with self.assertRaises(ValueError):
            day01.get_safe_position(0, "L-1")

        with self.assertRaises(ValueError):
            day01.get_safe_position(0, "R-1")

    def test_get_safe_position(self):
        # Simple cases
        self.assertEqual(day01.get_safe_position(0, "R1")[0], 1)
        self.assertEqual(day01.get_safe_position(5, "L1")[0], 4)
        self.assertEqual(day01.get_safe_position(0, "R100")[0], 0)

        # Wrapping to the right
        self.assertEqual(day01.get_safe_position(0, "R100")[0], 0)
        self.assertEqual(day01.get_safe_position(89, "R11")[0], 0)
        self.assertEqual(day01.get_safe_position(90, "R12")[0], 2)
        self.assertEqual(day01.get_safe_position(1, "R100")[0], 1)
        self.assertEqual(day01.get_safe_position(5, "R510")[0], 15)
        self.assertEqual(day01.get_safe_position(0, "R300")[0], 0)

        # Wrapping to the left
        self.assertEqual(day01.get_safe_position(0, "L100")[0], 0)
        self.assertEqual(day01.get_safe_position(1, "L1")[0], 0)
        self.assertEqual(day01.get_safe_position(1, "L2")[0], 99)
        self.assertEqual(day01.get_safe_position(1, "L100")[0], 1)
        self.assertEqual(day01.get_safe_position(5, "L200")[0], 5)
        self.assertEqual(day01.get_safe_position(5, "L510")[0], 95)

    def test_zero_cross(self):
        # No crosses
        self.assertEqual(day01.get_safe_position(0, "L1")[1], 0)
        self.assertEqual(day01.get_safe_position(0, "R1")[1], 0)
        self.assertEqual(day01.get_safe_position(10, "L1")[1], 0)
        self.assertEqual(day01.get_safe_position(10, "R1")[1], 0)

        # Cross zero once
        self.assertEqual(day01.get_safe_position(50, "R80")[1], 1)
        self.assertEqual(day01.get_safe_position(50, "R50")[1], 1)
        self.assertEqual(day01.get_safe_position(0, "R100")[1], 1)
        self.assertEqual(day01.get_safe_position(0, "R110")[1], 1)

        self.assertEqual(day01.get_safe_position(50, "L80")[1], 1)
        self.assertEqual(day01.get_safe_position(50, "L50")[1], 1)
        self.assertEqual(day01.get_safe_position(0, "L100")[1], 1)
        self.assertEqual(day01.get_safe_position(0, "L110")[1], 1)

        # Multiple crosses
        self.assertEqual(day01.get_safe_position(99, "R210")[1], 3)
        self.assertEqual(day01.get_safe_position(0, "R210")[1], 2)
        self.assertEqual(day01.get_safe_position(50, "R150")[1], 2)
        self.assertEqual(day01.get_safe_position(50, "R180")[1], 2)
        self.assertEqual(day01.get_safe_position(50, "R150")[1], 2)
        self.assertEqual(day01.get_safe_position(0, "R200")[1], 2)
        self.assertEqual(day01.get_safe_position(0, "R210")[1], 2)

        self.assertEqual(day01.get_safe_position(1, "L210")[1], 3)
        self.assertEqual(day01.get_safe_position(0, "L210")[1], 2)
        self.assertEqual(day01.get_safe_position(50, "L150")[1], 2)
        self.assertEqual(day01.get_safe_position(50, "L180")[1], 2)
        self.assertEqual(day01.get_safe_position(50, "L150")[1], 2)
        self.assertEqual(day01.get_safe_position(0, "L200")[1], 2)
        self.assertEqual(day01.get_safe_position(0, "L210")[1], 2)


