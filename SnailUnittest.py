import unittest
from SnailExample import get_snail_time


class TestExample(unittest.TestCase):
    def test_validity(self):
        self.assertEqual(get_snail_time(10, 2, 1), 9)  # 9 - expected result
        self.assertEqual(get_snail_time(10, 6, 1), 2)  # 2 - expected result
        self.assertEqual(get_snail_time(10, 8, 5), 2)
        self.assertEqual(get_snail_time(10, 11, 1), 1)
        self.assertEqual(get_snail_time(10, 11, 10), 1)
