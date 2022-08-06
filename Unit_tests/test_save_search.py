import unittest
from save_search import insert_new_data, get_user_data


class InsertData(unittest.TestCase):
    def test_true(self):
        result = insert_new_data("LouisePoole1", "ENGLAND", 5)
        self.assertTrue(result)

    def test_false(self):
        result = insert_new_data("blah", "blah", "blah")  # risk is not a number so ValueError
        self.assertFalse(result)


class GetData(unittest.TestCase):
    def test_true(self):
        result = get_user_data("LouisePoole22")
        self.assertTrue(result)

    def test_false(self):
        result = get_user_data("blah")  # User does not exist so UnboundLocalError for last_area
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
