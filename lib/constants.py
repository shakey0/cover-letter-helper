from lib.base_models import Input, Variables, Paragraph
import re


def process_all_data(all_data):
    inputs = [Input(input_data['name'], input_data['code']) for input_data in all_data['inputs']]
    variables_sets = [Variables(variables_data['name'], variables_data['code'], variables_data['variables'], variables_data['selected']) for variables_data in all_data['variables_sets']]
    paragraphs = [Paragraph(paragraph_data['name'], paragraph_data['text']) for paragraph_data in all_data['paragraphs']]
    return inputs, variables_sets, paragraphs


flash_messages = {
    "new_input": "New input [ {} - {} ] added successfully.",
    "updated_input": "Input [ {} - {} ] updated successfully.",
    "new_variables_set": "New variables set [ {} - {} ] added successfully.",
    "updated_variables_set": "Variables set [ {} - {} ] updated successfully.",
    "new_paragraph": "New paragraph [ {} ] added successfully.",
    "updated_paragraph": "Paragraph [ {} ] updated successfully."
}

def get_flash_message(action, name, code=None):
    return flash_messages[action].format(name, code) if code else flash_messages[action].format(name)


def all_unique(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return item
        seen.add(item)
    return True


def validate_paragraph(text, inputs, variables_sets):
    inputs_in_text = re.findall(r'(##\w+)', text)
    for input in inputs_in_text:
        if input not in [input.code for input in inputs]:
            return "Input '{}' has not been created".format(input)
    variables_in_text = re.findall(r'(\*\*\w+)', text)
    for variable in variables_in_text:
        if variable not in [variables.code for variables in variables_sets]:
            return "Variables set '{}' has not been created".format(variable)
    return True
