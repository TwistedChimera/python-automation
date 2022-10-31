# 1
spam = input('input a number: ')
assert int(spam) >= 10, 'spam less than 10'
print(spam)

# 2
eggs = input('input a word: ')
bacon = input('input another: ')
assert not(eggs.lower() == bacon.lower()), 'eggs cannot equal bacon ' + eggs + ' ' + bacon

assert False, 'this should never happen'
