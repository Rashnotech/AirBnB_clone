#!/usr/bin/python3
"""Testing the console, for all features!"""


from unittest.mock import patch
from io import StringIO
import unittest
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Testing all the implemented functionality in console"""
    def setUp(self):
        """Setting up the console"""
        self.fake_stdout = StringIO()
        self.patcher = patch('sys.stdout', new=self.fake_stdout)
        self.patcher.start()

    def test_quit_command(self):
        """Test quit command"""
        HBNBCommand().onecmd("quit")
        output = self.fake_stdout.getvalue()
        self.assertIsNotNone(output)

    def test_help_command(self):
        """ Test help command """
        HBNBCommand().onecmd("help")
        output = self.fake_stdout.getvalue()
        assert "Documented commands (type help <topic>):" in output
    
    def test_empty_line(self):
        """ Test empty line """
        HBNBCommand().onecmd(" ")
        output = self.fake_stdout.getvalue()
        self.assertIsNotNone(output)

    def test_create_command(self):
        """Test create command"""
        HBNBCommand().onecmd("create BaseModel")
        output = self.fake_stdout.getvalue()
        self.assertIsNotNone(output)

    def test_show_command(self):
        """Test show command """
        HBNBCommand().onecmd("show BaseModel")
        output = self.fake_stdout.getvalue()
        self.assertIsNotNone(output)

    def test_destroy_command(self):
        """Test all command"""
        HBNBCommand().onecmd("destroy BaseModel")
        output = self.fake_stdout.getvalue()
        assert "** instance id missing **" in output

    def test_all_command(self):
        """Test all command"""
        HBNBCommand().onecmd("all BaseModel")
        output = self.fake_stdout.getvalue()
        assert '[]' in output

    def test_update_command(self):
        """Test update command"""
        HBNBCommand().onecmd("update BaseModel")
        output = self.fake_stdout.getvalue()
        assert "** instance id missing **" in output

    """
    def test_all_command(self):
        Test all command
        HBNBCommand().onecmd("BaseModel.all()")
        output = self.fake_stdout.getvalue()
        self.assertIsNotNone(output)
    
    def test_review_all_command(self):
        Test review all commmand
        HBNBCommand().onecmd("Review.all()")
        output = self.fake_stdout.getvalue()
        self.assertIsNotNone(output)

    def test_user_all_command(self):
        Test User all command
        HBNBCommand().onecmd("User.all()")
        output = self.fake_stdout.getvalue()
        self.assertIsNotNone(output)
    
    def test_state_all(self):
        Test State all command
        HBNBCommand().onecmd("State.all()")
        output = self.fake_stdout.getvalue()
        self.assertIsNotNone(output)

    def test_city_all(self):
        Test city all command
        HBNBCommand().onecmd("City.all()")
        output = self.fake_stdout.getvalue()
        self.assertIsNotNone(output)

    def test_amenity_all(self):
        Test amenity all command
        HBNBCommand().onecmd("Amenity.all()")
        output = self.fake_stdout.getvalue()
        self.assertIsNotNone(output)

    def test_place_all(self):
        HBNBCommand().onecmd("Place.all()")
        output = self.fake_stdout.getvalue()
        self.assertIsNotNone(output)
    """

    def tearDown(self):
        """Tear down the console"""
        self.patcher.stop()


if __name__ == '__main__':
    unittest.main()
