import unittest
from API import get_rate_by_location, calculate_risk


class RateTest(unittest.TestCase):
    def test_returns_value(self):
        expected = int
        actual = type(get_rate_by_location("utla", "blackpool"))
        self.assertEqual(expected, actual)

    def test_error(self):
        self.assertFalse(get_rate_by_location("utl", "blackpool"))  # spelling error in level


class RiskTest(unittest.TestCase):
    def test_low(self):
        expected = "low"
        actual = calculate_risk(0.05)
        self.assertEqual(expected, actual)

    def test_medium(self):
        expected = "medium"
        actual = calculate_risk(0.15)
        self.assertEqual(expected, actual)

    def test_high(self):
        expected = "high"
        actual = calculate_risk(0.25)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
