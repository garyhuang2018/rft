# encoding= utf-8
# __author__= gary
import os

p = os.popen("ping 192.192.255.146")
x = p.read()
p.close()
if x.count('temeout'):
    print("ping不通")
else:
    print("ping通了")
