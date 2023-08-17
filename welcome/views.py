from flask import Blueprint, render_template
welcome_blueprint = Blueprint('welcome', __name__, template_folder='templates')

@welcome_blueprint.route('/')
def welcome():
    return render_template('welcome.html', name='Pranish')