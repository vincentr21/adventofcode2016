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

line = input[1]

inner = re.findall(r'\[([a-z]+)\]', line)
# outer = re.findall(r'^([a-z]+)|([a-z]+)$|\]([a-z]+)\[', line)
outer = re.findall(r'(.*?)\[.*?\]', line)

print inner
print outer
# =============================================== part 2 ======================================================
