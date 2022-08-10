import unittest
from yes_no_input import get_yes_no_input


class YesNoTest(unittest.TestCase):
    def test_yes(self):
        result = get_yes_no_input("y/n? ")  # enter "y"
        self.assertTrue(result)

    def test_no(self):
        result = get_yes_no_input("y/n? ")  # enter "n"
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
