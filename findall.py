import re

import re
xx = """guru99 
careerguru99	
selenium
sea"""
k1 = re.findall(r"^\w", xx)
k2 = re.findall(r"^\w", xx, re.MULTILINE)
print(k1)
print(k2)

