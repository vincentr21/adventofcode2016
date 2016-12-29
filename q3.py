# Advent of Code 2016 - Day 3
# Vincent Ren
# 12/28/2016

# =============================================== part 1 ======================================================
f = open('in3.txt', 'r')

input = f.read()
input = input.strip()  # removes end of file \n character
input = input.split('\n')
# print input
# print len(input)

count = 0

def isTriangle(a,b,c):
    tri_max = max(a,b,c)
    # tri_mid = min(max(a,b),c)  # this was wrong xD
    tri_mid = max(min(a,b), min(max(a,b),c));
    tri_min = min(a,b,c)

    # print tri_min, tri_mid, tri_max

    if tri_min + tri_mid > tri_max:
        return True
    return False

for line in input:
    line = line.strip()
    # print line.split()
    a, b, c = line.split()
    a, b, c, = int(a), int(b), int(c)
    # print a, b, c
    if isTriangle(a,b,c):
        count += 1



print count
# =============================================== part 2 ======================================================

col = [[],[],[]]


# number of input lines, 1 triangle per line
# N = len(input)
count = 0

for line in input:
    line = line.strip()
    a, b, c = line.split()
    a, b, c, = int(a), int(b), int(c)

    col[0].append(a)
    col[1].append(b)
    col[2].append(c)

    for i in range(0,3):
        if len(col[i]) == 3:
            if isTriangle(col[i][0], col[i][1], col[i][2]):
                count += 1
            col[i] = []

print count


