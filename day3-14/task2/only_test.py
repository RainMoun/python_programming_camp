import re

pattern = re.compile('.*?python.*', flags=re.IGNORECASE)
items = re.findall(pattern, 'hello Python  ni')
print(items)