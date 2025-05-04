import unittest
from src.homework.j_classes.class_a import Die

class TestDie(unittest.TestCase):

    def test_roll_value_in_range(self):
        die = Die()
        for _ in range(3):  # At least 3 rolls
            die.roll()
            value = die.get_rolled_value()
            self.assertGreaterEqual(value, 1)
            self.assertLessEqual(value, 6)
