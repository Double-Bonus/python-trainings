def is_adjacent_symbol(x, y):
    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # UP left,   UP,   UP Right
        (0, -1),           (0, 1),   # Left,            Right
        (1, -1),  (1, 0),  (1, 1)    # DOWN Left, DOWN, DOWN Right
    ]
    special_chars = {'*', '#', '$', '+', '=', '%', '&', '/', '-', '@'}
    
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if ((0 <= nx < max_X) and (0 <= ny < max_Y)): # bondaries check
            if lines[ny][nx] in special_chars:
                return True
    return False

def is_part_number(column, row, length):
    for i in range(column-length, column):
        if is_adjacent_symbol(i, row):
            return True
    return False

def calculate_sum(line, column, length):
    return int(line[(column-length):column])

def find_int(line, row):
    length = 0
    sum = 0

    for column, char in enumerate(line):
        if char.isdigit():
            length = length + 1
        elif length != 0:
            if is_part_number(column, row, length):
                sum = sum + calculate_sum(line, column, length)
                if DEBUG:
                    print(calculate_sum(line, column, length))
            length = 0

    return sum

DEBUG = False

# read the lines from the file
with open('input.txt') as f:
    lines = f.readlines()

max_X = len(lines[0]) - 1 # TODO: also calculates '\n'???
max_Y = len(lines)

if DEBUG:
    print("max_X: %2d"  % max_X)
    print("max_Y: %2d"  % max_Y)

total_sum = 0
row = 0
for line in lines:
    temp_int = find_int(line, row)
    total_sum = total_sum + temp_int
    row = row + 1
print(total_sum)

# Start from begining of the row (first row)
    # find int in row (index and length)
        # check if it should be valid (adjacent symbols)
            # if yes, add to sum
    # add sum to total sum
# move to next row 