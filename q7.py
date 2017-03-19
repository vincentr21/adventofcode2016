# Advent of Code 2016 - Day 7
# Vincent Ren
# 12/30/2016

import re
import operator  # for sorting a dict by value
# =============================================== part 1 ======================================================
f = open('in7.txt', 'r')

input = f.read()
input = input.strip()  # removes end of file \n character
input = input.split('\n')
print input
# print len(input)

# line = input[0]
#
# inner = re.findall(r'\[([a-z]+)\]', line)
# # outer = re.findall(r'^([a-z]+)|([a-z]+)$|\]([a-z]+)\[', line)
# # couldn't put these two regexes into one...
# outer = re.findall(r'(.*?)\[.*?\]', line)
# last_outer = re.findall(r'\[[a-z]*?\]([a-z]*?)$', line)

# appends the last found token by regex into the outer list
# outer.append(last_outer[0])

count = 0

def isABBA(str):
    N = len(str)
    # print N
    # print str
    for i in range(1, N-2):
        a0 = str[i-1]
        b0 = str[i]
        b1 = str[i+1]
        a1 = str[i+2]
        # print str[i-1], str[i], str[i+1], str[i+2]
        if a0 != b0 and a0 == a1 and b0 == b1:
            return True
    return False

for line in input:
    isInvalid = False

    inner = re.findall(r'\[([a-z]+)\]', line)
    # outer = re.findall(r'^([a-z]+)|([a-z]+)$|\]([a-z]+)\[', line)
    # couldn't put these two regexes into one...
    outer = re.findall(r'(.*?)\[.*?\]', line)
    last_outer = re.findall(r'\[[a-z]*?\]([a-z]*?)$', line)
    # appends the last found token by regex into the outer list
    outer.append(last_outer[0])

    for token in inner:
        if isABBA(token):
            isInvalid = True
            break

    if isInvalid:
        continue

    for token in outer:
        if isABBA(token):
            # print "FOuND!"
            count += 1
            break

# print inner
# print outer
# print last_outer

print count

# =============================================== part 2 ======================================================
