#!/usr/bin/env python3
""" Definitions and constans required for an cell measurement message"""

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

class _TLVType(ct.c_uint16):
    pass

class _TLVLength(ct.c_uint16):
    pass

class _HdrTLV(ct.Structure):
    _pack_ = 1
    _fields_ = [('type', _TLVType),
                ('length', _TLVLength)
               ]

class _CellPRBRep(ct.Structure):
    _pack_ = 1
    _fields_ = [('DL_res', ct.c_uint8),
                ('DL_used', ct.c_uint32),
                ('UL_res', ct.c_uint8),
                ('UL_used', ct.c_uint32)
               ]

class _CellPRBRepTLV(ct.Structure):
    _pack_ = 1
    _fields_ = [('header', _HdrTLV),
                ('body', _CellPRBRep)
               ]


class _CellPRBMeasTLV(ct.Structure):
    _pack_ = 1
    _fields_ = [('header', _HdrTLV)
               ]


####OPAQUE STRUCTS

class _CellPRBRepInfo(ct.Structure):
    _fields_ = [
        ('DL_prbs', ct.c_uint8),
        ('DL_prbs_used', ct.c_uint32),
        ('UL_prbs', ct.c_uint8),
        ('UL_prbs_used', ct.c_uint32),
        ]


class _CellReports(ct.Structure):
    _fields_ = [
        ('prb', _CellPRBRepInfo)
        ]
