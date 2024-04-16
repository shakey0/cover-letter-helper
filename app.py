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


class Variables:
    def __init__(self, name, values):
        self.name = name
        self.values = values

class Paragraph:
    def __init__(self, name, text):
        self.name = name
        self.text = text
        self.slug = name.lower().replace(' ', '_')

@app.route('/edit_base')
def edit_base():
    variables_set = [
        Variables('Frontend', ['JavaScript', 'React', 'HTML', 'CSS']),
        Variables('Backend', ['Python', 'Flask', 'Django', 'PostgreSQL', 'Ruby', 'Rails', 'Node.js', 'Express', 'MongoDB', 'Java', 'Spring']),
        Variables('DevOps', ['Docker', 'Kubernetes', 'AWS', 'Terraform']),
        Variables('Product Management', ['Agile', 'Scrum', 'Jira', 'Product Roadmap']),
        Variables('Soft Skills', ['Communication', 'Problem Solving', 'Teamwork', 'Time Management'])
    ]
    lorem_texts = [" ".join(fake.sentences(nb=10)) for _ in range(3)]
    paragraphs = [
        Paragraph('Introduction', lorem_texts[0]),
        Paragraph('Experience', lorem_texts[1]),
        Paragraph('Skills', lorem_texts[2])
    ]
    return render_template('edit_base.html', variables_set=variables_set, paragraphs=paragraphs)


@app.route('/drag_test')
def drag_test():
    return render_template('drag_test.html')


if __name__ == '__main__':
    app.run(debug=True)
