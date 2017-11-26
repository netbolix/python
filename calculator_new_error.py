#!/usr/bin/env python3

import sys
import csv
from collections import namedtuple

IncomeTaxQuickLookupItem = namedtuple(
     'IncomeTaxQuickLookupItem',
     ['start_point','tax_rate','quick_subtractor']
)

INCOME_TAX_QUICK_LOOKUP_TABLE = [
    IncomeTaxQuickLookupItem(80000,0.45,13505),
    IncomeTaxQuickLookupItem(55000,0.35,5505),
    IncomeTaxQuickLookupItem(35000,0.30,2755),
    IncomeTaxQuickLookupItem(9000,0.25,1005),
    IncomeTaxQuickLookupItem(4500,0.2,555),
    IncomeTaxQuickLookupItem(1500,0.1,105),
    IncomeTaxQuickLookupItem(0,0.03,0)
]

class Args(object):
    def __init__(self):
        self.args = sys.argv[1:]

    def _value_after_option(self,option):
        try:
            index = self.args.index(option)
            return self.args[index+1]
        except (ValueError,IndexError):
            print('Parameter Error')
            sys.exit(0)

    @property
    def config_path(self):
        return self._value_after_option('-c')


    @property
    def userdata_path(self):
        return self._value_after_option('-d')


    @property
    def export_path(self):
         return self._value_after_option('-o')

args = Args()

class Config(object):
    def __init__(self):
        config_path = args.config_path
        self.config = {}
        with open(config_path,'r') as file:
            for line in file.readlines():
                key,value = line.strip().split('=')
                try:
                    self.config[key] = float(value)
                except ValueError:
                    print('Parameter Error')

    def get_config(self,key):
        try:
            return self.config[key]
        except KeyError:
            print('Config Error')
            sys.exit(0)

    @property
    def shebaojishu_l(self):
        return self.get_config('JiShuL')


    @property
    def shebaojishu_h(self):
        return self.get_config('JiShuH')

    @property
    def shebaobili(self):
        return sum([
            self.get_config('YangLao'),
            self.get_config('YiLiao'),
            self.get_config('ShiYe'),
            self.get_config('GongShang'),
            self.get_config('ShengYu'),
            self.get_config('GongJiJin'),
        ])


config = Config()

class UserData(object):
    def __init__(self):
        userdata_path = args.userdata_path
        self.userdata = [] 
        with open(userdata_path,'r') as file:
            for line in file.readlines():
                user_id,gongzi_string = line.strip().split(',')
                try:
                    gongzi_sq = int(gongzi_string)
                except ValueError:
                    print('ParaMeter Error')
                    sys.exit(0)
                self.userdata.append((user_id,gongzi_sq))
    
    @staticmethod
    def shebaojin(gongzi_sq):
        if gongzi_sq < config.shebaojishu_l:
            return config.shebaojishu_l * \
                config.shebaobili
        if gongzi_sq > config.shebaojishu_h:
            return config.shebaojishu_h * \
                config.shebaobili
            return gongzi_sq * shebaobili


    @classmethod  
    def shui_gongzi_sh(cls,gongzi_sq):
        shebaojin = cls.shebaojin(gongzi_sq)
        gongzi_sb = gongzi_sq - shebaojin
        gongzi_ks = gongzi_sb - 3500
        if gongzi_ks < 0:
            return '0.00','{:.2f}'.format(gongzi_sb)
        for item in INCOME_TAX_LOOKUP_TABLE:
            if gongzi_ks > item.start_point:
                ks = gongzi_ks * item.tax_rate - item.quick_subtractor
                return '{:.2f}'.format(ks),'{:.2f}'.format(gongzi_sb - ks)
 

    def Caculator(self):
        result = []
        for user_id,gongzi_sq in self.userdata:
            data = [user_id,gongzi_sq]
            shebaoji = '{:.2f}'.format(self.shebaojin(gongzi_sq))
            ks,gongzi_sh = self.shui_gongzi_sh(gongzi_sq)
            data += [shebaoji,ks,gongzi_sh]
            result.append(data)
        return result

    def export(self,default='csv'):
        result = self.Caculator()
        with open(args.export_path,'w',newline='') as f:
            writer = csv.write(f)
            writer.writerows(result)


if __name__ == '__main__':
    calculator = UserData()
    calculator.export()
