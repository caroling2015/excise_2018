# -*- encoding: utf-8 -*-
# 正则表达式 regular expression
import re

# Match literal string value literal
n = re.match('foo','foo')
if n is not None:
    print n.group()

# Match regular expressions re1 or re2
bt = 'bat|bet|bit'
m = re.match(bt,'bat')
if m is not None:
    print m.group()

l = re.match(bt,'he bit me')
if l is not None:
    print l.group()
    print '===='
# search() looks for the first occurrence of the pattern within the string, it evaluates a string strictly from left to right
z = re.search(bt,'he bit me')
print z.group()