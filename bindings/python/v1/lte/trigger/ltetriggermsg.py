#!/usr/bin/env python3
"""Base class for a generic LTE Empower trigger event Message"""
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
from v1.lte.trigger import ActionType
from v1.lte.trigger import OperationType

class LTETriggerMsg(LTEMsg):
    def __init__(self):
        super().__init__()
        self.proto = ct.CDLL("libemproto.so")
        self._type = 3
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
        """Return action of the trigger message"""
        return self._action


    @property
    def direction(self):
        """Return direction of the trigger message"""
        return self._direction


    @property
    def oper(self):
        """Return operation of the trigger message"""
        return self._oper


    def format(self, buf, size):
        """A generic trigger event message format"""
        trigformat = self.proto.epf_trigger
        trigformat.restype = ct.c_int
        trigformat.argtypes = [ct.c_char_p, ct.c_uint, ct.c_uint,
                               ct.c_uint16]
        #defalt value for messagetype?
        return trigformat(buf, size, ActionType.EP_ACT_UE_REPORT, OperationType.EP_OPERATION_UNSPECIFIED)

    def parseacttype(self, buf, size):
        """Extracts trigger action type from LTE Empower trigger message"""
        typeparse = self.proto.epp_trigger_type
        typeparse.restype = ActionType
        typeparse.argtypes = [ct.c_char_p, ct.c_uint]

        return typeparse(buf, size)

    def parseoptype(self, buf, size):
        """Extracts trigger operation type from LTE Empower trigger message"""
        opparse = self.proto.epp_trigger_op
        opparse.restype = OperationType
        opparse.argtypes = [ct.c_char_p, ct.c_uint]

        return opparse(buf, size)
