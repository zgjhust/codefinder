#!/usr/bin/python
# -*- encode:utf-8 -*-

import re
import json
import os


codes = {}

if __name__ == '__main__':

    if not os.path.exists('../formatted/codes_dfh2.txt'):
        s = open('../original/dfhgag00_dfhv2.txt').read()
        rlt = re.split('(^DFH[A-Z]{0,2}\d{4}[A-Z]?)',
                       s, maxsplit=0, flags=re.MULTILINE)
        for i in range(0, len(rlt)-2, 2):
            codes[rlt[i+1].strip('\r\n').strip()] = rlt[i+2].strip('\r\n')
        json.dump(codes, open('../formatted/codes_dfh2.txt', 'w'),
                  encoding='gbk')
