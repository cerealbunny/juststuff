class alphatree:
    def __init__(self, val):
        self.data = val
        self.pwsize = 0
        self.kids = []
    def add(self, val):
        #print([kid.data for kid in at.kids], end=' ')
        #print(val, end= ' ')
        #print('i')
        for letter in val:
            if not self.kids:
                self.kids = [alphatree(letter)]
        #print([kid.data for kid in at.kids], end=' ')
        #print('i')
            elif letter not in [kid.data for kid in self.kids]:
                self.kids.append(alphatree(letter))
        #print([kid.data for kid in at.kids], end=' ')
        #print('i')
            self = self.kids[[kid.data for kid in self.kids].index(letter)]
            self.pwsize += 1
        if not self.kids:
            self.kids = [alphatree('*')]
        else:
            self.kids.append(alphatree('*'))
        return
    #add(at.kids[[kid.data for kid in at.kids].index(val[0])],val[1:])
    def find(self, val):
    #print([kid.data for kid in at.kids])
        for letter in val:
            if not self.kids or letter not in [kid.data for kid in self.kids]:
                print(0,file=f2)
                return
            self = self.kids[[kid.data for kid in self.kids].index(letter)]
            val = val[1:]
        print(self.pwsize,file=f2)
        return
def atprn(at):
    for kid in at.kids:
        print(kid.data)
        atprn(kid)
def matchtxt(f1, f2):
    return f1.read()==f2.read()
at = alphatree('*')
f = open('tst1.txt','r')
f1 = open('tst1out.txt','r')
f2 = open('realout.txt','w')
for a0 in range(int(f.readline())):
    op, contact = f.readline().split()
    lstc = [letter for letter in contact]
    eval('at.'+op+'(lstc)')
    #atprn(at)
f2 = open('realout.txt','r')
print(matchtxt(f1,f2))
f.close();f1.close();f2.close()
