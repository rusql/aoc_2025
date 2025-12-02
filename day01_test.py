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
        self.assertEqual(day01.get_safe_position(0, "R1"), 1)
        self.assertEqual(day01.get_safe_position(5, "L1"), 4)
        self.assertEqual(day01.get_safe_position(0, "R100"), 0)

        # Wrapping to the right
        self.assertEqual(day01.get_safe_position(0, "R100"), 0)
        self.assertEqual(day01.get_safe_position(89, "R11"), 0)
        self.assertEqual(day01.get_safe_position(90, "R12"), 2)
        self.assertEqual(day01.get_safe_position(1, "R100"), 1)
        self.assertEqual(day01.get_safe_position(5, "R510"), 15)
        self.assertEqual(day01.get_safe_position(0, "R300"), 0)

        # Wrapping to the left
        self.assertEqual(day01.get_safe_position(0, "L100"), 0)
        self.assertEqual(day01.get_safe_position(1, "L1"), 0)
        self.assertEqual(day01.get_safe_position(1, "L2"), 99)
        self.assertEqual(day01.get_safe_position(1, "L100"), 1)
        self.assertEqual(day01.get_safe_position(5, "L200"), 5)
        self.assertEqual(day01.get_safe_position(5, "L510"), 95)

