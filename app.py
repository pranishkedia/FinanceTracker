from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('welcome.html', name="Pranish")

if __name__ == '__main__':
    app.run()