"""TESTING CORRECT, INCORRECT AND BOUNDARY INPUT FOR THE return_population FUNCTION"""

import unittest
from Population import return_population


class TestConnection(unittest.TestCase):                #location does exist
    def test_population_true(self):
        expected = (int(563851))
        actual = return_population('somerset')
        self.assertEqual(expected, actual)

    def test_population_false(self):
        self.assertFalse(return_population('hello'))  # location does not exist

    def test_population_boundary(self):
        expected = (563851)
        actual = return_population('SomERseT')  # some letters capitalised
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()