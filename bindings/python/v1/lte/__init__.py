#!/usr/bin/env python3


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

class _SchedIdT(ct.c_uint32):
    pass

#RAN types
class _SliceIdT(ct.c_uint64):
    pass


#TLV Types
class _TlvTypeT(ct.c_uint16):
    pass

class _TlvLengthT(ct.c_uint16):
    pass
#enb_id_t.restype = ct.c_uint64

class _HeaderId(ct.Structure):
    _pack_ = 1
    _fields_ = [('enb_id_t', _EnbIdT),
                ('cell_id_t', _CellIdT),
                ('mod_id_t', _ModIdT)
               ]

class _Header(ct.Structure):
    _pack_ = 1
    _fields_ = [('type', ct.c_uint8),
                ('vers', ct.c_uint8),
                ('id', _HeaderId),
                ('flags', ct.c_uint16),
                ('seq', ct.c_uint32),
                ('length', ct.c_uint16),
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


class MessageType(CEnum):
    """Message Type"""
    EP_TYPE_INVALID_MSG = 0
    EP_TYPE_SINGLE_MSG = 1
    EP_TYPE_SCHEDULE_MSG = 2
    EP_TYPE_TRIGGER_MSG = 3
    EP_TYPE_EXTENDED = 0xff

(EP_TYPE_INVALID_MSG, EP_TYPE_SINGLE_MSG, EP_TYPE_SCHEDULE_MSG, EP_TYPE_TRIGGER_MSG,
 EP_TYPE_EXTENDED) = (0, 1, 2, 3, 0xff)

class ActionType(IntEnum):
    """enum definition"""
    EP_ACT_INVALID = 0
    EP_ACT_HELLO = 1
    EP_ACT_ECAP = 2
    EP_ACT_CCAP = 3
    EP_ACT_UE_REPORT = 4
    EP_ACT_UE_MEASURE = 5
    EP_ACT_MAC_REPORT = 6
    EP_ACT_HANDOVER = 7
    EP_ACT_RAN_SETUP = 9
    EP_ACT_RAN_SLICE = 10

EMPOWER_VERSION = 1
