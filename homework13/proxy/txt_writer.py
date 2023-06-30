from abstract_writer import Writer


class TxtWriter(Writer):
    def __init__(self, file_path):
        self.file_path = file_path

    def write_file(self, new_data):
        with open(self.file_path, 'w') as file:
            file.write(new_data)
