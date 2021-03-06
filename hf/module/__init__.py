# -*- coding: utf-8 -*-
#
# Copyright 2012 Institut für Experimentelle Kernphysik - Karlsruher Institut für Technologie
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""
The very core of HappyFace are modules doing the actual work.
All of them derive from :class:`ModuleBase`, and any other

.. data:: config

    A config parser instance with the aggregated data
    from all module configuration files. It is created and populated
    at initialization by :func:`hf.configtools.readConfigurationAndEnv`.
    
    Since this module variable is used by most category related methods,
    it is important to initialize it early.

"""
from module import getColumnFileReference, moduleClassLoaded, \
    importModuleClasses, getModuleClass
from ModuleBase import ModuleBase
from ModuleProxy import ModuleProxy
import database

config = None

__all__ = ["ModuleBase", "ModuleProxy", "database", "config",
    "getColumnFileReference", "moduleClassLoaded",
    "importModuleClasses", "getModuleClass"]

