from flask import Flask, render_template
from routes.base import base
from faker import Faker
fake = Faker()
import os

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
    if os.environ.get('APP_ENV') == 'test':
        root_dir = os.environ.get('ROOT_DIR')
        print('Current working directory:', root_dir)
        os.chdir(root_dir)
    app.run(
        host="0.0.0.0",
        debug=True,
        port=int(os.environ.get('PORT', 5000))
    )
