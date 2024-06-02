from flask import request, render_template, url_for, jsonify, flash, Blueprint
from lib.base_data_repository import base_data_repository
from lib.base_models import get_slug
from lib.constants import process_all_data, get_flash_message, all_unique, validate_paragraph


base = Blueprint('base', __name__)


@base.route('/edit_base')
def edit_base():
    action = request.args.get('action')
    if action:
        slug = request.args.get('slug')
        data_type = request.args.get('data_type')
        if action == "deleted":
            flash(data_type[:-1].title().replace('_', ' ') + ' deleted successfully.', 'success emphasise-vars')
        else:
            data = base_data_repository.get_data_by_slug(data_type, slug)
            flash(get_flash_message(action + "_" + data_type[:-1], data['name'], data.get('code')), 'success emphasise-vars')
    all_data = base_data_repository.get_data()
    inputs, variables_sets, paragraphs = process_all_data(all_data)
    return render_template('edit_base.html', inputs=inputs, variables_sets=variables_sets, paragraphs=paragraphs)


@base.route('/update-order', methods=['POST'])
def update_order():
    data = request.get_json()
    order = data['order']
    data_type = data['type']
    base_data_repository.update_order(data_type, order)
    return jsonify(success=True)


@base.route('/add_input', methods=['GET', 'POST'])
def add_input():
    if request.method == 'POST':
        name = request.form['input-name-act-input']
        code = request.form['input-code-act-input']
        result = base_data_repository.add_data('inputs', get_slug(name), name=name, code=code)
        if result != True:
            return jsonify({'error': result})
        return jsonify({'success': True, 'redirect': url_for('base.edit_base', action="new", data_type="inputs", slug=get_slug(name))})
    return render_template('add_input.html')


@base.route('/edit_input/<string:slug>', methods=['GET', 'POST'])
def edit_input(slug):
    if request.method == 'POST':
        name = request.form['input-name-act-input']
        code = request.form['input-code-act-input']
        result = base_data_repository.update_data('inputs', slug, name=name, code=code)
        if result != True:
            return jsonify({'error': result})
        return jsonify({'success': True, 'redirect': url_for('base.edit_base', action="updated", data_type="inputs", slug=get_slug(name))})
    item, used = base_data_repository.get_data_by_slug('inputs', slug, get_used=True)
    return render_template('add_input.html', edit=True, input_name=item['name'], type_code=item['code'], slug=slug, used=used)


@base.route('/delete_input/<string:slug>', methods=['GET', 'POST'])
def delete_input(slug):
    result = base_data_repository.delete_data('inputs', slug)
    # if result != True:
    #     return jsonify({'error': result})
    return jsonify({'success': True, 'redirect': url_for('base.edit_base', action="deleted", data_type="inputs", slug=slug)})


@base.route('/add_variables', methods=['GET', 'POST'])
def add_variables():
    if request.method == 'POST':
        name = request.form['list-name-act-input']
        code = request.form['var-code-act-input']
        variables = request.form.getlist('variables[]')
        is_unique = all_unique(variables)
        if is_unique != True:
            return jsonify({'error': "Variable '{}' is duplicated".format(is_unique)})
        selected = request.form.getlist('by_default[]')
        result = base_data_repository.add_data('variables_sets', get_slug(name), name=name, code=code, variables=variables, selected=selected)
        if result != True:
            return jsonify({'error': result})
        return jsonify({'success': True, 'redirect': url_for('base.edit_base', action="new", data_type="variables_sets", slug=get_slug(name))})
    return render_template('add_variables.html')


@base.route('/edit_variables/<string:slug>', methods=['GET', 'POST'])
def edit_variables(slug):
    if request.method == 'POST':
        name = request.form['list-name-act-input']
        code = request.form['var-code-act-input']
        variables = request.form.getlist('variables[]')
        is_unique = all_unique(variables)
        if is_unique != True:
            return jsonify({'error': "Variable '{}' is duplicated".format(is_unique)})
        selected = request.form.getlist('by_default[]')
        result = base_data_repository.update_data('variables_sets', slug, name=name, code=code, variables=variables, selected=selected)
        if result != True:
            return jsonify({'error': result})
        return jsonify({'success': True, 'redirect': url_for('base.edit_base', action="updated", data_type="variables_sets", slug=get_slug(name))})
    item, used = base_data_repository.get_data_by_slug('variables_sets', slug, get_used=True)
    return render_template('add_variables.html', edit=True, list_name=item['name'], type_code=item['code'],
                           values=item['variables'], selected=item['selected'], slug=slug, used=used)
    
    
@base.route('/delete_variables/<string:slug>', methods=['GET', 'POST'])
def delete_variables(slug):
    result = base_data_repository.delete_data('variables_sets', slug)
    # if result != True:
    #     return jsonify({'error': result})
    return jsonify({'success': True, 'redirect': url_for('base.edit_base', action="deleted", data_type="variables_sets", slug=slug)})


@base.route('/add_paragraph', methods=['GET', 'POST'])
def add_paragraph():
    all_data = base_data_repository.get_data()
    inputs, variables_sets, paragraphs = process_all_data(all_data)
    if request.method == 'POST':
        name = request.form['paragraph-name-act-input']
        text = request.form['paragraph-text-act-input']
        is_valid = validate_paragraph(text, inputs, variables_sets)
        if is_valid != True:
            return jsonify({'error': is_valid})
        result = base_data_repository.add_data('paragraphs', get_slug(name), name=name, text=text)
        if result != True:
            return jsonify({'error': result})
        return jsonify({'success': True, 'redirect': url_for('base.edit_base', action="new", data_type="paragraphs", slug=get_slug(name))})
    return render_template('add_paragraph.html', inputs=inputs, variables_sets=variables_sets)


@base.route('/edit_paragraph/<string:slug>', methods=['GET', 'POST'])
def edit_paragraph(slug):
    all_data = base_data_repository.get_data()
    inputs, variables_sets, paragraphs = process_all_data(all_data)
    if request.method == 'POST':
        name = request.form['paragraph-name-act-input']
        text = request.form['paragraph-text-act-input']
        is_valid = validate_paragraph(text, inputs, variables_sets)
        if is_valid != True:
            return jsonify({'error': is_valid})
        result = base_data_repository.update_data('paragraphs', slug, name=name, text=text)
        if result != True:
            return jsonify({'error': result})
        return jsonify({'success': True, 'redirect': url_for('base.edit_base', action="updated", data_type="paragraphs", slug=get_slug(name))})
    item = base_data_repository.get_data_by_slug('paragraphs', slug)
    return render_template('add_paragraph.html', edit=True, paragraph_name=item['name'], paragraph_text=item['text'],
                           inputs=inputs, variables_sets=variables_sets, slug=slug)
    
    
@base.route('/delete_paragraph/<string:slug>', methods=['GET', 'POST'])
def delete_paragraph(slug):
    result = base_data_repository.delete_data('paragraphs', slug)
    # if result != True:
    #     return jsonify({'error': result})
    return jsonify({'success': True, 'redirect': url_for('base.edit_base', action="deleted", data_type="paragraphs", slug=slug)})
