#! Python3

import os

spam = ['ppppp 6/12/2009 ppppp', 'ppppp 6/13/2009 ppppp', 'ppppp 3/13/2010 ppppp', 'ppppp 1/14/2011 ppppp', 'ppppp 5/22/2012 ppppp', 'ppppp 3/24/2013 ppppp', 'ppppp 7/30/2014 ppppp', 'ppppp 8/16/2015 ppppp', 'ppppp 9/12/2015 ppppp', 'ppppp 6/22/2016 ppppp', 'ppppp 9/4/2016 ppppp', 'ppppp 10/19/2016 ppppp', 'ppppp 12/30/2016 ppppp', 'ppppp 1/5/2017 ppppp', 'ppppp 6/18/2018 ppppp', 'ppppp 10/13/2018 ppppp', 'ppppp 2/3/2020 ppppp', 'ppppp 8/17/2020 ppppp', 'ppppp 12/13/2021 ppppp', 'ppppp 6/8/2022 ppppp']

os.chdir(r'''c:\\Users\\sulla\\Downloads\\Automate the Boring Stuff with Python Programming\\[TutsNode.com] - Automate the Boring Stuff with Python Programming\\11. Files''')
if not os.path.isdir('.\\generated'):
    os.mkdir(r'''.\\generated''')
for filename in spam:
    print(filename)
    fileObj = open('''.\\generated\\''' + 'ppppp 6/12/2009 ppppp', 'w')
