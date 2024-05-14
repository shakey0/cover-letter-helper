def get_slug(name):
    slug = [char for char in name if char.isalnum()]
    return ''.join(slug).lower()


class Input:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.slug = get_slug(name)


class Variables:
    def __init__(self, name, code, values, selected):
        self.name = name
        self.code = code
        self.values = values
        self.selected = selected
        self.slug = get_slug(name)


class Paragraph:
    def __init__(self, name, text):
        self.name = name
        self.text = text
        self.slug = get_slug(name)
