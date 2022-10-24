import pyperclip, re, pprint
pdf = pyperclip.paste()
pdfStripped = re.sub(r'\n|\t', '', pdf)
pyperclip.copy(pdfStripped)

telRegex = re.compile(r'(?:[({\[]?[+]{0,1}(?:\d+[-\/]?)+[)}\]]?[ ]?){8,}\d')
emailRegex = re.compile(r'''
((?P<local>(?!.*\.\.+.*[@])(?!\..*[@])(?!.*\.[@])[!#$%&'*+\.\-\/=?^_`{|}~a-zA-Z0-9]{0,64})[@](?P<ipv4>\[\d{3}\.\d{3}\.\d{3}\.\d{3}\])?(?P<ipv6>\[IPv6\:(?:[0-9a-fA-F]{4}\:?){8}\])?(?P<single>(?=[a-zA-Z]\.)[a-zA-Z])?(?P<domain1>(?![0-9]+\.)(?![\-][a-zA-Z0-9\-]*\.)(?![a-zA-Z0-9\-]*[\-]\.)[a-zA-Z0-9\-]+)?\.?(?P<domain2>(?![0-9]+\.)(?![\-][a-zA-Z0-9\-]*\.)(?![a-zA-Z0-9\-]*[\-]\.)[a-zA-Z0-9\-]+)?\.?(?(domain2)(?P<domain3>(?![0-9]+\.)(?![\-][a-zA-Z0-9\-]*\.)(?![a-zA-Z0-9\-]*[\-]\.)[a-zA-Z0-9\-]+)?))''',re.VERBOSE)

telephones = re.findall(telRegex, pdfStripped)
emails = re.findall(emailRegex, pdf)

for i in range(len(telephones)):
    print(telephones[i])
for i in range(len(emails)):
    print(emails[i][0])

