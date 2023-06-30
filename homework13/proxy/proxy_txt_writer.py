from txt_reader import TxtReader
from txt_writer import TxtWriter


class TxtProxyReaderAndWriter:
    def __init__(self, file_path):
        self.__result = ''
        self.__is_actual = False
        self.__txt_reader = TxtReader(file_path)
        self.__txt_writer = TxtWriter(file_path)

    def read_file(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__txt_reader.read_file()
            self.__is_actual = True
            return self.__result

    def write_data(self, data):
        self.__txt_writer.write_file(data)
        self.__is_actual = False
        self.__result = ''

    def update_status(self):
        self.__is_actual = False


if __name__ == '__main__':
    proxy_writer_reader = TxtProxyReaderAndWriter('txt_data.txt')
    print(proxy_writer_reader.read_file())
    proxy_writer_reader.update_status()
    print(proxy_writer_reader.read_file())
    proxy_writer_reader.write_data('hey, how are you')
    print(proxy_writer_reader.read_file())
