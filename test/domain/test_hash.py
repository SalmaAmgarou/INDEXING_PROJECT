import unittest
from src.domain.hash import Hash


class TestHash(unittest.TestCase):

    def setUp(self):
        self.hash_object = Hash()

    def test_should_return_key_mod(self):
        self.assertEqual(self.hash_object.hash_function(24), 1, "Wrong mod keey")

    def test_should_insert_key_on_address(self):
        self.assertEqual(self.hash_object.insert_key(24, 'Element'), 1, "Wrong address!")

    def test_should_insert_key_on_next_address(self):
        self.assertEqual(self.hash_object.insert_key(48, 'Element'), 2, "Wrong address!")
