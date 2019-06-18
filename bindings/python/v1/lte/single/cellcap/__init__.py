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

class _TLVType(ct.c_uint16):
    pass

class _TLVLength(ct.c_uint16):
    pass

class _CellCapDet(ct.Structure):
    _pack_ = 1
    _fields_ = [
        ('pci', ct.c_uint16),
        ('feat', ct.c_uint32),
        ('DL_earfcn', ct.c_uint16),
        ('DL_prbs', ct.c_uint8),
        ('UL_earfcn', ct.c_uint16),
        ('UL_prbs', ct.c_uint8),
        ('max_ues', ct.c_uint16)
        ]


class _CellDetails(ct.Structure):
    _fields_ = [
        ('pci', ct.c_uint16),
        ('feat', ct.c_uint32),
        ('DL_earfcn', ct.c_uint16),
        ('UL_earfcn', ct.c_uint16),
        ('DL_prbs', ct.c_uint8),
        ('UL_prbs', ct.c_uint8),
        ('max_ues', ct.c_uint16)
        ]

class _HdrTLV(ct.Structure):
    _pack_ = 1
    _fields_ = [('type', _TLVType),
                ('length', _TLVLength)
               ]

class _CcapTLV(ct.Structure):
    _fields_ = [
        ('header', _HdrTLV),
        ('body', _CellCapDet)
        ]

class _CellCapReq(ct.Structure):
    _pack_ = 1
    _fields_ = [('dummy', ct.c_uint8)
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


class CellcapType(CEnum):
    """enum definition"""
    EP_CCAP_NOTHING = 0
    EP_CCAP_UE_REPORT = 1
    EP_CCAP_UE_MEASURE = 2
    EP_CCAP_CELL_MEASURE = 4
    EP_CCAP_X2_HANDOVER = 8


class TLVType(CEnum):
    """enum definition"""
    EP_TLV_INVALID = 0
    EP_TLV_RNTI_REPORT = 0x0001
    EP_TLV_CELL_CAP = 0x0100
    EP_TLV_CELL_PRB_REQ = 0x0101
    EP_TLV_CELL_PRB_REPORT = 0x0102
    EP_TLV_RAN_MAC_SCHED = 0x0500
    EP_TLV_RAN_SLICE_MAC_RES = 0x0501
    EP_TLV_RAN_SLICE_MAC_SCHED = 0x0502
    EP_TLV_RAN_CAP = 0x0503
    EP_TLV_UE_RRC_MEAS = 0x0600
    EP_TLV_UE_RRC_REPORT = 0x0601
    EP_TLV_UE_REP_ID = 0x0700
    EP_TLV_UE_REP_STATE = 0x0701
