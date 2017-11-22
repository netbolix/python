#!/usr/bin/env python3

import sys

class Get_canshu(object):
    def __init__(self):
        self.canshu = {}
        args = sys.argv[1:]
        print(args)
        index = args.index('-c')
        self.canshu['config'] =  args[index+1]
        print(self.canshu['config'])
        index = args.index('-d')
        self.canshu = {'userdata' : args[index+1]}
        print(self.canshu['userdata'])
        index = args.index('-o')
        self.canshu = {'outfile': args[index+1]}
        print(self.canshu['outfile'])
        print(type(self.canshu))
#    def get_cs(self):
#        print(self.canshu['config'])

class Config(object):
    def __init__(self,configfile):
        with open(configfile,'r') as file:
            for line in file:
                line_strip = line.strip()
                line_split = line.split('=')
                self._config = {'line_split[0]':'line_split[1]'}
    
    def get_config(self,name):
        return self._config[name]


#class UserData(object):
#    def __init__(self,userdatafile):
#        with open(userdatafile,'r' with file:
#            for line in file:
#                line_split = line.split(',')
#                self._uesrdata = {'line_split[0]':'line_split[1]'}
    
#    def caculator(self):
#        for id,gongzi in self._userdata.items():


if __name__ == '__main__':
   s = Get_canshu()
   #a = s.get_cs()           
