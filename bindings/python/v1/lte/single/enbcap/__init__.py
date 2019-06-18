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
from v1.lte.single.cellcap import _CellDetails
from v1.lte.single.ran import _RanSetupDet

class _EnbIdT(ct.c_uint64):
    pass

class _CellIdT(ct.c_uint16):
    pass

class _ModIdT(ct.c_uint32):
    pass



class _EnbCapRep(ct.Structure):
    _pack_ = 1
    _fields_ = [('cap', ct.c_uint32)
               ]

class _EnbCapReq(ct.Structure):
    _pack_ = 1
    _fields_ = [('dummy', ct.c_uint8)
               ]

EP_ECAP_CELL_MAX = 8

CELLDETAILS = _CellDetails*EP_ECAP_CELL_MAX
RANDETAILS = _RanSetupDet*EP_ECAP_CELL_MAX

class _EnbDetails(ct.Structure):
    _fields_ = [('cells', CELLDETAILS),
                ('nof_cells', ct.c_uint32),
                ('ran', RANDETAILS),
                ('nof_ran', ct.c_uint32)
               ]

#enum definition
class CEnum(IntEnum):
    """enum definition"""
    @classmethod
    def from_param(cls, self):
        if not isinstance(self, cls):
            raise TypeError
        return self


class EnbcapType(CEnum):
    """enum definition"""
    EP_ECAP_NOTHING = 0x0
    EP_ECAP_UE_REPORT = 0x1
    EP_ECAP_UE_MEASURE = 0x2
    EP_ECAP_HANDOVER = 0x4
