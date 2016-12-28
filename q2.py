# Advent of Code 2016 - Day 2
# Vincent Ren
# 12/27/2016

# =============================================== part 1 ======================================================
f = open('in2.txt', 'r')

input = f.read()
input = input.strip()  # removes \n character
input = input.split('\n')
# print input
# print size(input)
# inputLines = len(input)


keypad = ((1, 4, 7),
          (2, 5, 8),
          (3, 6, 9))

# print keypad[0]
# print keypad[0][1]

x = 1
y = 1

output = ''

for line in input:
    # print line
    for c in line:
        if c == 'U':
            y = max(0, y - 1)
        elif c == "D":
            y = min(2, y + 1)
        elif c == "L":
            x = max(0, x - 1)
        elif c == "R":
            x = min(2, x + 1)

    output += str(keypad[x][y])
print output

# =============================================== part 2 ======================================================

keypad = (('', '', '5', '', ''),
          ('', '2', '6', 'A', ''),
          ('1', '3', '7', 'B', 'D'),
          ('', '4', '8', 'C', ''),
          ('', '', '9', '', ''),)

x = 0
y = 2

output = ''

for line in input:
    for c in line:
        if c == 'U':
            if keypad[x][max(0, y - 1)] != '':
                y = max(0, y - 1)
        elif c == "D":
            if keypad[x][min(4, y + 1)] != '':
                y = min(4, y + 1)
        elif c == "L":
            if keypad[max(0, x - 1)][y] != '':
                x = max(0, x - 1)
        elif c == "R":
            if keypad[min(4, x + 1)][y] != '':
                x = min(4, x + 1)

    output += keypad[x][y]
print output
