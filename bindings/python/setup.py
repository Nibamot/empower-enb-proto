#!/usr/bin/env python3
#
# Copyright (c) 2018 FBK-CreateNet
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

"""Setup script."""

from distutils.core import setup

setup(name="empower-enb-proto",
      version="1.0",
      description="EmPOWER protocols",
      author="Abin Ninan Thomas",
      author_email="",
      url="https://github.com/5g-empower/empower-enb-agent",
      long_description="EmPOWER Protocols wrapper for LTE base stations",
      packages=['v1', 'v1.lte', 'v1.lte.schedule', 'v1.lte.schedule.hello',
                'v1.lte.schedule.cellmeas', 'v1.lte.single', 'v1.lte.single.enbcap',
                'v1.lte.trigger', 'v1.lte.single.cellcap', 'v1.lte.single.ran',
                'v1.lte.trigger.uerep', 'v1.lte.trigger.uemeas'])
