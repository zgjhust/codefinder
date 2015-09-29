#!/usr/bin/python
# -*- encode:utf-8 -*-

import re
import json
import os


codes = {}

if __name__ == '__main__':

    if not os.path.exists('../formatted/codes_db2codes.txt'):
        s = open('../original/dsnc1m0a.txt').read()
        rlt = re.split('(^[-+]?\d{3,6}\s)|(^00[A-Z0-9]{6}\r\n)',
                       s, maxsplit=0, flags=re.MULTILINE)
        for i in range(0, len(rlt)-3, 3):
            codes[rlt[i+1].strip('\r\n').strip() if rlt[i+1] else
                  rlt[i+2].strip('\r\n').strip()] = rlt[i+3].strip('\r\n')
        json.dump(codes, open('../formatted/codes_db2codes.txt', 'w'),
                  encoding='gbk')
