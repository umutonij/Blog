from app.models import Comment,User
from app import db
import unittest

class CommentTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Blogs class
    '''
    def setUp(self):
        self.user_wecode = User(username = 'Wecode',password = '12345', email = 'jacquelineumutoni13@gmail.com')
        self.new_comment = Comment(blog_id=12345,blog_title='Review for blogs',image_path="https://image.tmdb.org/t/p/w500/jdjdjdjn",blog_review='This blog is the best thing since sliced bread',user = self.user_wecode ) 

    def tearDown(self):
        Comment.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.blog_id,12345)
        self.assertEquals(self.new_comment.blog_title,'Review for blogs')
        self.assertEquals(self.new_comment.image_path,"https://image.tmdb.org/t/p/w500/jdjdjdjn")
        self.assertEquals(self.new_comment.blog_comment,'This blog is the best thing since sliced bread')
        self.assertEquals(self.new_comment.user,self.user_wecode) 

    def test_save_comment(self): 
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_get_comment_by_id(self):

        self.new_comment.save_comment()
        got_comments = Comment.get_comments(12345)
        self.assertTrue(len(got_comments) == 1)