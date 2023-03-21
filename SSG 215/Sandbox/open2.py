fname = input('Enter file name: ')
try :
    fhand = open(fname)
except :
    print(f'File cannot be opened: {fname}')
    quit()

count = 0
for line in fhand :
    if line.startswith('Import'):
        count = count + 1
print(f'There were {count} import lines in {fhand}')