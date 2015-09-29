#!/usr/bin/python
# -*- encode:utf-8 -*-

import re
import json
import os


codes = {}

if __name__ == '__main__':

    if not os.path.exists('../formatted/codes_db2msg.txt'):
        s = open('../original/dsnm1m0g.txt').read()
        rlt = re.split('(^DSN[A-Z0-9]{5,8})',
                       s, maxsplit=0, flags=re.MULTILINE)
        for i in range(0, len(rlt)-2, 2):
            codes[rlt[i+1].strip('\r\n').strip()] = rlt[i+2].strip('\r\n')
        json.dump(codes, open('../formatted/codes_db2msg.txt', 'w'),
                  encoding='gbk')
