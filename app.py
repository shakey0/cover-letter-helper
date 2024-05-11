from flask import Flask, request, render_template, redirect, url_for
from lib.base_data_repository import base_data_repository
from lib.base_models import get_slug
from lib.constants import process_all_data
from faker import Faker
fake = Faker()

app = Flask(__name__)


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


@app.route('/edit_base')
def edit_base():
    all_data = base_data_repository.get_data()
    inputs, variables_sets, paragraphs = process_all_data(all_data)
    return render_template('edit_base.html', inputs=inputs, variables_sets=variables_sets, paragraphs=paragraphs)


@app.route('/add_input', methods=['GET', 'POST'])
def add_input():
    if request.method == 'POST':
        name = request.form['input-name-act-input']
        code = request.form['input-code-act-input']
        slug = get_slug(name)
        base_data_repository.add_data('inputs', name=name, code=code, slug=slug)
        return redirect(url_for('edit_base'))
    return render_template('add_input.html')


@app.route('/edit_input/<string:slug>')
def edit_input(slug):
    item = base_data_repository.get_data_by_slug('inputs', slug)
    return render_template('add_input.html', edit=True, input_name=item['name'], type_code=item['code'])


@app.route('/add_variables')
def add_variables():
    return render_template('add_variables.html')


@app.route('/edit_variables/<string:slug>')
def edit_variables(slug):
    item = base_data_repository.get_data_by_slug('variables_sets', slug)
    return render_template('add_variables.html', edit=True, list_name=item['name'], type_code=item['code'], values=item['variables'])


@app.route('/add_paragraph')
def add_paragraph():
    all_data = base_data_repository.get_data()
    inputs, variables_sets, paragraphs = process_all_data(all_data)
    return render_template('add_paragraph.html', inputs=inputs, variables_sets=variables_sets)


@app.route('/edit_paragraph/<string:slug>')
def edit_paragraph(slug):
    item = base_data_repository.get_data_by_slug('paragraphs', slug)
    all_data = base_data_repository.get_data()
    inputs, variables_sets, paragraphs = process_all_data(all_data)
    return render_template('add_paragraph.html', edit=True, paragraph_name=item['name'], paragraph_text=item['text'], inputs=inputs, variables_sets=variables_sets)


@app.route('/drag_test')
def drag_test():
    return render_template('drag_test.html')


if __name__ == '__main__':
    app.run(debug=True)
