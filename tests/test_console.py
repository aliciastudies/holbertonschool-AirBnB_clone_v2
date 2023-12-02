#!/usr/bin/python3
""" unittesting console """
import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os
from console import HBNBCommand
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'file')
class TestConsole(unittest.TestCase):
    def setUp(self):
        """ set up: create objects, initialise variables"""
        # create instance of command for each test
        self.command = HBNBCommand()

    def tearDown(self):
        """ clean-up: close, release, revert """
        # reset to original value
        sys.stdout = sys.__stdout__

    def test_do_create(self):
        """ Test the create function """
        with patch('sys.stdout', new=StringIO()) as output:
            self.command.do_create('BaseModel')
            self.assertTrue(len(output.getvalue()) > 0)

            self.command.onecmd('create')
            self.assertIn("** class name missing **\n", output.getvalue())

            self.command.do_create('blah')
            self.assertIn("** class doesn't exist **\n", output.getvalue())

    def test_do_all(self):
        # Test without args
        with patch('sys.stdout', new=StringIO()) as output:
            self.command.onecmd('all')
            self.assertIn("** class name missing **", output.getvalue())

            # Test with args (e.g., 'User')
            self.command.do_all('User')
            self.assertIn('[]', output.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
