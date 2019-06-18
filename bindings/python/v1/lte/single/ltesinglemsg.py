#!/usr/bin/env python3
"""Base class for a generic LTE Empower Single event Message"""
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
from v1.lte.ltemsg import LTEMsg
from v1.lte.single import ActionType
from v1.lte.single import OperationType

class LTESingleMsg(LTEMsg):
    def __init__(self):
        super().__init__()
        self.proto = ct.CDLL("libemproto.so")
        self._type = 1
        self._version = 1
        self._enbid = 1
        self._pci = 0
        self._modid = 0
        self._length = 0
        self._action = 0
        self._direction = 0
        self._oper = 0

    @property
    def action(self):
        """Return action of the schedule message"""
        return self._action


    @property
    def direction(self):
        """Return direction of the schedule message"""
        return self._direction



    @property
    def oper(self):
        """Return operation of the schedule message"""
        return self._oper


    def format(self, buf, size):
        """A generic single event message format"""
        singformat = self.proto.epf_single
        singformat.restype = ct.c_int
        singformat.argtypes = [ct.c_char_p, ct.c_uint, ct.c_uint,
                               ct.c_uint16]
        #defalt value for messagetype?
        return singformat(buf, size, ActionType.EP_ACT_ECAP, OperationType.EP_OPERATION_UNSPECIFIED)

    def parseacttype(self, buf, size):
        """Extracts single action type from LTE Empower Single message"""
        typeparse = self.proto.epp_single_type
        typeparse.restype = ActionType
        typeparse.argtypes = [ct.c_char_p, ct.c_uint]

        return typeparse(buf, size)

    def parseoptype(self, buf, size):
        """Extracts single operation type from LTE Empower Single message"""
        opparse = self.proto.epp_single_op
        opparse.restype = OperationType
        opparse.argtypes = [ct.c_char_p, ct.c_uint]

        return opparse(buf, size)
