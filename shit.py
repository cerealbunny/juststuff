import os
import os.path
import re
def gendict(dir):
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

print(gendict('/Users/michaeltang'))