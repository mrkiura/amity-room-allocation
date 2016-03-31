import unittest
import app
from amity import Amity


class AppTest(unittest.TestCase):

    # def setUp(self):

    def test_app_initialization(self):
        '''
        Test whether the init_app method returns
        an instance of class Amity
        '''
        result = app.init_app()
        self.assertIsInstance(result, Amity)
