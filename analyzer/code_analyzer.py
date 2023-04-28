
class LineTooLongError(Exception):
    def __init__(self, line_index):
        self.line_index = line_index

    def __str__(self):
        return f'Line {self.line_index}: S001 Too long'


class IndentationMultipleError(Exception):

    def __init__(self, line_index):
        self.line_index = line_index

    def __str__(self):
        return f'Line {self.line_index}: S002 Indentation is not a multiple of four'


class SemicolonError(Exception):

    def __init__(self, line_index):
        self.line_index = line_index

    def __str__(self):
        return f'Line {self.line_index}: S003 Unnecessary semicolon'


class SpaceError(Exception):

    def __init__(self, line_index):
        self.line_index = line_index

    def __str__(self):
        return f'Line {self.line_index}: S004 At least two spaces before an inline comment'


class ToDoError(Exception):

    def __init__(self, line_index):
        self.line_index = line_index

    def __str__(self):
        return f'Line {self.line_index}: S005 TODO found'


class BlankLineError(Exception):

    def __init__(self, line_index):
        self.line_index = line_index

    def __str__(self):
        return f'Line {self.line_index}: S006 More than two blank lines used before this line'


def check_line_too_long(line, line_index):
    try:
        if len(line.strip()) > 79:
            raise LineTooLongError(line_index)
    except LineTooLongError as e:
        print(e)


def check_indentation(line, line_index):
    try:
        if line.startswith(' '):
            if (len(line) - len(line.lstrip())) % 4 != 0:
                raise IndentationMultipleError(line_index)
    except IndentationMultipleError as e:
        print(e)


def check_semicolon(line, line_index):
    try:
        line_splitted = line.split('#')
        if line_splitted[0].strip().endswith(';'):
            raise SemicolonError(line_index)
    except SemicolonError as e:
        print(e)


def check_space(line, line_index):
    try:
        new_line = line.split('#')
        if '#' in line and new_line[0].strip() != '':
            if len(new_line[0]) - len(new_line[0].rstrip()) < 2:
                raise SpaceError(line_index)
    except SpaceError as e:
        print(e)


def check_todo(line, line_index):
    try:
        if '#' in line:
            new_line = line.split('#')
            if 'todo' in new_line[1].lower():
                raise ToDoError(line_index)
    except ToDoError as e:
        print(e)


def check_blank_line(actual_line, line_index, file_target):
    blank_line_counter = 0
    try:
        with open(file_target, 'r') as file:
            for num, line in enumerate(file, start=1):
                if line == actual_line and blank_line_counter > 2 and num == line_index:
                    raise BlankLineError(line_index)
                if line.strip() == '':
                    blank_line_counter += 1
                else:
                    blank_line_counter = 0
    except BlankLineError as e:
        print(e)


def analyze_file():
    file_target = input()
    with open(file_target, 'r') as file:
        for num, line in enumerate(file, start=1):
            check_line_too_long(line, num)
            check_indentation(line, num)
            check_semicolon(line, num)
            check_space(line, num)
            check_todo(line, num)
            check_blank_line(line, num, file_target)


if __name__ == '__main__':
    analyze_file()
