class MakeParagraph():
    def __init__(self, txt):
        self.txt = txt

    def __enter__(self):
        return '<p>' + self.txt + '</p>'

    def __exit__(self, type, value, traceback):
        print('exit')


with MakeParagraph('new text') as paragraph:
    print(paragraph)
