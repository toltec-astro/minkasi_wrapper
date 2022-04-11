# Licensed under a 3-clause BSD style license - see LICENSE.rst

from collections import defaultdict

import subprocess
from distutils.core import Extension

from extension_helpers import get_compiler
from extension_helpers import add_openmp_flags_if_available
from pathlib import Path


minkasi_dir = Path(__file__).parent.joinpath('minkasi')


def pkgconfig(package, kw):
    flag_map = {'-I': 'include_dirs', '-L': 'library_dirs', '-l': 'libraries'}
    output = subprocess.getoutput(
        'pkg-config --cflags --libs {}'.format(package))
    for token in output.strip().split():
        kw.setdefault(flag_map.get(token[:2]), []).append(token[2:])
    return kw


def get_extensions():

    cfg = defaultdict(list)

    files = [
        'minkasi.c',
        'mkfftw.c'
        ]
    cfg['sources'].extend(
            minkasi_dir.joinpath(x).as_posix() for x in files)

    # external dependencies
    cfg['libraries'].append('m')

    # add fftw3 config
    cfg = pkgconfig('fftw3', cfg)
    # this only added the non-threaded libs, and we also need the threaded
    # ones
    cfg['libraries'].extend(['fftw3_threads', 'fftw3f', 'fftw3f_threads'])

    if get_compiler() in ('unix', 'mingw32'):
        cfg['extra_compile_args'].extend([
            '-pedantic',
            '-Wno-newline-eof',
            '-Wno-unused-const-variable',
            ])

    extension = Extension('minkasi_wrapper.extern._minkasi', **cfg)
    add_openmp_flags_if_available(extension)
    return [extension, ]
