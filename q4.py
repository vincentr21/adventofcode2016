# Advent of Code 2016 - Day 4
# Vincent Ren
# 12/28/2016

import re
import operator  # for sorting a dict by value
# =============================================== part 1 ======================================================
f = open('in4.txt', 'r')

input = f.read()
input = input.strip()  # removes end of file \n character
input = input.split('\n')
# print input
# print len(input)

# line = input[0]

mySum = 0

# testing:
# input =['a-b-c-d-e-f-g-h-987[abcde]']

for line in input:
    # print line
    # parsing and cleaning string inputs
    chars = re.match(r'[a-z-]+', line).group()
    num = re.search(r'[0-9]+', line).group()
    checksum = re.search(r'\[[a-z]+\]', line).group()

    chars = re.sub(r'-', '', chars)
    num = int(num)
    checksum = re.sub(r'\[|\]', '', checksum)


    # print type(chars), chars
    # print type(num), num
    # print type(checksum), checksum


    # initialize a map with a-z keys
    charCount = {}
    for i in range(97, 123):
        charCount[chr(i)] = 0
        # print charCount

    # print charCount

    for c in chars:
        charCount[c] += 1

    # print charCount

    # print charCount.items()

    sortedCharCount = sorted(charCount.items(), key=operator.itemgetter(0))

    # print sortedCharCount

    sortedCharCount = sorted(sortedCharCount, key=operator.itemgetter(1), reverse=True)


    # print sortedCharCount

    realChecksum = ''
    for c in range(0,5):
        realChecksum += sortedCharCount[c][0]

    if checksum == realChecksum:
        mySum += num

    # print realChecksum

print mySum


# =============================================== part 2 ======================================================

def rotateChar(char, rotateNum):
    asciiChar = ord(char)
    asciiChar += rotateNum % 26
    if asciiChar > ord('z'):
        asciiChar -= 26
    return chr(asciiChar)

print rotateChar('a',27)

for line in input:
    # print line
    # parsing and cleaning string inputs
    chars = re.match(r'[a-z-]+', line).group()
    num = re.search(r'[0-9]+', line).group()
    checksum = re.search(r'\[[a-z]+\]', line).group()

    chars = re.sub(r'-', ' ', chars)
    chars = chars.strip()
    num = int(num)
    # checksum = re.sub(r'\[|\]', '', checksum)


    # print type(chars), chars
    # print type(num), num
    # print type(checksum), checksum


    decyphered = ''

    for c in chars:
        if c == ' ':
            decyphered += ' '
        else:
            decyphered += rotateChar(c, num)

    print decyphered, num


