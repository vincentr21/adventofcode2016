# Advent of Code 2016 - Day 5
# Vincent Ren
# 12/30/2016

import hashlib
# =============================================== part 1 ======================================================
f = open('in5.txt', 'r')

input = f.read()
input = input.strip()  # removes end of file \n character
# input = input.split('\n')
print input

index = 0

password = ''

# input = 'abc'
# key = 'abc3231929'
# m.update(key)
# md5hash = m.hexdigest()
# print md5hash, type(md5hash), key, index

# while len(password) < 8:
#     m = hashlib.md5()
#     key = input + str(index)
#     m.update(key)
#     md5hash = m.hexdigest()
#
#     if md5hash[0:5] == '00000':
#         print md5hash, type(md5hash), key, index
#         password += md5hash[5]
#     index += 1
#
# print password

# =============================================== part 2 ======================================================

password = list('xxxxxxxx')
index = 0

while 'x' in password:
    m = hashlib.md5()
    key = input + str(index)
    m.update(key)
    md5hash = m.hexdigest()


    if md5hash[0:5] == '00000':
        pos = int(md5hash[5], 16)
        if pos < 8 and password[pos] == 'x':
            print md5hash, type(md5hash), key, index
            password[pos] = md5hash[6]
    index += 1

password = ''.join(password)

print password