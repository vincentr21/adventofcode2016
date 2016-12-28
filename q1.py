# Advent of Code 2016 - Day 1
# Vincent Ren
# 12/26/2016

# =============================================== part 1 ======================================================
f = open('in1.txt', 'r')

input = f.read()
input = input.strip()  # removes \n character
input = input.split(', ')
print input

# n, e, s, w
direction = 'n'

count = {
    'n' : 0,
    'e' : 0,
    's' : 0,
    'w' : 0,
}

for move in input:
    rotation = move[:1]
    distance = int(move[1:])

    if rotation == 'R':
        if direction == 'n':
            direction = 'e'
        elif direction == 'e':
            direction = 's'
        elif direction == 's':
            direction = 'w'
        elif direction == 'w':
            direction = 'n'

    elif rotation == 'L':
        if direction == 'n':
            direction = 'w'
        elif direction == 'e':
            direction = 'n'
        elif direction == 's':
            direction = 'e'
        elif direction == 'w':
            direction = 's'

    count[direction] += distance

# print count

output = abs(count['n']-count['s']) + abs(count['e']-count['w'])
print output

# =============================================== part 2 ======================================================

visited = []
direction = 'n'
location = [0 ,0]

for move in input:
    rotation = move[:1]
    distance = int(move[1:])
    
    if rotation == 'R':
        if direction == 'n':
            direction = 'e'
        elif direction == 'e':
            direction = 's'
        elif direction == 's':
            direction = 'w'
        elif direction == 'w':
            direction = 'n'

    elif rotation == 'L':
        if direction == 'n':
            direction = 'w'
        elif direction == 'e':
            direction = 'n'
        elif direction == 's':
            direction = 'e'
        elif direction == 'w':
            direction = 's'

    for i in range(distance):
        if direction == 'n':
            location[1] += 1
        elif direction == 'e':
            location[0] += 1
        elif direction == 's':
            location[1] -= 1
        elif direction == 'w':
            location[0] -= 1

        if (location[0], location[1]) in visited:
            print 'found: ', (location[0], location[1])
            output = abs(location[0]) + abs(location[1])
            print output
            break

        visited.append((location[0], location[1]))

print visited

