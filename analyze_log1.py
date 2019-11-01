import re
import sys
import pprint

with open(sys.argv[1]) as f:
    events = []
    while(not re.search(r"^Log Buffer", next(f), flags=re.IGNORECASE)):
        pass   
    next(f)
    d = {}
    for line in f:
        event = line.split(":")[3].strip()
        events.append(event)
        if event not in d:
            d[event] = 1
        else:
            d[event] +=1
    pprint.pprint(d)

list_sorted = sorted(d.items(), key=lambda x: int(x[1]), reverse=True)
pprint.pprint(list_sorted)
