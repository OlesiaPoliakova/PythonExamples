import unittest
from Power import power
class TestExample(unittest.TestCase):
    def test_validity(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(3.0, 1), 3)
        self.assertEqual(power(2.0, 0), 1)
        self.assertEqual(power(2.0, -1), 0.5)
