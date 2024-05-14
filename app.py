from flask import Flask, request, render_template, redirect, url_for, jsonify, flash
from lib.base_data_repository import base_data_repository
from lib.base_models import get_slug
from lib.constants import process_all_data, get_flash_message
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


@app.route('/edit_base')
def edit_base():
    action = request.args.get('action')
    if action:
        slug = request.args.get('slug')
        data_type = request.args.get('data_type')
        data = base_data_repository.get_data_by_slug(data_type, slug)
        flash(get_flash_message(action + "_" + data_type[:-1], data['name'], data.get('code')), 'success emphasise-vars')
    all_data = base_data_repository.get_data()
    inputs, variables_sets, paragraphs = process_all_data(all_data)
    return render_template('edit_base.html', inputs=inputs, variables_sets=variables_sets, paragraphs=paragraphs)


@app.route('/add_input', methods=['GET', 'POST'])
def add_input():
    if request.method == 'POST':
        name = request.form['input-name-act-input']
        code = request.form['input-code-act-input']
        result = base_data_repository.add_data('inputs', get_slug(name), name=name, code=code)
        if result != True:
            return jsonify({'error': result})
        return jsonify({'success': True, 'redirect': url_for('edit_base', action="new", data_type="inputs", slug=get_slug(name))})
    return render_template('add_input.html')


@app.route('/edit_input/<string:slug>', methods=['GET', 'POST'])
def edit_input(slug):
    if request.method == 'POST':
        name = request.form['input-name-act-input']
        code = request.form['input-code-act-input']
        result = base_data_repository.update_data('inputs', slug, name=name, code=code)
        if result != True:
            return jsonify({'error': result})
        return jsonify({'success': True, 'redirect': url_for('edit_base', action="updated", data_type="inputs", slug=get_slug(name))})
    item = base_data_repository.get_data_by_slug('inputs', slug)
    return render_template('add_input.html', edit=True, input_name=item['name'], type_code=item['code'], slug=slug)


@app.route('/add_variables', methods=['GET', 'POST'])
def add_variables():
    if request.method == 'POST':
        name = request.form['list-name-act-input']
        code = request.form['var-code-act-input']
        variables = request.form.getlist('variables[]')
        selected = request.form.getlist('by_default[]')
        result = base_data_repository.add_data('variables_sets', get_slug(name), name=name, code=code, variables=variables, selected=selected)
        if result != True:
            return jsonify({'error': result})
        return jsonify({'success': True, 'redirect': url_for('edit_base', action="new", data_type="variables_sets", slug=get_slug(name))})
    return render_template('add_variables.html')


@app.route('/edit_variables/<string:slug>', methods=['GET', 'POST'])
def edit_variables(slug):
    if request.method == 'POST':
        name = request.form['list-name-act-input']
        code = request.form['var-code-act-input']
        variables = request.form.getlist('variables[]')
        selected = request.form.getlist('by_default[]')
        result = base_data_repository.update_data('variables_sets', slug, name=name, code=code, variables=variables, selected=selected)
        if result != True:
            return jsonify({'error': result})
        return jsonify({'success': True, 'redirect': url_for('edit_base', action="updated", data_type="variables_sets", slug=get_slug(name))})
    item = base_data_repository.get_data_by_slug('variables_sets', slug)
    return render_template('add_variables.html', edit=True, list_name=item['name'], type_code=item['code'],
                           values=item['variables'], selected=item['selected'], slug=slug)


@app.route('/add_paragraph', methods=['GET', 'POST'])
def add_paragraph():
    if request.method == 'POST':
        name = request.form['paragraph-name-act-input']
        text = request.form['paragraph-text-act-input']
        result = base_data_repository.add_data('paragraphs', get_slug(name), name=name, text=text)
        if result != True:
            return jsonify({'error': result})
        return jsonify({'success': True, 'redirect': url_for('edit_base', action="new", data_type="paragraphs", slug=get_slug(name))})
    all_data = base_data_repository.get_data()
    inputs, variables_sets, paragraphs = process_all_data(all_data)
    return render_template('add_paragraph.html', inputs=inputs, variables_sets=variables_sets)


@app.route('/edit_paragraph/<string:slug>', methods=['GET', 'POST'])
def edit_paragraph(slug):
    if request.method == 'POST':
        name = request.form['paragraph-name-act-input']
        text = request.form['paragraph-text-act-input']
        result = base_data_repository.update_data('paragraphs', slug, name=name, text=text)
        if result != True:
            return jsonify({'error': result})
        return jsonify({'success': True, 'redirect': url_for('edit_base', action="updated", data_type="paragraphs", slug=get_slug(name))})
    item = base_data_repository.get_data_by_slug('paragraphs', slug)
    all_data = base_data_repository.get_data()
    inputs, variables_sets, paragraphs = process_all_data(all_data)
    return render_template('add_paragraph.html', edit=True, paragraph_name=item['name'], paragraph_text=item['text'],
                           inputs=inputs, variables_sets=variables_sets, slug=slug)


@app.route('/drag_test')
def drag_test():
    return render_template('drag_test.html')


if __name__ == '__main__':
    app.run(debug=True)
