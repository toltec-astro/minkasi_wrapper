#!/usr/bin/env python

import ctypes
from pathlib import Path


_lib_path = next(iter(Path(__file__).parent.glob("_minkasi*.so")))
_minkasi_c_module = ctypes.cdll.LoadLibrary(_lib_path)


# This the name used by the original minkasi.py to refer to the C module.
# so we leave it this way
mylib = _minkasi_c_module


__all__ = ['mylib']
