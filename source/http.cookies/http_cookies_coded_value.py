#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

#end_pymotw_header

from http import cookies


c = cookies.SimpleCookie()
c['integer'] = 5
c['string_with_quotes'] = 'He said, "Hello, World!"'

for name in ['integer', 'string_with_quotes']:
    print(c[name].key)
    print('  %s' % c[name])
    print('  value=%r' % c[name].value)
    print('  coded_value=%r' % c[name].coded_value)
    print()
