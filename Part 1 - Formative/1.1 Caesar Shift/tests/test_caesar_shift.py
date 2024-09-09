from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import caesar_encode

class TestCaesarShift(TestCase):

    def test_insert_lowercase(self):
        self.assertEqual(caesar_encode('helloworld', 5), 'mjqqtbtwqi')

    def test_insert_space_lowercase(self):
        self.assertEqual(caesar_encode('hello world', 5), 'mjqqt btwqi')