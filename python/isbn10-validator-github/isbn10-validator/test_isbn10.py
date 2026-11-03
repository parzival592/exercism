import unittest

from isbn10 import is_valid


class TestISBN10Validator(unittest.TestCase):
    def test_valid_isbn_with_hyphens(self):
        self.assertTrue(is_valid("3-598-21508-8"))

    def test_valid_isbn_without_hyphens(self):
        self.assertTrue(is_valid("3598215088"))

    def test_valid_isbn_with_x_check_character(self):
        self.assertTrue(is_valid("3-598-21507-X"))

    def test_invalid_checksum(self):
        self.assertFalse(is_valid("3598215089"))

    def test_x_in_wrong_position(self):
        self.assertFalse(is_valid("359X215078"))

    def test_wrong_length(self):
        self.assertFalse(is_valid("359821508"))

    def test_invalid_character(self):
        self.assertFalse(is_valid("35982150A8"))

    def test_invalid_checksum_example(self):
        self.assertFalse(is_valid("1234567890"))


if __name__ == "__main__":
    unittest.main()
