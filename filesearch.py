"""probably create additional helpers, this is no longer findtwin but find*twins
    dictionary to store files now by filetype
    then, depending on the filetype chosen, hash the entire list stored in dict entry by their file size. find the match."""

import filecmp
import os
import os.path
import re
def gendict(dir): #generates dictionary of all files in dir and under, key=filetype & value=list of all files of type
    os.chdir('/')
    wlst = os.walk(dir)
    d = {'NoType':[]}
    for tup in wlst:
        os.chdir(tup[0])
        for i in tup[2]:
            ftype = re.search(r'\.[^\.]+$',i).group(0) if re.search(r'\.[^\.]+$',i) else None
            if not ftype:
                d['NoType'].append(os.path.abspath(i))
            elif ftype not in d:
                d[ftype] = [os.path.abspath(i)]
            else:
                d[ftype].append(os.path.abspath(i))
    return d

def findtwins():
    exitype = not not re.match(r'(\w*\n$)',ftype)
    lst = gendict('/Users/michaeltang')
    os.chdir('/')
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
    findtwins()

