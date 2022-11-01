import webbrowser, pyperclip, sys

address = ''

# supply address from arguments or clipboard
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/search/' + address)




