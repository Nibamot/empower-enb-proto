#!/usr/bin/env python3


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

class _HelloReply(ct.Structure):
    _pack_ = 1
    _fields_ = [('id', ct.c_uint32)]

class _HelloRequest(ct.Structure):
    _pack_ = 1
    _fields_ = [('id', ct.c_uint32)]

class _EnbIdT(ct.c_uint64):
    pass

class _CellIdT(ct.c_uint16):
    pass

class _ModIdT(ct.c_uint32):
    pass
