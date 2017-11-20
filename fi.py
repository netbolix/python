#!/usr/bin/env python3

filename = '/etc/protocols'
f = open(filename)
try:
	f.write('shiyanlou')
except:
	print("File write Error")
finally:
	print("finally")
	f.close()

