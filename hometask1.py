# 1. You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
# For example, alison heck should be capitalized correctly as Alison Heck.
# Given a full name, your task is to capitalize the name appropriately.
# Input Format:A single line of input containing the full name, S.
# Constraints:* 0 < len(S) < 1000*
# The string consists of alphanumeric characters and spaces.
# Note: in a word only the first character is capitalized.
# Example 12abc when capitalized remains 12abc.
# Output Format:Print the capitalized string, S.

name = input("#1\nEnter fullname: ")
list1 = name.split(" ")
capitalizedName = ""
for el in list1:
    capitalizedName = capitalizedName + el.capitalize()+" "
print(capitalizedName)

# 2. Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

string = input("\n#2\nEnter string: ")
dic1 = {}
for let in string:
    dic1.update({let: str(string.count(let))})
print(sorted(dic1.items(), key=lambda item: item[1], reverse=True))

# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. 
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String
# [start: end: step]

string = input("\n#3\nEnter string: ")
if len(string)<2: str2=""
else: str2 = string[:2]+string[len(string)-2:]
print(str2)

# 4. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
list1 = ['abc', 'xyz', 'aba', '1221']
number = 0
for el in list1:
     if (len(el)>1) & (el[0] == el[len(el)-1]): number=number+1
print("\n#4\nList: ",list1,"\nnumber:",number)

# 5. You are given with 3 sets, find if third set is a subset of the first and the second sets
# Input: set([1,2]), set([2,3), set([2])
# Expected result: True
# Input: set([1,2]), set([3,4), set([5])
# Expected result: False

set1 = set([1,2])
set2 = set([2,3])
set3 = set([2])
print("\n#5\nSets",set1,set2,set3,"\nthird set is a subset of the first and the second sets\n",set3.issubset(set1)&set3.issubset(set2))

set1 = set([1,2])
set2 = set([3,4])
set3 = set([5])
print("\nSets",set1,set2,set3,"\nthird set is a subset of the first and the second sets\n",set3.issubset(set1)&set3.issubset(set2))

# 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

n = int(input("\n#6\nEnter size of the dictionary: "))
print({(a+1): (a+1) ** 2 for a in range(n)})

# 7. Write a Python script to merge two Python dictionaries

dic1 = {1: "a", 2: "b"}
dic2 = {2: "a", 3: "c"}
dic3 = dic1.copy()
dic3.update(dic2)
print("\n#7\ndictionary 1: ", dic1, "\ndictionary 2: ", dic2, "\nmerge of two dictionaries", dic3)

# 8. Write a Python program to find the highest 3 values in a dictionary
# import random
# import operator
# d = {a: random.randint(0,100) for a in range(7)}
# print(d)
# list1 = []
# for i in range(3):
#     maximumValue = max(d.items(), key=operator.itemgetter(1))
#     del d[maximumValue[0]]
#     list1.append(maximumValue[1])
# print(list1)

import random
d = {a: random.randint(0, 100) for a in range(7)}
print("\n#8\ndictionary: ", d)
list1 = list({k: v for k, v in sorted(d.items(), key=lambda item: item[1])}.values())
print("highest 3 values in a dictionary: ", list1[len(list1)-3:])

# 9. Write a Python program to remove duplicates from a list.

list1 = [2, 3, 2, 5, 7, 8, 5]
print("\n#9\ninput list", list1, "\nsorted list", set(list1))

# 10. Write a Python program to get the difference between the two lists
list1 = [el for el in range(4)]
list2 = [el for el in range(2, 6)]
print("\n#10\nInput lists", list1, list2)
print("difference between the two lists", set(list1).symmetric_difference(set(list2)))