from urllib.request import *

u=urlopen('http://www.python.org')

print('url:',u.geturl())

print('Meta information:', u.info())

print('http status:', u.getcode())

content = u.read()

print(content)
