import re

regex ='(\w(\w)\w)-(\d\d\d)'
m = re.match(regex,'abc-123')
if m is not None:
    print m.group()
    print m.group(1)
    print m.group(2)
    print m.groups()
else:
    print "hello"


m = re.search('^The','end. The')
if m is not None:
    print m.group()