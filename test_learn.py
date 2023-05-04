#\\\\\\\\while////////
# i = 1
# while i >= 0:
#     print(i)
#     i = i + 1
#     if i == 10001:
#         break
#---------------------------------------------
#\\\\\\\for//////
# friends = ["joe", "jack", "marpel"]
# count = 0
# for thisone in friends:
#     print ("hello", thisone)
#     count = count + 1
# print ("I said", count, "hello's")
#---------------------------------------------
#\\\\\string/////
# len('string')

# i = '100101010100100110011001010111001'
# g = '100101010100100110011001010111001'
# d = '100101010100100110011001010111001'
# for b in range(0, len(i)):
#     print (i[b], g[b], d[b])
#))))))example((((((((
# for letter in 'my,string':
#     print(letter)
# string = "hello is a exampel number two"

# for harf in string:
#     print(harf)

# count = 0
# for letter in string:
#     if letter == 'l':
#         count = count + 1
# print(count)

# q = 'hello baby you is very kind'
# print(q[11:])

#))))))example2((((((
# "pourya".upper()
# dir('hello  baby')
# 'hello baby you is very kind'.count("a")
# s = 'hell0'
# s.find('l')
# s.find('l', 2)
# print('     t67567ghgjgjfhjghj    yrtyt ryrt      '.strip())
# print('hello'.startswith('h'))
# name = 'baby'
# print('hello %s howareyou?' % name)
#-------------------------------------------------
#\\\\\\list's///////
# l = [4, 6, 0, -9, 3.7, 'test,code']
# print(l[0])
# l2 = [l, 5, [1, 2]]
# for i in range(0, len(l2)):
#     print(l2[i])
# l[0] = 9
# for i in range(0, len(l)):
#     print(i, l[i])
# for item in l:
#     print(item)

# l1 = [3, 4, 9, 0]
# l2 = ['toy', 'programmer', 'developer']
# print(l1 + l2)
# print(l1.append('new'))
# print(l1.extend([5, 6, 7]))
# print(l1.sort())
# print(l1.pop())
# print(l1.remove(4))
# print(l1)
# s = 'hello baby you is very cute'
# print(s.split())
# list_of_words = s.split()
# print('_'.join(list_of_words))
#----------------------------------------
#\\\\\\dictionary//////
# a = dict()
# p2e = dict()
# p2e['yek'] = 'one'
# p2e['du'] = 'two'
# p2e['seea'] = 'tree'
# print(p2e, a)


# string = 'hello baby you is very kind'
# counter = dict()
# for letter in string:
#     if letter in counter:
#         counter[letter] += 1
#     else:
#         counter[letter] = 1

# for this_one in list(counter.keys()):
#     print('%s appeared %s times' % (this_one, counter[this_one]))
    

# string = 'hello baby you is very kind'
# counter = dict()
# for letter in string:
#     counter[letter] = counter.get(letter, 0) + 1

# for this_one in list(counter.keys()):
#     print('%s appeared %s times' % (this_one, counter[this_one]))
#--------------------------------------------------------
#\\\\\\Tuples//////
# a = (1, 2, 3)
# a[0] = 5
# (4,)
# type((4,))
# t = (0, 1, 2, 3, 4, 'hello baby you is very kind')
# t[1:4]
# a = (1, 2)
# x, y = a
# email = 'pourya.meamarian@gmail.com'
# email.split('@')
# name, domain = email.split('@')
# vazn = {'aylar': 50, 'rori': 74,'koli': 46, 'javad': 87,}
# list(vazn.items())
# for name, vazn in list(vazn.items()):
#     print ('vazn %s taghriban hast %s' % (name, vazn))
#-------------------------------------------------------
#\\\\\\\librarys///////
# import datetime
# datetime.date.today()
#------------------------------------------------------
#\\\\\\\ files ////////
# f = open("C:/Users/pourya.meamarian/Desktop/test_text.txt")
# f.read()
# f.close()
#------\
# for line in f:
    # print (line)
#------/
#\\\\\\\files_CSV//////
# import csv
# from statistics import mean
# with open('/C:/Users/pourya.meamarian/Desktop/project/py/files.csv') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         name = row[0]
#         these_grades = list()
#         for grade in row[1:]:
#             these_grades.append(int(grade))
# print ("avernge of %10s is %5.2f" % (name, mean(these_grades)))