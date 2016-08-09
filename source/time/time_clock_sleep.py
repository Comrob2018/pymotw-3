#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header

import time

for i in range(6, 1, -1):
    print('{} {:0.2f} {:0.2f}'.format(
        time.ctime(), time.time(), time.clock())
    )
    print('Sleeping', i)
    time.sleep(i)
