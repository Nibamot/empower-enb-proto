#!/usr/bin/env python3
"""Base class for a LTE single Empower cellcap Message request"""
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
from v1.lte.single.cellcap.ltescellcap import LTESCellCap


class LTESCellCapReq(LTESCellCap):
    """Class that deals with a single Cellcap request"""
    def __init__(self, **kwargs):
        super().__init__()
        self.proto = ct.CDLL("libemproto.so")
        self._direction = 0
        self._oper = 0
        self._sequence = 0

        #The optional keyword arguments are if the user
        #wants to parse on creating an instance
        if kwargs:
            if 'buf' in kwargs:
                buf = kwargs.get('buf')
            if 'buflen' in kwargs:
                buflen = kwargs.get('buflen')

            self.parse(buf, buflen)


    """def format(self, buf, size):
        #A generic single event message format
        repformat = self.proto.epf_single_ccap_req
        repformat.restype = ct.c_int
        repformat.argtypes = [ct.c_char_p, ct.c_uint, _EnbIdT, _CellIdT,
                              _ModIdT]
        return repformat(buf, size, self._enbid, self._pci, self._modid)


    def parse(self, buf, size):
        #parse a single event EnB capabilities reply
        repparse = self.proto.epp_single_ccap_req
        repparse.restype = ct.c_int
        repparse.argtypes = [ct.c_char_p, ct.c_uint]
        return repparse(buf, size)"""
