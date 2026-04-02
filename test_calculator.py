import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    # --- add ---

    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(3, 5), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -4), -6)

    def test_add_positive_and_negative(self):
        self.assertEqual(self.calc.add(10, -3), 7)

    def test_add_zeros(self):
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_add_floats(self):
        self.assertAlmostEqual(self.calc.add(1.1, 2.2), 3.3)

    # --- subtract ---

    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -3), -2)

    def test_subtract_positive_and_negative(self):
        self.assertEqual(self.calc.subtract(5, -3), 8)

    def test_subtract_same_numbers(self):
        self.assertEqual(self.calc.subtract(7, 7), 0)

    def test_subtract_floats(self):
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)

    # --- multiply ---

    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    def test_multiply_positive_and_negative(self):
        self.assertEqual(self.calc.multiply(5, -2), -10)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(99, 0), 0)

    def test_multiply_floats(self):
        self.assertAlmostEqual(self.calc.multiply(2.5, 4.0), 10.0)


if __name__ == "__main__":
    unittest.main()
