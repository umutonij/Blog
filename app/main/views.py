from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Blog,Comment
from .. import db,photos
from .forms import UpdateProfile,BlogForm,CommentForm
from flask_login import current_user,login_required
import datetime


@main.route('/')
def index():
    inkoko = Blog.query.all()
    print(inkoko)
    imishwi=Comment.query.all()

    return render_template('index.html', title = 'Blog App - Home' ,inkoko=inkoko,imishwi=imishwi)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    blog_count = Blog.count_blogs(uname)

    if user is None:
        abort(404)

    return render_template('profile/profile.html',user = user, blogs = blog_count)


@main.route('/user/<uname>/update', methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname = user.username))

    return render_template('profile/update.html', form = form)


@main.route('/user/<uname>/update/pic', methods = ['POST'])
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()

    return redirect(url_for('main.profile', uname = uname))


@main.route('/blog/new', methods = ['GET','POST'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        blog = form.text.data
        # category = form.category.data
        

        new_blog = Blog(blog_title = title,blog_content = blog)
        new_blog.save_blog()
        return redirect(url_for('main.index'))

    title = 'New Blog'
    return render_template('new_blog.html', title = title, blog_form = form)

@main.route('/blog/<int:id>', methods = ["GET","POST"])
def blog(id):
    blog = Blog.get_blog(id)
    posted_date = blog.posted.strftime('%b %d, %Y')
    if request.args.get('like'):
        blog.likes += 1

        db.session.add(blog)
        db.session.commit()

        return redirect(url_for('.blog', id = blog.id))

    elif request.args.get('dislike'):
        blog.dislikes += 1

        db.session.add(blog)
        db.session.commit()

        return redirect(url_for('.blog', id = blog.id))

    form = CommentForm()
    if form.validate_on_submit():
        comment = form.text.data

        new_comment = Comment(comment = comment, user = current_user, blog_id = blog)

        new_comment.save_comment()

    comments = Comment.get_comments(blog)

    return render_template('blog.html', blog = blog, comment_form = form,comments = comments, date = posted_date)

@main.route('/user/<uname>/blogs', methods = ['GET','POST'])
def user_blogs(uname):
    user = User.query.filter_by(username = uname).first()
    blogs = Blog.query.filter_by(user_id = user.id).all()
    blog_count = Blog.count_blogs(uname)

    return render_template('profile/blogs.html', user = user, blogs = blogs, blogs_count = blog_count)
@main.route('/newComment/', methods = ['GET','POST'])
@login_required
def form():
  
    # pitch = Blog.query.filter_by(id = id).first()
    # if pitch is None:
    #     abort(404)

    form = CommentForm()

    if form.validate_on_submit():
        comment = form.text.data

        new_comment = Comment(comment = comment, user_id = current_user.id)

        new_comment.save_comment()
        return redirect(url_for('.index'))
   

    return render_template('new_coment.html', form = form)

@main.route('/delete_blog/<id>', methods=['GET', 'POST'])
def delete_blog(id):
    blog = Delete.query.filter_by(id=id).first()

    db.session.delete(blog)
    db.session.commit()

    return redirect(url_for('main.all_blogs'))