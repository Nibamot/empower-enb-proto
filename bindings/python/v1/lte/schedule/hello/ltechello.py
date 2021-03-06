#!/usr/bin/env python3
"""Base class for a generic LTE Empower schedule Hello Message"""
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
from v1.lte.schedule.lteschedulemsg import LTEScheduleMsg

class LTECHello(LTEScheduleMsg):
    """Class that deals with a scheduled hello message"""
    def __init__(self):
        super().__init__()
        self.proto = ct.CDLL("libemproto.so")
        self._action = ActionType.EP_ACT_HELLO
        self._id = 1
