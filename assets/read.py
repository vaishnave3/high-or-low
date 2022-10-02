import re
import random

f1 = open("sourceCode.txt", "r", encoding='utf-8')
l = []
for line in f1:
    x = re.findall("tt[0-9][0-9][0-9]{5}", line)
    if len(x) == 1:
        if len(l) == 0:
            l.append(x[0])
        if l[len(l)-1] != x[0]:
            l.append(x[0])

f = open("listTitles.txt", "w")
for i in l:
    f.write(i)
    f.write("\n")

