# write your code here

class LineTooLongError(Exception):
    def __init__(self, line_index):
        self.line_index = line_index

    def __str__(self):
        return f'Line {self.line_index}: S001 Too long'


def analyze_file():
    with open(input(), 'r') as file:
        for num, line in enumerate(file, start=1):
            try:
                if len(line.strip()) > 79:
                    raise LineTooLongError(num)
            except LineTooLongError as e:
                print(e)


if __name__ == '__main__':
    analyze_file()