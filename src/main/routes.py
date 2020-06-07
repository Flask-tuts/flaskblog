from flask import Blueprint, render_template, request
from src.models import Post

main = Blueprint('main', __name__)


@main.route('/')
def index():
    page = request.args.get('page', 1, type=int)

    posts = Post.query.order_by(Post.timestamp.desc()).paginate(per_page=5, page=page)
    return render_template('index.html', title='Home', posts=posts)


@main.route('/about')
def about():
    return render_template('about.html', title='About Us')


@main.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

