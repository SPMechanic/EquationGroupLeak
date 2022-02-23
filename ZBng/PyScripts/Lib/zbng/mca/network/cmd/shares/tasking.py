# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: tasking.py
import mcl_platform.tasking
from tasking_dsz import *
_fw = mcl_platform.tasking.GetFramework()
if _fw == 'dsz':
    RPC_INFO_MAP = dsz.RPC_INFO_MAP
    RPC_INFO_LIST = dsz.RPC_INFO_LIST
    RPC_INFO_QUERY = dsz.RPC_INFO_QUERY
    RPC_INFO_QUERY_WMI = dsz.RPC_INFO_QUERY_WMI
else:
    raise RuntimeError('Unsupported framework (%s)' % _fw)