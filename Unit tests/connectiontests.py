"""TESTING CORRECT, INCORRECT AND BOUNDARY INPUT FOR THE return_population FUNCTION"""

import unittest
from Population import return_population


class TestConnection(unittest.TestCase):
    def test_population_true(self):
        expected = (563851)
        actual = return_population('somerset')

        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()

class TestConnection(unittest.TestCase):
    def test_population_false(self):
        expected = (563851)
        actual = return_population(1234)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()



class TestConnection(unittest.TestCase):
    def test_population_boundary(self):
        expected = (563851)
        actual = return_population('SomERseT')

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()