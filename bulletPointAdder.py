#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# Seperate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):   # Loops through all indexes in the "lines" list
    lines[i] = '* ' + lines[i]   # Adds star to each string in "lines" list
text = '\n'.join(lines)
pyperclip.copy(text)
