class FromDataAdapter:
    def __init__(self, file_path):
        self.__file_path = file_path

    def convert_from_txt_to_html(self):
        with open(self.__file_path, 'r') as file:
            lines = file.readlines()
        headers = lines[0].replace('\n', '').split(',')

        data = [item.replace('\n', '').split(',') for item in lines[1:]]
        result = []
        for user_data in data:
            html_output = ""
            for header, value in zip(headers, user_data):
                html_output += f"<{header}>{value}</{header}>\n"
            result.append(html_output)
        return result


if __name__ == '__main__':
    html = FromDataAdapter('users.txt').convert_from_txt_to_html()
    print(html)
