import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    def test_discount_with_float_values(self):
        prices = [10.0, 4.5, 20.5]
        expected_discount = 4.5
        self.assertEqual(expected_discount, discount(prices))

    def test_list_smaller_than_three(self):
        prices = [10, 4]
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def test_list_larger_than_three(self):
        prices = [10, 4, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    def test_empty_list(self):
        prices = []
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def test_mixed_list(self):
        prices = [10, 4, 20, 10.10, 100.00]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    def test_matching_list(self):
        prices = [10, 10, 10, 10, 10]
        expected_discount = 10
        self.assertEqual(expected_discount, discount(prices))


if __name__ == '__main__':
    unittest.main()