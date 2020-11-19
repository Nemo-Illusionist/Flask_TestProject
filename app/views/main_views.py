from flask import render_template, Blueprint

main = Blueprint('main', __name__, url_prefix='/')


@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html', title='Home')
