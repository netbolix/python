#!/usr/bin/env python3

import sys


# define shebao
def shebao(gz):
      shebao = gz*0.165
      return shebao

def yb(id,sh):
         ys_se = format(sh,".2f")
         print("%d:%s" % (id,ys_se))

def gs(ys_sde):
      if ys_sde < 0:
         return 0
      elif ys_sde <= 1500:
         return ys_sde*0.03
      elif ys_sde <= 4500:
         return ys_sde*0.1-105
      elif ys_sde <= 9000:
         return ys_sde*0.2-555
      elif ys_sde <= 35000:
         return ys_sde*0.25-1005
      elif ys_sde <= 50000:
         return ys_sde*0.3-2755
      elif ys_sde <= 80000:
         return ys_sde*0.35-5505
      else :
         return ys_sde*0.45-13505


#class ParameterError(Exception):
#	''' A use-defined exception class. '''
#        def __init__(self):
#		Exception.__init__(self)

# format gz of date and the nubmer of cs

#try:
#   cs == len(sys.argv)
#   if cs > 2:
#	raise ParameterError
#except ParameterError:
#   print("Parameter Error")
#   sys.exit(0)

if __name__ == '__main__':
    for arg in sys.argv[1:]:
       userinfo = arg.split(':')
       try:
          id = int(userinfo[0])
          gz = int(userinfo[1])
#          print(id,gz)
       except:
          print("Paremeter Error")
          sys.exit()
       sb = shebao(gz)
       ys_sde = gz-sb-3500
       ys_sde=gs(ys_sde)
       sh = gz-sb-ys_sde
       yb(id,sh)
