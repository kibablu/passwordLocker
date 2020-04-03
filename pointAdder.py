#!/usr/bin/env python3 
# pointAdder.py - Adds Wikipedia bullet points to start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):  # loop through all indexes in the lines list
    lines[i] = '* ' + lines[i]  # add star to each string in lines list

text = '\n'.join(lines) # joins the lines into one single string value
pyperclip.copy(text)
# print(text)


'''
We split the text along its newlines to get a list in which each item is one line of the text. (line 9)
We store the list in lines and then loop through the items in lines. (line 9 and 10)
For each line, we add a star and a space to the start of the line. Now each string in lines begins with a star. (line 11)
'''

# worked - copy a list of items, run the program then paste it 
'''
* Lists of animals
* Lists of cultivar
* Lists of biologists by author abbreviation
* Lists of aquarium life
'''