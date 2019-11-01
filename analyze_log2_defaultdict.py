import re
import sys
from collections import defaultdict
import pprint

with open(sys.argv[1]) as f:
    events = []
    while(not re.search(r"^Log Buffer", next(f), flags=re.IGNORECASE)):
        pass   
    next(f)
    d2 = defaultdict(int)
    for line in f:
        event = line.split(":")[3].strip()
        events.append(event)
        d2[event] +=1
    pprint.pprint(d2)

list_sorted = sorted(d2.items(), key=lambda x: int(x[1]), reverse=True)
pprint.pprint(list_sorted)

