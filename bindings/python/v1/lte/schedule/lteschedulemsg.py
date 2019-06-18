#!/usr/bin/env python3
"""Base class for a generic LTE Empower schedule Message"""
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
from v1.lte.schedule import ActionType
from v1.lte.schedule import OperationType
from v1.lte.ltemsg import LTEMsg


class LTEScheduleMsg(LTEMsg):
    """Scheduled event message for communication
    with the controller"""
    def __init__(self):
        super().__init__()
        self.proto = ct.CDLL("libemproto.so")
        self._type = 2
        self._version = 1
        self._enbid = 1
        self._pci = 0
        self._modid = 0
        self._length = 0
        self._action = 0
        self._direction = 0
        self._oper = 0
        self._interval = 0
        self._sequence = 0

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




    @property
    def interval(self):
        """Return interval of the schedule message"""
        return self._interval

    @interval.setter
    def interval(self, interval):
        self._interval = interval


    def format(self, buf, size):
        """Format a schedule event message"""
        schedmsgformat = self.proto.epf_schedule
        schedmsgformat.restype = ct.c_int
        schedmsgformat.argtypes = [ct.c_char_p, ct.c_uint,
                                   ct.c_uint, ct.c_uint,
                                   ct.c_uint32]

        return schedmsgformat(buf, size, ActionType.EP_ACT_HELLO,
                              OperationType.EP_OPERATION_UNSPECIFIED,
                              self._interval)

    def parseinterval(self, buf, size):
        """Extracts interval from LTE Empower Scheduled message"""
        intervalparse = self.proto.epp_sched_interval
        intervalparse.restype = ct.c_uint32
        intervalparse.argtypes = [ct.c_char_p, ct.c_uint]

        return intervalparse(buf, size)


    def parseacttype(self, buf, size):
        """Extracts schedule type from LTE Empower Scheduled message"""
        typeparse = self.proto.epp_schedule_type
        typeparse.restype = ActionType
        typeparse.argtypes = [ct.c_char_p, ct.c_uint]

        return typeparse(buf, size)
