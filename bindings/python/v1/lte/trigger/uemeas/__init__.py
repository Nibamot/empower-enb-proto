#!/usr/bin/env python3
"""Useful constants and definitions for Empower LTE trigger UE Measure Message"""

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

class _ModIdT(ct.c_uint32):
    pass

class _MeasIdT(ct.c_uint16):
    pass

class _CellIdT(ct.c_uint16):
    pass

class _RntiIdT(ct.c_uint16):
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

class _UeRRCRep(ct.Structure):
    _pack_ = 1
    _fields_ = [('meas_id', _MeasIdT),
                ('pci', _CellIdT),
                ('rsrp', ct.c_uint16),
                ('rsrq', ct.c_uint16)
               ]

class _UeRRCRepTLV(ct.Structure):
    _pack_ = 1
    _fields_ = [('header', _HdrTLV),
                ('body', _UeRRCRep)
               ]

class _UeRRCMeas(ct.Structure):
    _pack_ = 1
    _fields_ = [('meas_id', _MeasIdT),
                ('rnti', _RntiIdT),
                ('earfcn', ct.c_uint16),
                ('interval', ct.c_uint16),
                ('max_cells', ct.c_int16),
                ('max_meas', ct.c_int16)
               ]

class _UeRRCMeasTLV(ct.Structure):
    _pack_ = 1
    _fields_ = [('header', _HdrTLV),
                ('body', _UeRRCMeas)
               ]


EP_UE_RRC_MEAS_MAX = 8


class _UeRRCReport(ct.Structure):
    _fields_ = [
        ('meas_id', _MeasIdT),
        ('pci', _CellIdT),
        ('rsrp', ct.c_uint16),
        ('rsrq', ct.c_uint16)
        ]

RRCREP = _UeRRCReport*EP_UE_RRC_MEAS_MAX

class _UeReport(ct.Structure):
    _fields_ = [
        ('rrc', RRCREP),
        ('nof_rrc', ct.c_uint32)
        ]

class _UeRRCMeasurement(ct.Structure):
    _fields_ = [
        ('meas_id', _MeasIdT),
        ('rnti', _RntiIdT),
        ('earfcn', ct.c_uint16),
        ('interval', ct.c_uint16),
        ('max_cells', ct.c_int16),
        ('max_meas', ct.c_int16),
        ]

RRCMEAS = _UeRRCMeasurement*EP_UE_RRC_MEAS_MAX

class _UeMeasurement(ct.Structure):
    _fields_ = [
        ('rrc', RRCMEAS),
        ('nof_rrc', ct.c_uint32)
        ]

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
