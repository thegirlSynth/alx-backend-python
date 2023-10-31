#!/usr/bin/env python3
"""
Parameterize a unit test
"""

from parameterized import parameterized
import unittest
from unittest.mock import Mock, patch
from utils import (
    get_json,
    access_nested_map,
)


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
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map, path):
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
        my_mock = Mock()
        my_mock.json.return_value = test_payload

        with patch("requests.get", return_value=my_mock) as mock_requests_get:
            result = get_json(test_url)
            self.assertEqual(result, test_payload)
            mock_requests_get.assert_called_once_with(test_url)


if __name__ == "__main__":
    unittest.main()
