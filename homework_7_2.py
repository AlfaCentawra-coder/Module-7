from pprint import pprint
def custom_write(file_name, strings):
    string_position = {}
    with open(file_name, 'w') as file:
        for line_number, string in enumerate(strings, start=1):
            byte_position = file.tell()
            file.write(string + '\n')
            string_position[(line_number, byte_position)] = string

    return string_position



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)