# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   interview_test.py
@Contact :   9824373@qq.com
@Desc    :
@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-22     zhan        1.0         None
'''

import sys
from collections import defaultdict
from typing import List


def addEle(mydict,dict_revers,strLst,n):
    tmpKey = set()
    for istr in strLst:
        zip_str = zipStr(istr, n)
        mydict[zip_str].append(istr)
        tmpKey.add(zip_str)

    for k in tmpKey:
        if len(mydict[k])>1:
            nexStrs = mydict.pop(k)
            addEle(mydict,dict_revers,nexStrs,n+1)
        else:
            dict_revers[mydict[k][0]] = k


def zipStr(mystr,n):
    if len(mystr)<=n+1:
        zip_str = mystr
    else:
        zip_str = mystr[:n-1] + str(len(mystr) - n) + mystr[-1]

    return zip_str

if __name__ == '__main__':
    # strLst = [line.strip() for line in sys.stdin]
    strLst = ['like',
              'god',
              'internal',
              'me',
              'internet',
              'interval',
              'intension',
              'face',
              'intrusion', ]

    mydict = defaultdict(list)
    mydict_revers = {}

    addEle(mydict,mydict_revers,strLst,2)

    for istr in strLst:
        print(mydict_revers[istr])

