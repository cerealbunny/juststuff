"""os.path.isdir() to determine if dir
    if so move to dir
    filecmp.cmp to compare two files
    easiest shit in my life to do, but the trick is making it faster"""

import filecmp
import os
import os.path
import re
def childfiles(dir):
    os.chdir(dir)
    lst = list(map(lambda x:os.path.abspath(x),os.listdir()))
    for file in lst:
        if os.path.isdir(file):
            for item in childfiles(file):
                lst.append(item)
    return lst

def findtwin(dir):
    ftype = input('Input filetype (.xxx format), or press ENTER if no specific filetype desired: ')
    exitype = not not re.match(r'(\w*\n$)',ftype)
    owd = os.getcwd()
    lst = childfiles(dir)
    os.chdir(owd); os.chdir(dir)
    for _ in range(len(lst)):
        x = lst.pop()
        #print(lst)
        if exitype:
            for item in lst:
                if filecmp.cmp(x,item) and x!=item and not (os.path.isdir(x) or os.path.isdir(item)):
                    print('----\n{}\nmatches\n{}\n----'.format(x, item))
        else:
            for item in lst:
                if re.match(r'(.*'+ftype+')',item):
                    if filecmp.cmp(x,item) and x!=item and not (os.path.isdir(x) or os.path.isdir(item)):
                        print('----\n{}\nmatches\n{}\n----'.format(x, item))

if __name__ == "__main__":
    os.chdir('/Users/michaeltang')
    findtwin(input('Input desired directory: '))
