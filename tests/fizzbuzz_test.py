import unittest
from src.fizzbuzz import fizzbuzz


class TestFizzbuzz(unittest.TestCase):
    def test_3_returns_fizz(self):
        # Arrange
        expected = "Fizz"
        # Act
        actual = fizzbuzz(3)
        # Assert
        self.assertEqual(expected, actual)

    def test_5_returns_buzz(self):
        # Arrange
        expected = "Buzz"
        # Act
        actual = fizzbuzz(5)
        # Assert
        self.assertEqual(expected, actual)

    def test_15_returns_fizzbuzz(self):
        # Arrange
        expected = "FizzBuzz"
        # Act
        actual = fizzbuzz(15)
        # Assert
        self.assertEqual(expected, actual)

    def test_6_returns_fizz(self):
        expected = "Fizz"
        actual = fizzbuzz(6)
        self.assertEqual(expected, actual)

    def test_20_returns_buzz(self):
        expected = "Buzz"
        actual = fizzbuzz(20)
        self.assertEqual(expected, actual)

    def test_7_returns_a_string(self):
        expected = "7"
        actual = fizzbuzz(7)
        self.assertEqual(expected, actual)

    def test_0_returns_error(self):
        with self.assertRaises(ValueError):
            fizzbuzz(0)
    
    def test_negative_num(self):
        expected = "Buzz"
        actual = fizzbuzz(-10)
        self.assertEqual(expected, actual)

        # def test_zero_hours_total(self):
        #     with self.assertRaises(ValueError):
        #         pay = divide_pay(360.0, {"Alice": 0.0, "Bob": 0.0, "Carol": 0.0})
