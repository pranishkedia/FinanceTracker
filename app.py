from flask import Flask, render_template
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)

'''@app.route('/')
def hello_world():
    return render_template('welcome.html', name="Pranish")
'''


from main.views import main_blueprint
app.register_blueprint(main_blueprint)

from users.views import users_blueprint
app.register_blueprint(users_blueprint)

from blog.views import blog_blueprint
app.register_blueprint(blog_blueprint)




if __name__ == '__main__':
    app.run()

