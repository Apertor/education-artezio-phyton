# 1. You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
# For example, alison heck should be capitalized correctly as Alison Heck.
# Given a full name, your task is to capitalize the name appropriately.
# Input Format:A single line of input containing the full name, S.
# Constraints:* 0 < len(S) < 1000*
# The string consists of alphanumeric characters and spaces.
# Note: in a word only the first character is capitalized.
# Example 12abc when capitalized remains 12abc.
# Output Format:Print the capitalized string, S.

#name = input("Enter fullname: ")

# 2. Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

# string = input("Enter string: ")
# for leteral in string:
#     print("'"+leteral+"': "+str(string.count(leteral)))


# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. 
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String

# [start: end: step]

string = input("Enter string: ")
if len(string)<2: str2=""
else: str2 = string[:2]+string[len(string)-2:]
print(str2)