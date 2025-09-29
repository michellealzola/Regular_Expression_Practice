"""
A named capture group is a part of a regular expression that both matches some text
and stores what it matched under a name (a label). In Python regex, you write it like:

=================
(?P<name>pattern)
=================

Purpose:
Capture the part of the string that matches the pattern and give that capture a name (name), not just a number.

Why use it?

Easier to read than numeric groups (group(1), group(2), …).

Lets you access matches by name: m.group("name").

Useful when you have many groups and want clarity.
"""

import re

rex = re.compile(r"(?P<first_name>\w+) (?P<last_name>\w+)")
m = rex.search("Michelle Alzola")
print(m.group("first_name"))
print(m.group("last_name"))
print(m.group(1))
print(m.group(2))
print(m.groupdict())

rex2 = re.compile(r"(?P<var>[A-Za-z_]\w*)\s*=\s*(?P<value>\d+)")
m2 = rex2.search("sum = 10")
print(m2.group("var"))
print(m2.group("value"))
print(m2.groupdict())

#Backreference the same text
rex3 = re.compile(r"(?P<word>\w+)\s+(?P=word)")
print(bool(rex3.search("hello hello")))
print(bool(rex3.search("hello world")))

# Use names in substitution
new = re.sub(r"(?P<first>\w+) (?P<last>\w+)", r"\g<last>, \g<first>", "Michelle Alzola")
print(new)


# \g<...> is how you refer to a captured group inside the replacement string of re.sub.

# \g<name> → the text matched by the named group (?P<name>...)
#
# \g<number> → the text matched by the numbered group (...)

# numbered groups --> inside ()
print(re.sub(r"(\w+)\s+(\w+)", r"\2, \1", "Ada Lovelace"))
print(re.sub(r"(\w+)\s+(\w+)", r"\g<2>, \g<1>", "Ada Lovelace"))

# named groups --> inside <>
print(re.sub(r"(?P<f>\w+)\s+(?P<l>\w+)", r"\g<l>, \g<f>", "Alan Turing"))

# whole match (group 0)
print(re.sub(r"\d+", r"[\g<0>]", "ID 1234"))