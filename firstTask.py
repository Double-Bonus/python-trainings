import numpy as np

def is_adjacent_symbol(x, y):
    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # UP left,   UP,          UP Right
        (0, -1),         (0, 1),     # Left,                   Right
        (1, -1), (1, 0), (1, 1)      # DOWN Left, DOWN Bottom, DOWN Right
    ]
    
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        # Check if the new position is within bounds
        if ((0 <= nx < max_X) and (0 <= ny < max_Y)): # bondaries check
            if lines[ny][nx] == '*' or lines[ny][nx] == '#' or lines[ny][nx] == '$' or lines[ny][nx] == '+' or lines[ny][nx] == '=' or lines[ny][nx] == '%' or lines[ny][nx] == '&' or lines[ny][nx] == '/' or lines[ny][nx] == '$' or lines[ny][nx] == '-' or lines[ny][nx] == '@':
                return True
    
    return False



def is_part_number(lines, column, row, length):
    # for i in range(column, column + length):
    for i in range(column-length, column):
        if is_adjacent_symbol(i, row):
            return True
    return False

def calculate_sum(line, column, length):
    return int(line[(column-length+1):column+1])


# returns first found int and it length: 0 if not found
def find_int(line, lines, row):
    length = 0
    sum = 0

# one more for loop for lines and count row nr
    for column, char in enumerate(line):
        # print(column)
        if char.isdigit():
            length = length + 1
        elif length != 0:
            if is_part_number(lines, column, row, length):
                sum = sum + calculate_sum(line, column-1, length)
                print(calculate_sum(line, column-1, length))
            length = 0

    return sum


# read the lines from the file
# with open('test_in.txt') as f:
with open('input.txt') as f:
# with open('input.txt') as f:
    lines = f.readlines()

max_X = len(lines[0]) - 1 # TODO: also calculates '\n'???
max_Y = len(lines)


print("max_X: %2d"  % max_X)
print("max_Y: %2d"  % max_Y)
# print(lines[0])
# print(lines[0][0])
# print(lines[1][0])

# print(find_int(lines[9], lines, 8))
sum = 0
row = 0
for line in lines:
    temp_int = find_int(line, lines, row)
    sum = sum + temp_int
    row = row + 1
print(sum)




# Start from begining of the row (first row)
    # find int in row (index and lenth)
        #  check if it should be valid 
# print output