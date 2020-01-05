import re, sys
dt = '12-2-2016'
pattern = '(\d{1,2})-(\d{1,2})-(\d{2,4})'
m = re.search(pattern, dt)
if m:
    month = m.group(2)
    print(month)
