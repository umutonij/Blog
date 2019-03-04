import unittest
from app.models import Pitch  
Blog = Blog

class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Blog class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_blog = Blog(133,'killed by excelence')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog,Blog))