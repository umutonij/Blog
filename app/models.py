from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))   
    

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    blogs = db.relationship('Blog', backref ='blog',lazy="dynamic")
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    comments = db.relationship('Comment', backref ='comments',lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)
    

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Blog(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer,primary_key = True)
    # name = db.Column(db.String(255)) 
    # category= db.Column(db.String(255))
    comment_blog = db.relationship('Comment', backref ='comment_blog',lazy = "dynamic")
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    blog_title=  db.Column(db.String(255))
    blog_content=  db.Column(db.String(255))
    

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blog(cls,category):
        blogs = Blog.query.filter_by(category=category).all()
        return blog

    @classmethod
    def get_blog(cls,id):
        blog = Blog.query.filter_by(id=id).first()

        return blog

    @classmethod
    def count_blogs(cls,uname):
        user = User.query.filter_by(username=uname).first()
        blogs = Blog.query.filter_by(user_id=user.id).all()

        blogs_count = 0
        for blog in blogs:
            blogs_count += 1

        return blogs_count

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(255)) 
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))
  

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,blog):
        comments = Comment.query.filter_by(blog_id=blog).all()
        return comments



# class Review(db.Model):

#     __tablename__ = 'reviews'

#     id = db.Column(db.Integer,primary_key = True)
#     movie_id = db.Column(db.Integer)
#     movie_title = db.Column(db.String)
#     image_path = db.Column(db.String)
#     movie_review = db.Column(db.String)
#     posted = db.Column(db.DateTime,default=datetime.utcnow)
#     user_id = db.Column(db.Integer,db.ForeignKey("users.id"))