import unittest

from main.geowox_main import reverse_sum


class TestCase(unittest.TestCase):
    def test_that_24_1_returns_34(self):
        """
        first parameter to the function: int.
        second parameter to the function: int.
        :return: int
        """
        self.assertEqual(reverse_sum(24, 1), 34)

    def test_that_0_neg1_returns_neg1(self):
        """
         first parameter to the function: int.
        second parameter to the function: int.
        :return: int
        """
        self.assertEqual(reverse_sum(0, -1), -1)

    def test_that_a_bc_returns_0(self):
        """
        first parameter to the function: char.
        second parameter to the function: string.
        :return: int
        """
        self.assertEqual(reverse_sum("a", "bc"), 0)

    def test_that_1_a_returns_0(self):
        """
        first parameter to the function: int.
        second parameter to the function: char.
        :return: int
        """
        self.assertEqual(reverse_sum(1, 'a'), 0)

    def test_that_a_2_returns_0(self):
        """
        first parameter to the function: char.
        second parameter to the function: int.
        :return: int
        """
        self.assertEqual(reverse_sum('a', 2), 0)

    def test_that_float_neg3_returns_0(self):
        """
        first parameter to the function: float.
        second parameter to the function: int.
        :return: int
        """
        self.assertEqual(reverse_sum(2.12, -3), 0)


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
