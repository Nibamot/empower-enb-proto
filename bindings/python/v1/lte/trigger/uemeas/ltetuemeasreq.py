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
from v1.lte.trigger import DIRECTION_REQUEST
from v1.lte.trigger import OperationType
from v1.lte.trigger.uemeas import _EnbIdT
from v1.lte.trigger.uemeas import _CellIdT
from v1.lte.trigger.uemeas import _ModIdT
from v1.lte.trigger.uemeas import _UeMeasurement
from v1.lte.trigger.uemeas.ltetuemeas import LTETUeMeas

class LTETUeMeasReq(LTETUeMeas):
    """Class that deals with a trigger UE Measure request"""
    def __init__(self, **kwargs):
        super().__init__()
        self.proto = ct.CDLL("libemproto.so")
        self._direction = DIRECTION_REQUEST
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

    def format(self, buf, size, uemeas):
        """A  trigger UE Measure event message format"""
        repformat = self.proto.epf_trigger_uemeas_req
        repformat.restype = ct.c_int
        repformat.argtypes = [ct.c_char_p, ct.c_uint, _EnbIdT, _CellIdT,
                              _ModIdT, OperationType, ct.POINTER(_UeMeasurement)]
        return repformat(buf, size, self._enbid, self._pci, self._modid,
                         OperationType.EP_OPERATION_START, uemeas)


    def parse(self, buf, size):
        """parse a trigger event UE Measure reply"""
        repparse = self.proto.epp_trigger_uemeas_req
        repparse.restype = ct.c_int
        repparse.argtypes = [ct.c_char_p, ct.c_uint, ct.POINTER(_UeMeasurement)]
        return repparse(buf, size, ct.pointer(_UeMeasurement()))
