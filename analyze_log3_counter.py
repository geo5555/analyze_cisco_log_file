import re
import sys
from collections import Counter, defaultdict
import pprint

with open(sys.argv[1]) as f:
    events = []
    while(not re.search(r"^Log Buffer", next(f), flags=re.IGNORECASE)):
        pass   
    next(f)
    for line in f:
        event = line.split(":")[3].strip()
        events.append(event)
    c = Counter(events)
    pprint.pprint(c)
    pprint.pprint(c.most_common(10))
