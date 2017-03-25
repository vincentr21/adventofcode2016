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


count = 0
def getABAList(outerList):
    ABAList = set()
    for token in outerList:
        N = len(token)
        for i in range(0, N - 2):
            a0 = token[i]
            b = token[i + 1]
            a1 = token[i + 2]
            if a0 != b and a0 == a1:
                ABAList.add(a0+b+a1)
    return ABAList

def BABIsInABAList(ABAList, innerList):
    for token in innerList:
        N = len(token)
        for i in range(0, N - 2):
            a0 = token[i]
            b = token[i + 1]
            a1 = token[i + 2]
            if a0 != b and a0 == a1:
                ABA = b+a0+b

                if ABA in ABAList:
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


    ABAList = getABAList(outer)

    if BABIsInABAList(ABAList, inner):
        count += 1

print count

