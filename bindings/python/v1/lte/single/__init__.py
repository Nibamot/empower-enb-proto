#!/usr/bin/env python3
"""Useful constants and definitions for Empower LTE Single Message"""

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

class _SingleType(ct.c_uint16):
    pass

class _SingleHeader(ct.Structure):
    _pack_ = 1
    _fields_ = [('type', _SingleType),
                ('op', ct.c_uint8)
               ]

CHAR_P = ct.POINTER(ct.c_char_p)
#enum definition
class CEnum(IntEnum):
    """enum definition"""
    @classmethod
    def from_param(cls, self):
        if not isinstance(self, cls):
            raise TypeError
        return self


class ActionType(CEnum):
    """enum definition"""
    EP_ACT_INVALID = 0
    EP_ACT_HELLO = 1
    EP_ACT_ECAP = 2
    EP_ACT_CCAP = 3
    EP_ACT_UE_REPORT = 4
    EP_ACT_UE_MEASURE = 5
    EP_ACT_CELL_MEASURE = 6
    EP_ACT_HANDOVER = 7
    EP_ACT_RAN_SETUP = 9
    EP_ACT_RAN_SLICE = 10


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
