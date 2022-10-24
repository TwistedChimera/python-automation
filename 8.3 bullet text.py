import pyperclip

text = pyperclip.paste()

splitText = text.split('\n')
for line in range(len(splitText)):
    splitText[line] = '* ' + splitText[line]
splitText = '\n'.join(splitText)

pyperclip.copy(splitText)
