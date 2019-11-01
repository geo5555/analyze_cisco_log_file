import re
import sys
from collections import Counter, defaultdict
import pprint

#not recommended for large log files
events = re.findall(r"%([a-z0-9_-]+):", open(sys.argv[1]).read(), flags=re.MULTILINE | re.IGNORECASE)
pprint.pprint(Counter(events))