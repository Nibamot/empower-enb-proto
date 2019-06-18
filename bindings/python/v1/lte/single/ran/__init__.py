#!/usr/bin/env python3
""" Classes/Structs/enums/constants required for RAN"""

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
from v1.lte.single.cellcap import _HdrTLV


class _SchedIdT(ct.c_uint32):
    pass

class _SliceIdT(ct.c_uint64):
    pass

class _RntiIdT(ct.c_uint16):
    pass

class _CellIdT(ct.c_uint16):
    pass

#enum definition
class CEnum(IntEnum):
    """enum definition"""
    @classmethod
    def from_param(cls, self):
        if not isinstance(self, cls):
            raise TypeError
        return self

class RanL1Caps(CEnum):
    EP_RAN_LAYER1_CAP_NOTHING = 0


class RanL2Caps(CEnum):
    EP_RAN_LAYER2_CAP_NOTHING = 0
    EP_RAN_LAYER2_CAP_RBG_SLICING = 1
    EP_RAN_LAYER2_CAP_PRB_SLICING = 2

class RanL3Caps(CEnum):
    EP_RAN_LAYER3_CAP_NOTHING = 0

class _RanSliceCaps(ct.Structure):
    _pack_ = 1
    _fields_ = [('pci', ct.c_uint16),
                ('l1_caps', ct.c_uint32),
                ('l2_caps', ct.c_uint32),
                ('l3_caps', ct.c_uint32),
                ('mac_sched', ct.c_uint32),
                ('max_slices', ct.c_uint16)
               ]

class _RanSliceCapsTLC(ct.Structure):
    _pack_ = 1
    _fields_ = [('header', _HdrTLV),
                ('body', _RanSliceCaps)
               ]

###RAN SLICING SETUP#######

class _RanMacSched(ct.Structure):
    _pack_ = 1
    _fields_ = [('slice_sched', _SchedIdT)
               ]

class _RanMacSchedTLV(ct.Structure):
    _pack_ = 1
    _fields_ = [('header', _HdrTLV),
                ('body', _RanMacSched)
               ]

class _RanSetup(ct.Structure):
    _pack_ = 1
    _fields_ = [('layer1_cap', ct.c_uint32),
                ('layer2_cap', ct.c_uint32),
                ('layer3_cap', ct.c_uint32)
               ]

###RAN SLICING SLICE SETUP#######

class _RanSliceSched(ct.Structure):
    _pack_ = 1
    _fields_ = [('user_sched', _SchedIdT)
               ]

class _RanSliceSchedTLV(ct.Structure):
    _pack_ = 1
    _fields_ = [('header', _HdrTLV),
                ('body', _RanSliceSched)
               ]

class _RanSliceRes(ct.Structure):
    _pack_ = 1
    _fields_ = [('rbgs', ct.c_uint16)
               ]

class _RanSliceResTLV(ct.Structure):
    _pack_ = 1
    _fields_ = [('header', _HdrTLV),
                ('body', _RanSliceRes)
               ]

class _RanSliceInf(ct.Structure):
    _pack_ = 1
    _fields_ = [('id', _SliceIdT)
               ]

EP_RAN_USERS_MAX = 32
USERS = _RntiIdT*EP_RAN_USERS_MAX
####OPAQUE STRUCTS
class _RanSliceL2Det(ct.Structure):
    _fields_ = [('usched', _SchedIdT),
                ('rbgs', ct.c_uint16)
               ]

class _RanSliceDet(ct.Structure):
    _fields_ = [('nof_users', ct.c_uint32),
                ('users', USERS),
                ('l2', _RanSliceL2Det)
               ]

EP_RAN_SCHED_INVALID = 0

class _RanMacDet(ct.Structure):
    _fields_ = [('slice_sched', _SchedIdT)
               ]

class _RanL2Det(ct.Structure):
    _fields_ = [('mac', _RanMacDet)
               ]

class _RanSetupDet(ct.Structure):
    _fields_ = [('pci', _CellIdT),
                ('l1_mask', ct.c_uint32),
                ('l2_mask', ct.c_uint32),
                ('l3_mask', ct.c_uint32),
                ('l2', _RanL2Det),
                ('max_slices', ct.c_uint16),
               ]
