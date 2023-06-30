from abstract_reader import Reader


class TxtReader(Reader):

    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, 'r') as file:
            text = file.read()
        return text
