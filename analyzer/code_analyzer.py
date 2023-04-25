# write your code here
file_path = input()

with open (file_path, 'r') as file:
    line_counter = 0
    for line in file:
        if len(line.strip()) > 79:
            print(f'Line {line_counter + 1}: S001 Too long')
        line_counter += 1

