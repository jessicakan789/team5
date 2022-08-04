import unittest
from predict import *

class TestGetSimilarWord(unittest.TestCase):
    def test_misspelt(self):
        list = ['salford','manchester','bolton']
        threshold = 0.7
        input  = 'saalford'

        self.assertEqual(get_similar_word(list,input,threshold)[1][0], 'salford')  # add assertion here

    def test_different_case(self):
        list = ['salford', 'manchester', 'bolton']
        threshold = 0.7
        input = 'ManChESTer'

        self.assertEqual(get_similar_word(list, input, threshold)[1][0], 'manchester')  # add assertion here

    def test_trailing_spaces(self):
        list = ['salford', 'manchester', 'bolton']
        threshold = 0.7
        input = ' manchester  '
        self.assertEqual(get_similar_word(list, input, threshold)[1][0], 'manchester')

    def test_two_similar(self):
        list = ['saalford', 'sallford','manchester', 'bolton']
        threshold = 0.7
        input = 'salford'
        self.assertEqual(get_similar_word(list, input, threshold)[1], ['saalford', 'sallford'])

    def test_no_similar(self):
        list = ['salford','manchester','bolton']
        threshold = 0.7
        input = 'london'
        self.assertIsNone(get_similar_word(list, input, threshold))





# class TestGetSimilarFunc(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here
#
#
# class TestGetUserInputFunc(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion hereGe



if __name__ == '__main__':
    unittest.main()
