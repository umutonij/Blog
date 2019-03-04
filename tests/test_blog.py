import unittest
from app.models import Blog

class PostModelTest(unittest.TestCase):

    def setUp(self):
        self.new_blog= Blog(id = 1, blog_title = 'Python', blog_content = 'Programming language that helps to build application')


    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog, Blog))

    

if __name__ == '__main__':
    unittest.main()