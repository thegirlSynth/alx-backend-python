#!/usr/bin/env python3
"""
Tests methods of the utils module
"""

from parameterized import parameterized
import unittest
from unittest.mock import Mock, patch
from utils import get_json, access_nested_map, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Tests that the utils.access_nested_map method returns
    what it is supposed to.
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Tests the utils.access_nested_map function
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Tests that utils.access-nested_map correctly raises exceptions"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Tests that utils.get_json returns the expected result.
    """

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ],
    )
    def test_get_json(self, test_url, test_payload):
        """
        Tests that utils.get_json functions properly
        """
        my_mock = Mock()
        my_mock.json.return_value = test_payload

        with patch("requests.get", return_value=my_mock) as mock_requests_get:
            result = get_json(test_url)
            self.assertEqual(result, test_payload)
            mock_requests_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Tests that the utils.memoize decorator functions properly.
    """

    def test_memoize(self):
        """
        Creates a Testclass for testing the utils.memoize decorator
        """

        class TestClass:
            """
            Instantiates a test class
            """

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as mocked:
            test_class = TestClass()

            result1 = test_class.a_property
            result2 = test_class.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            mocked.assert_called_once()


if __name__ == "__main__":
    unittest.main()
