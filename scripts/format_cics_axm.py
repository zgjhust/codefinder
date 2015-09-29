#!/usr/bin/python
# -*- encode:utf-8 -*-

import re
import json
import os


codes = {}

if __name__ == '__main__':

    if not os.path.exists('../formatted/codes_axm.txt'):
        s = open('../original/dfhg4g00_axm.txt').read()
        rlt = re.split('(^AXM[A-Z]{2}\d{4}[A-Z]?)',
                       s, maxsplit=0, flags=re.MULTILINE)
        for i in range(0, len(rlt)-2, 2):
            codes[rlt[i+1].strip('\r\n').strip()] = rlt[i+2].strip('\r\n')
        json.dump(codes, open('../formatted/codes_axm.txt', 'w'),
                  encoding='gbk')
