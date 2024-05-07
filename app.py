from flask import Flask, request, render_template
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


class Input:
    def __init__(self, name, code):
        self.name = name
        self.code = code

class Variables:
    def __init__(self, name, code, values):
        self.name = name
        self.code = code
        self.values = values

class Paragraph:
    def __init__(self, name, text):
        self.name = name
        self.text = text
        self.slug = name.lower().replace(' ', '_')

@app.route('/edit_base')
def edit_base():
    inputs = [
        Input('Company Name', '##cn'),
        Input('Industry', '##in'),
        Input('Job Title', '##jt'),
        Input('Job Focus', '##jf')
    ]
    variables_sets = [
        Variables('Frontend', '**fr', ['JavaScript', 'React', 'HTML', 'CSS']),
        Variables('Backend', '**ba', ['Python', 'Flask', 'Django', 'PostgreSQL', 'Ruby', 'Rails', 'Node.js', 'Express', 'MongoDB', 'Java', 'Spring']),
        Variables('DevOps', '**de', ['Docker', 'Kubernetes', 'AWS', 'Terraform']),
        Variables('Product Management', '**pm', ['Agile', 'Scrum', 'Jira', 'Product Roadmap']),
        Variables('Soft Skills', '**ss', ['Communication', 'Problem Solving', 'Teamwork', 'Time Management'])
    ]
    var_codes = ['**ba', '**de', '**ss', '**pm', '**ba', '**fr', '**de', '**ss', '**fr', '**pm']
    var_codes = [f'<strong style="color: black; text-shadow: 0.5px 0.5px 1px rgba(0, 0, 0, 0.3);">{var_code}</strong>' for var_code in var_codes]
    paragraphs = [
        Paragraph('Introduction', f'Official wonder result {var_codes[0]} crime item be fact. Than answer happy break. Likely school turn security service perform surface. Care account how figure author. Run instead evidence direction add {var_codes[1]}. Company experience provide reach sing. Discuss particularly these kitchen where police most. Nearly same effect. Color {var_codes[2]} girl generation professor writer trade result. Beyond year out challenge much over only.'),
        Paragraph('Experience', f'Deal relate individual attorney. Want will attack check dark {var_codes[3]} charge white. Customer challenge rich {var_codes[4]} trade exactly. Western deal writer small. Decade you rock else. Shoulder little white prevent western public {var_codes[5]}. Interesting wear chair really wish Democrat discover. Nothing wife too front heart than church pull. Police civil before team society {var_codes[6]} common strategy. Rather traditional eye less even including.'),
        Paragraph('Skills', f'Factor international usually herself benefit though need meeting {var_codes[7]}. Instead personal dark would appear difference state. Culture ten represent appear allow find language {var_codes[8]} music. Ball blood require reduce person while. Court education general support best always study. Citizen memory can. Person itself letter morning return buy fund. Scene many capital money support expert {var_codes[9]}. Board again candidate among child daughter their. Among event although likely turn.')
    ]
    return render_template('edit_base.html', inputs=inputs, variables_sets=variables_sets, paragraphs=paragraphs)

@app.route('/add_input')
def add_input():
    return render_template('add_input.html')

@app.route('/edit_input')
def edit_input():
    return render_template('add_input.html', edit=True, input_name='Company Name', type_code='##cn')

@app.route('/add_variables')
def add_variables():
    return render_template('add_variables.html')

@app.route('/edit_variables')
def edit_variables():
    return render_template('add_variables.html', edit=True, list_name='Frontend', type_code='**fr', values=['JavaScript', 'React', 'HTML', 'CSS'])

@app.route('/add_paragraph')
def add_paragraph():
    return render_template('add_paragraph.html')

@app.route('/edit_paragraph')
def edit_paragraph():
    return render_template('add_paragraph.html', edit=True, paragraph_name='Introduction', paragraph_text='Official wonder result **ba crime item be fact. Than answer happy break. Likely school turn security service perform surface. Care account how figure author. Run instead evidence direction add **de. Company experience provide reach sing. Discuss particularly these kitchen where police most. Nearly same effect. Color **fr here certainly house on first.')

@app.route('/drag_test')
def drag_test():
    return render_template('drag_test.html')


if __name__ == '__main__':
    app.run(debug=True)
