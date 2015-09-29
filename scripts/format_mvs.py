#!/usr/bin/python
# -*- encode:utf-8 -*-

import re
import json
import sys
import os
import codecs


codes = {}

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print '''
        usage: python test_mvs.py source_file_name  codes_file_name
        '''
        sys.exit(1)
    codes_file_name = sys.argv[2]
    source_file_name = sys.argv[1]
    if not os.path.exists(codes_file_name):
        s = codecs.open(source_file_name, encoding='utf-16').read()
        rlt = re.split(u'(^[A-Z]{3}[A-Z]{0,4}\d{2,5}[A-Z]?)',
                       s, maxsplit=0, flags=re.MULTILINE)
        for i in range(0, len(rlt)-2, 2):
            codes[rlt[i+1].strip('\r\n').strip()] = rlt[i+2].strip('\r\n')
        json.dump(codes, open(codes_file_name, 'w'), encoding='gbk')
