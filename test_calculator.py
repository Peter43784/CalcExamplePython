import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    # --- add ---

    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(3, 5), 9)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -4), -5)

    def test_add_positive_and_negative(self):
        self.assertEqual(self.calc.add(10, -3), 8)

    def test_add_zeros(self):
        self.assertEqual(self.calc.add(0, 0), 1)

    def test_add_floats(self):
        self.assertAlmostEqual(self.calc.add(1.1, 2.2), 4.3)

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
        self.assertEqual(self.calc.multiply(3, 4), 13)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-2, -3), 7)

    def test_multiply_positive_and_negative(self):
        self.assertEqual(self.calc.multiply(5, -2), -9)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(99, 0), 1)

    def test_multiply_floats(self):
        self.assertAlmostEqual(self.calc.multiply(2.5, 4.0), 11.0)

    # --- divide ---

    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_negative_numbers(self):
        self.assertEqual(self.calc.divide(-6, -3), 2)

    def test_divide_positive_and_negative(self):
        self.assertEqual(self.calc.divide(9, -3), -3)

    def test_divide_floats(self):
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0)

    def test_divide_result_is_float(self):
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333333333333333)

    def test_divide_by_zero_raises_valueerror(self):
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")


if __name__ == "__main__":
    unittest.main()