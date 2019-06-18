#!/usr/bin/env python3
"""Base class for a LTE Empower schedule hello Message reply"""
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
from v1.lte.schedule import DIRECTION_REPLY
from v1.lte.schedule.hello.ltechello import LTECHello
from v1.lte.schedule.hello import _EnbIdT
from v1.lte.schedule.hello import _CellIdT
from v1.lte.schedule.hello import _ModIdT


class LTECHelloRep(LTECHello):
    """Class that deals with a scheduled hello reply"""
    def __init__(self, **kwargs):
        super().__init__()
        self.proto = ct.CDLL("libemproto.so")
        self._direction = DIRECTION_REPLY
        self._oper = 0
        self._interval = 2000
        self._sequence = 0

        #The optional keyword arguments are if the user
        #wants to parse on creating an instance
        if kwargs:
            if 'buf' in kwargs:
                buf = kwargs.get('buf')
            if 'buflen' in kwargs:
                buflen = kwargs.get('buflen')

            self.parse(buf, buflen)

    def format(self, buf, size):
        """Format a scheduled hello reply"""
        repformat = self.proto.epf_sched_hello_rep
        repformat.restype = ct.c_int
        repformat.argtypes = [ct.c_char_p, ct.c_uint, _EnbIdT, _CellIdT,
                              _ModIdT, ct.c_uint32, ct.c_uint32]
        return repformat(buf, size, self._enbid, self._pci, self._modid,
                         self._interval, self._id)


    def parse(self, buf, size):
        """Format a scheduled hello reply"""
        repparse = self.proto.epp_sched_hello_rep
        repparse.restype = ct.c_int
        repparse.argtypes = [ct.c_char_p, ct.c_uint, ct.POINTER(ct.c_uint32)]
        return repparse(buf, size, ct.pointer(ct.c_uint32(self._id)))
