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
from v1.empowermsg import EmpowerMsg
from v1.lte import _EnbIdT
from v1.lte import _CellIdT
from v1.lte import _ModIdT
from v1.lte import EP_TYPE_SCHEDULE_MSG
from v1.lte import EMPOWER_VERSION
from v1.lte import MessageType

class LTEMsg(EmpowerMsg):
    """child of the EmpowerMsg class for LTE domain"""
    def __init__(self, **kwargs):
        super().__init__()
        self.proto = ct.CDLL("libemproto.so")
        self._type = 0
        self._version = 1
        self._enbid = 1
        self._pci = 0
        self._modid = 0
        self._length = 0

        #The optional keyword arguments are if the user
        #wants to parse on creating an instance
        if kwargs:
            if 'buf' in kwargs:
                buf = kwargs.get('buf')
            if 'buflen' in kwargs:
                buflen = kwargs.get('buflen')

            self.parse(buf, buflen)


    @property
    def type(self):
        """Return type of the message"""
        return self._type

    @type.setter
    def type(self, _type):
        self._type = _type

    @property
    def version(self):
        """Return version of the message"""
        return self._version

    @version.setter
    def version(self, _version):
        self._version = _version

    @property
    def enbid(self):
        """Return enbid of the message"""
        return self._enbid

    @enbid.setter
    def enbid(self, _enbid):
        self._enbid = _enbid

    @property
    def pci(self):
        """Return cell identifier of the message"""
        return self._pci

    @pci.setter
    def pci(self, _pci):
        self._pci = _pci

    @property
    def modid(self):
        """Return modid of the message"""
        return self._modid

    @modid.setter
    def modid(self, _modid):
        self._modid = _modid

    @property
    def length(self):
        """Return length of the message"""
        return self._length


    def format(self, buf, size):
        """A generic LTE message header format"""
        hdrformat = self.proto.epf_head
        hdrformat.restype = ct.c_int
        hdrformat.argtypes = [ct.c_char_p, ct.c_uint, ct.c_uint,
                              _EnbIdT, _CellIdT, _ModIdT,
                              ct.c_uint16]
        #defalt value for messagetype?
        return hdrformat(buf, size, EP_TYPE_SCHEDULE_MSG,
                         self._enbid, self._pci, self._modid, 1)


    def parse(self, buf, size):
        """A generic LTE message header parse"""
        hdrparse = self.proto.epp_head
        hdrparse.restype = ct.c_int
        hdrparse.argtypes = [ct.c_char_p, ct.c_uint, ct.POINTER(ct.c_uint),
                             ct.POINTER(_EnbIdT), ct.POINTER(_CellIdT), ct.POINTER(_ModIdT),
                             ct.POINTER(ct.c_uint16)]
        return hdrparse(buf, size, ct.pointer(ct.c_uint(EP_TYPE_SCHEDULE_MSG)),
                        ct.pointer(_EnbIdT(self._enbid)), ct.pointer(_CellIdT(self._pci)),
                        ct.pointer(_ModIdT(self._modid)), ct.pointer(ct.c_uint16(1)))



    def parseseqno(self, buf, size):
        """Extracts the sequence number of the message"""
        msgseq = self.proto.epp_seq
        msgseq.restype = ct.c_uint32
        msgseq.argtypes = [ct.c_char_p, ct.c_uint]
        return msgseq(buf, size)


    def parselength(self, buf, size):
        """Extracts the sequence number of the message"""
        msgseq = self.proto.epp_msg_length
        msgseq.restype = ct.c_uint16
        msgseq.argtypes = [ct.c_char_p, ct.c_uint]
        return msgseq(buf, size)
