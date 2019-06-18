#!/usr/bin/env python3
"""Base class for a generic LTE Empower Message"""
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
from v1.lte.trigger.uerep.ltetuerep import LTETUeRep
from v1.lte.trigger.uerep import _EnbIdT
from v1.lte.trigger.uerep import _CellIdT
from v1.lte.trigger.uerep import _ModIdT
from v1.lte.trigger.uerep import _UeDet

class LTETUeRepRep(LTETUeRep):
    """Class that deals with a trigger UE Report reply"""
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

    def format(self, buf, size, uedet):
        """A generic trigger event UE Report message format"""
        repformat = self.proto.epf_trigger_uerep_rep
        repformat.restype = ct.c_int
        repformat.argtypes = [ct.c_char_p, ct.c_uint, _EnbIdT, _CellIdT,
                              _ModIdT, ct.c_uint32, ct.c_uint32,
                              ct.POINTER(_UeDet)]
        return repformat(buf, size, self._enbid, self._pci, self._modid,
                         ct.c_uint32(1), ct.c_uint32(1), (uedet))

    def parse(self, buf, size):
        """parse a trigger event UE Report reply"""
        repparse = self.proto.epp_trigger_uerep_rep
        repparse.restype = ct.c_int
        repparse.argtypes = [ct.c_char_p, ct.c_uint, ct.POINTER(ct.c_uint32),
                             ct.c_uint32, ct.POINTER(_UeDet)]
        return repparse(buf, size, ct.pointer(ct.c_uint32()), ct.c_uint32(),
                        ct.pointer(_UeDet()))

    def failformat(self, buf, size):
        """A  trigger UE report format fail event message"""
        repfailformat = self.proto.epf_trigger_uerep_rep_fail
        repfailformat.restype = ct.c_int
        repfailformat.argtypes = [ct.c_char_p, ct.c_uint, _EnbIdT, _CellIdT,
                                  _ModIdT]
        return repfailformat(buf, size, self._enbid, self._pci, self._modid)
