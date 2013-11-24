url = 'http://compsoc.dur.ac.uk/whitespace/name.ws'
url = 'http://compsoc.dur.ac.uk/whitespace/fibonacci.ws'
from urllib.request import urlopen
s = urlopen(url).read().decode()
s = ''.join(c for c in s if c in " \t\n")
s = s.translate(dict(zip(map(ord," \t\n"), map(ord,"STL"))))
print(repr(s))
