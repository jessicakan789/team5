import unittest
from area_advice import provide_advice


class ProvideAdvice(unittest.TestCase):
    def test_england(self):
        with self.assertRaises(FileNotFoundError):  # unit test cannot read files
            provide_advice("England")

    def test_utla(self):
        with self.assertRaises(FileNotFoundError):  # unit test cannot read files
            provide_advice("Aberdeen City")

    def test_false(self):
        result = provide_advice("blah")  # location does not exist so returns False
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
