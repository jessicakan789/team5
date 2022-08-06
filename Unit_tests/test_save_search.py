import unittest
from save_search import insert_new_data, get_user_data


class InsertData(unittest.TestCase):
    def test_true(self):
        result = insert_new_data("LouisePoole1", "ENGLAND", 5)
        self.assertTrue(result)

    def test_false(self):
        result = insert_new_data("LouisePoole1", "england", "5")
        self.assertTrue(result)


# class GetData(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
