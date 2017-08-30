import urllib.request
import re
link="http://www.teenreads.com/reviews/flawed"
f=urllib.request.urlopen(link)
myfile=f.read()
s=re.search(r'<div>(.*?)</div>',str(myfile))
m=s.group()
sentences=re.split(r'[\.\?!][ ]',m)
for s in sentences:
    print(s)