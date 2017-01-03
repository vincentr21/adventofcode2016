# Advent of Code 2016 - Day 6
# Vincent Ren
# 12/30/2016

import operator  # for sorting a dict by value
# =============================================== part 1 ======================================================
f = open('in6.txt', 'r')

input = f.read()
input = input.strip()  # removes end of file \n character
input = input.split('\n')
print input
# print len(input)

cols = len(input[0])

# initialize a map with a-z keys for each column
charCount = []
for col in range(0, cols):
    charCount.append({})
    for i in range(97, 123):
        charCount[col][chr(i)] = 0

# print charCount

for line in input:

    for i in range(cols):
        charCount[i][line[i]] += 1

# print charCount

output = ''
for i in range(cols):
    sortedCharCount = sorted(charCount[i].items(), key=operator.itemgetter(0))
    sortedCharCount = sorted(sortedCharCount, key=operator.itemgetter(1), reverse=True)

    print sortedCharCount

    output += sortedCharCount[0][0]

print output


# =============================================== part 2 ======================================================
# this only works for this specific output, where there are no letters with 0 occurrences, would not work in the general case
# I don't care cause I'm greedy atm
output = ''
for i in range(cols):
    sortedCharCount = sorted(charCount[i].items(), key=operator.itemgetter(0))
    sortedCharCount = sorted(sortedCharCount, key=operator.itemgetter(1))

    print sortedCharCount

    output += sortedCharCount[0][0]

print output

