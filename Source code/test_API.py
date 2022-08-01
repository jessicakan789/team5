import unittest
from API import get_rate_by_location, calculate_risk


class Rate(unittest.TestCase):
    def test_returns_value(self):
        expected = 274  # must keep updating value
        actual = get_rate_by_location("utla", "blackpool")
        self.assertEqual(expected, actual)

    def test_error(self):
        self.assertFalse(get_rate_by_location("utl", "blackpool"))


class Risk(unittest.TestCase):
    def test_low(self):
        expected = "low"
        actual = calculate_risk(0.5)
        self.assertEqual(expected, actual)

    def test_medium(self):
        expected = "medium"
        actual = calculate_risk(1.5)
        self.assertEqual(expected, actual)

    def test_high(self):
        expected = "high"
        actual = calculate_risk(2.5)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
