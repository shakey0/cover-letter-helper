from flask import Flask, render_template
from routes.base import base
from faker import Faker
fake = Faker()

app = Flask(__name__)
app.secret_key = 'secret_key'


class CoverLetter:
    def __init__(self, name):
        self.name = name

@app.route('/')
def index():
    cover_letters = [
        CoverLetter('Super Fridges Ltd.'),
        CoverLetter('International Business Machines Corp.'),
        CoverLetter('The Coca-Cola Company')
    ]
    return render_template('index.html', cover_letters=cover_letters)


app.register_blueprint(base)


@app.route('/drag_test')
def drag_test():
    return render_template('drag_test.html')


if __name__ == '__main__':
    app.run(debug=True)
