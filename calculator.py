
#!/usr/bin/env python3

import sys

class ParameterError(Exception):
	''' A use-defined exception class. '''
        def __init__(self):
		Exception.__init__(self)

# format gz of date and the nubmer of cs

try:
   cs == len(sys.argv)
   if cs > 2:
	raise ParameterError
except ParameterError:
   print("Parameter Error")
   sys.exit(0)

try:
  gz = int(sys.argv[1]
  sys.exit(0)

ys_sde = gz-3500

if ys_sde < 0:
     print(format(0,".2f"))
elif ys_sde <= 1500:
     ys_se = format(ys_sde*0.03,".2f")
     print(ys_se)
elif ys_sde <= 4500:
     ys_se = format(ys_sde*0.1-105,".2f")
     print(ys_se)
elif ys_sde <= 9000:
     ys_se = format(ys_sde*0.2-555,".2f")
     print(ys_se)
elif ys_sde <= 35000:
     ys_se = format(ys_sde*0.25-1005,".2f")
     print(ys_se)
elif ys_sde <= 50000:
     ys_se = format(ys_sde*0.3-2755,".2f")
     print(ys_se)
elif ys_sde <= 80000:
     ys_se = format(ys_sde*0.35-5505,".2f")
     print(ys_se)
else :
     ys_se = format(ys_sde*0.45-13505,".2f")
     print(ys_se)
