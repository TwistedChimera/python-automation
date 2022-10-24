import pyperclip, re, pprint
pdf = pyperclip.paste()
pdfStripped = re.sub(r'\n|\t', '', pdf)
pyperclip.copy(pdfStripped)

telRegex = re.compile(r'''
(?:                             # group 1
[+]?                            # outer + (optional)
[({\[]?                         # parenthesis characters: ({[ (optional)
[+]?                            # inner + (optional)
(?:                             # group 2
\d+                             # match one or more digits 
[-\/\.]?                        # dash characters: -/. (optional)
)+                              # group 2 end: match one or more digits and dash characters until space
[)}\]]?                         # parenthesis characters: )}] (optional)
[ ]*                            # space separated digits, zero or more
){8,}                           # group 1 end: filter out shorter matches (min: 8 max: inf)
\d                              # make sure it ends in a digit (8+1 = 9 units(**) minimum)

# ** - Raising and lowering that number will filter
#      the minumum and/or maximum length of the output
''', re.VERBOSE)

emailRegex = re.compile(r'''
# local@domain1.domain2.domain3 OR local@[ipv4] OR local@[ipv6] OR local@domain

(                                                   # Group 1

(?P<local>                                          # local
(?!.*\.\.+.*[@])                                    # no consecutive periods
(?!\..*[@])                                         # no starting period
(?!.*\.[@])                                         # no ending period
[!#$%&'*+\.\-\/=?^_`{|}~a-zA-Z0-9]{0,64}            # allowed characters and up to 64 characters
)                                                   # end local

[@]                                                 # @

# TODO: less naive ipv4 checks & implementation
(?P<ipv4>                                           # ipv4
\[                                                  # [
\d{3}\.\d{3}\.\d{3}\.\d{3}                          # no checks ipv4 syntax
\]                                                  # ]
)?                                                  # end ipv4 (optional)

# TODO: less naive ipv6 checks & implementaion
(?P<ipv6>                                           # ipv6
\[IPv6\:                                            # [IPv6:
(?:[0-9a-fA-F]{4}\:?){8}                            # no checks ipv6 syntax
\]                                                  # ]
)?                                                  # end ipv6 (optional)

(?P<single>                                         # single (single letter domain or subdomain)
(?=[a-zA-Z]\.)                                      # look ahead for 1 letter 1 period
[a-zA-Z]                                            # if found: match 1 letter
)?                                                  # end single (optional)

# TODO: proper length checks for domains
(?P<domain1>                                        # domain1 (subdomain OR domain)
(?![0-9]+\.)                                        # if domain isn't all numbers
(?![\-][a-zA-Z0-9\-]*\.)                            # AND if no starting dash
(?![a-zA-Z0-9\-]*[\-]\.)                            # AND no ending dash
[a-zA-Z0-9\-]+                                      # match up to before period
)?                                                  # end domain1 (optional)

\.?                                                 # first period (optional)

(?P<domain2>                                        # domain2 (domain OR top level domain)
(?![0-9]+\.)                                        # if domain isn't all numbers
(?![\-][a-zA-Z0-9\-]*\.)                            # AND if no starting dash
(?![a-zA-Z0-9\-]*[\-]\.)                            # AND no ending dash
[a-zA-Z0-9\-]+                                      # match up to before period
)?                                                  # end domain2 (optional)

\.?                                                 # second period (optional)

# TODO: proper top level domain checks
(?(domain2)                                         # if domain 2 is used
(?P<domain3>                                        # domain 3 (top level domain)
(?![0-9]+\.)                                        # if domain isn't all numbers
(?![\-][a-zA-Z0-9\-]*\.)                            # AND if no starting dash
(?![a-zA-Z0-9\-]*[\-]\.)                            # AND no ending dash
[a-zA-Z0-9\-]+                                      # match up to before period
)?                                                  # end domain3 (optional)
)                                                   # end domain2 check
)                                                   # end Group 1
''',re.VERBOSE)

telephones = re.findall(telRegex, pdfStripped)
emails = re.findall(emailRegex, pdf)

emails2 = []

# DEBUG: Uncomment to view output
#for i in range(len(telephones)):
#    print(telephones[i])
for i in range(len(emails)):
    emails2.append(emails[i][0])
    #print(emails[i][0])

toClipboard = '\n'.join(telephones) + '\n' + '\n'.join(emails2)
pyperclip.copy(toClipboard)

