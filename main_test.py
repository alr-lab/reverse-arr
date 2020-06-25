import main
import unittest


class TestReverseArray(unittest.TestCase):
    def test_simple_integer_array(self):
        self.assertEqual([4, 3, 2, 1], main.reverse_array([1, 2, 3, 4]))

    def test_simple_string_array(self):
        self.assertEqual(['def', 'abc'], main.reverse_array(['abc', 'def']))

    def test_empty_array_will_not_fail(self):
        self.assertEqual([], main.reverse_array([]))
