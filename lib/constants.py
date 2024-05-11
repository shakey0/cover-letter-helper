from lib.base_models import Input, Variables, Paragraph


def process_all_data(all_data):
    inputs = [Input(input_data['name'], input_data['code']) for input_data in all_data['inputs']]
    variables_sets = [Variables(variables_data['name'], variables_data['code'], variables_data['variables']) for variables_data in all_data['variables_sets']]
    paragraphs = [Paragraph(paragraph_data['name'], paragraph_data['text']) for paragraph_data in all_data['paragraphs']]
    return inputs, variables_sets, paragraphs
