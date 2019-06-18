#!/usr/bin/env python3
"""Empower-Parser"""

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
from v1 import MessageType
from v1 import ActionType
from v1.lte.ltemsg import LTEMsg

class EmpowerParser:
    """Wrapper around direct python bindings"""

    """@staticmethod
    def parseversion(buf, size):
        #function to parse any message to be parsed by
        #LTEMsg or its child classes
        _proto = ct.CDLL("libemproto.so")
        parseversion = _proto.epp_ve
        return ltemsg.parse(buf, size)"""



    @staticmethod
    def parseevent(buf, size):
        """function to parse any message to be parsed by
        LTEMsg or its child classes"""
        _proto = ct.CDLL("libemproto.so")
        parseevent = _proto.epp_msg_type
        parseevent.restype = MessageType
        parseevent.argtypes = [ct.c_char_p, ct.c_uint]
        return parseevent(buf, size)


    @staticmethod
    def parseaction(buf, size):
        """function to parse any message to be parsed by
        LTEMsg or its child classes"""
        _proto = ct.CDLL("libemproto.so")
        parseaction = _proto.epp_msg_type #generic action type?
        parseaction.restype = ActionType
        parseaction.argtypes = [ct.c_char_p, ct.c_uint]
        return parseaction(buf, size)

    @staticmethod
    def parsedirection(buf, size):
        """function to parse any message to be parsed by
        LTEMsg or its child classes"""
        _proto = ct.CDLL("libemproto.so")
        parsedirection = _proto.epp_dir
        parsedirection.restype = ct.c_uint
        parsedirection.argtypes = [ct.c_char_p, ct.c_uint]
        return parsedirection(buf, size)
