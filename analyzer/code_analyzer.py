# write your code here

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
    if len(line.strip()) > 79:
        raise LineTooLongError(line_index)


def check_indentation(line, line_index):
    if line.startswith(' '):
        if (len(line) - len(line.lstrip())) % 4 != 0:
            raise IndentationMultipleError(line_index)


def check_semicolon(line, line_index):
    print(line.rstrip)
    if ';' in line.rstrip:
        raise SemicolonError(line_index)


def check_space(line, line_index):
    if '#' in line:
        new_line = line.split('#')
        if len(new_line[0]) - len(new_line[0].rstrip()) < 2:
            raise SpaceError(line_index)


def check_todo(line, line_index):
    if '#' in line:
        new_line = line.split('#')
        if 'todo' in new_line[1].lower():
            raise ToDoError(line_index)


def check_blank_line(line, line_index, *lines):
    too_much_blank_lines = True
    for line in lines:
        if line != '\n':
            too_much_blank_lines = False
            break
    if too_much_blank_lines and line != '\n':
        raise BlankLineError(line_index)


def analyze_file():
    with open(input(), 'r') as file:
        for num, line in enumerate(file, start=1):
            try:
                check_line_too_long(line, num)
                check_indentation(line, num)
                check_semicolon(line, num)
                check_space(line, num)
                check_todo(line, num)
            except Exception as e:
                print(e)


if __name__ == '__main__':
    analyze_file()
