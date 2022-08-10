import unittest
from db_utils import get_password
from unittest import mock
from unittest.mock import patch

class TestGetPassword(unittest.TestCase):
    @patch('db_utils.get_password')
    def test_get_password_true(self, mock_username):
        username = "LouisePoole"
        mock_username.return_value = username
        expected = ('', True)
        actual = get_password(mock_username)
        self.assertEqual(expected, actual)

