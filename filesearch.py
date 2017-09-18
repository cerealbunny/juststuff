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
        for i in tup[2]: #insert file abspaths into entries by filetype; create new filetype key if doesn't already exist
            ftype = re.search(r'\.[^\.]+$',i).group(0) if re.search(r'\.[^\.]+$',i) else None
            if not ftype:
                d['NoType'].append(os.path.abspath(i))
            elif ftype not in d:
                d[ftype] = [os.path.abspath(i)]
            else:
                d[ftype].append(os.path.abspath(i))
    return d

def hashdict(d): #delete one-value type entries and turn the other entries in to hash tables by filesize, created by mod 100 (simple)
    for key in d.keys():
        if len(d[key]) == 1:
            d[key] = {0:[]}
        else:
            htb = {x:[] for x in range(100)}
            for val in d[key]:
                try:
                    htb[os.stat(val).st_size%100].append(val)
                except FileNotFoundError:
                    pass
            d[key] = htb
    return d

def findtwins(tspec):
    d = hashdict(gendict('/Users/michaeltang'))
    if tspec in d.keys():
        for lst in d[tspec].values():
            if len(lst) > 1:
                for _ in range(len(lst)):
                    x = lst.pop()
                    for item in lst:
                        if filecmp.cmp(x,item):
                            print('----\n{}\nmatches\n{}\n----'.format(x, item))
    else:
        for val in d.values(): #accessing hashtables
            for lst in val.values():
                if len(lst) > 1:
                    for _ in range(len(lst)):
                        x = lst.pop()
                        for item in lst:
                            if filecmp.cmp(x,item):
                                print('----\n{}\nmatches\n{}\n----'.format(x, item))

if __name__ == "__main__":
    findtwins(input('Enter specific type (.format) if needed or just press ENTER to scan all:').strip())

