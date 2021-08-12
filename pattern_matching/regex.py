import re

"""
. matches any character except a new line
\d matches digit (0-9)
\D not a digit (0-9)
\w word character (a-z, A-Z, 0-9, _)
\w not a word character
\s Whitespace (space, tab, newline)
\S not Whitespace

\b word boundary
\B not a word boundary
^ Beginning of a string
$ End of a string

[] matches charactes in brackets
[^ ] matches charactes Not in brackets
"""

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + { } [ ] \ | ( )

google.com

321-555-4321
123.555.1234

Mr. Schafer
Mr Smith
Mrs. Robinson
Mr. T'''

sentence = 'Start a sentence and then bring it to an end'

# dot matches any character except new line
# escaping special characters add a backslash before the character
# searching for all the periods in the text to search
dot_pattern = re.compile(r'\.')
dot_matches = dot_pattern.finditer(text_to_search)

for dot in dot_matches:
    print(dot)

# searching for a url
url_pattern = re.compile(r'google\.com')

url_matches = url_pattern.finditer(text_to_search)

for url in url_matches:
    print(url)

# mathing a digit using \d
print(digit for digit in re.compile(r'\d').finditer(text_to_search))

