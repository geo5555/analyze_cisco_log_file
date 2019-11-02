import re
import sys
from collections import Counter
import pprint

with open(sys.argv[1]) as f:
    c = Counter()
    while(not re.search(r"^Log Buffer", next(f), flags=re.IGNORECASE)):
        pass   
    next(f)
    for line in f:
        event = line.split(":")[3].strip()[1:]
        c[event] +=1
    pprint.pprint(c)
    pprint.pprint(c.most_common(10))
