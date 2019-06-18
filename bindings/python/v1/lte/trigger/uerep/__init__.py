#!/usr/bin/env python3
"""Useful constants and definitions for Empower LTE trigger UE Report Message"""

#
# Copyright (c) 2018 FBK-CREATENET
# AUTHOR- Abin Ninan Thomas
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.
import ctypes as ct
from enum import IntEnum


class _EnbIdT(ct.c_uint64):
    pass

class _CellIdT(ct.c_uint16):
    pass

class _ModIdT(ct.c_uint32):
    pass

class _RntiIdT(ct.c_uint16):
    pass

class _PlmnIdT(ct.c_uint32):
    pass

class _ImsiIdT(ct.c_uint64):
    pass

class _TmsiIdT(ct.c_uint32):
    pass

class _TLVType(ct.c_uint16):
    pass

class _TLVLength(ct.c_uint16):
    pass

class _HdrTLV(ct.Structure):
    _pack_ = 1
    _fields_ = [('type', _TLVType),
                ('length', _TLVLength)
               ]

class _UeRepState(ct.Structure):
    _pack_ = 1
    _fields_ = [('rnti', _RntiIdT),
                ('state', ct.c_uint8)
               ]

class _UeRepStateTLV(ct.Structure):
    _pack_ = 1
    _fields_ = [('header', _HdrTLV),
                ('body', _UeRepState)
               ]

class _UeRepIdentity(ct.Structure):
    _pack_ = 1
    _fields_ = [('rnti', _RntiIdT),
                ('plmn', _PlmnIdT),
                ('imsi', _ImsiIdT),
                ('tmsi', _TmsiIdT)
               ]

class _UeRepIdentityTLV(ct.Structure):
    _pack_ = 1
    _fields_ = [('header', _HdrTLV),
                ('body', _UeRepIdentity)
               ]

class _UeRepReq(ct.Structure):
    _pack_ = 1
    _fields_ = [('dummy', ct.c_uint8)]


####OPAQUE STRUCTS########
#enum definition
class CEnum(IntEnum):
    """enum definition"""
    @classmethod
    def from_param(cls, self):
        if not isinstance(self, cls):
            raise TypeError
        return self


class _UeRepStatus(CEnum):
    """enum definition"""
    UE_STATUS_INVALID = 0
    UE_STATUS_RADIO_CONNECTED = 1
    UE_STATUS_RADIO_DISCONNECTED = 2
    UE_STATUS_RCC_IDLE = 3
    UE_STATUS_RRC_CONNECTED = 4
    UE_STATUS_MAX = 5

class OperationType(CEnum):
    """enum definition"""
    EP_OPERATION_UNSPECIFIED = 0
    EP_OPERATION_SUCCESS = 1
    EP_OPERATION_FAIL = 2
    EP_OPERATION_NOT_SUPPORTED = 3
    EP_OPERATION_ADD = 4
    EP_OPERATION_REM = 5
    EP_OPERATION_SET = 6
    EP_OPERATION_UNSET = 7
    EP_OPERATION_START = 8
    EP_OPERATION_STOP = 9

class _UeDet(ct.Structure):
    _fields_ = [
        ('plmn', _PlmnIdT),
        ('rnti', _RntiIdT),
        ('imsi', _ImsiIdT),
        ('tmsi', _TmsiIdT),
        ('state', ct.c_uint8)
        ]
