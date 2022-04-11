A Wrapper for the Minkasi Map Maker.
------------------------------------

.. image:: http://img.shields.io/badge/powered%20by-AstroPy-orange.svg?style=flat
    :target: http://www.astropy.org
    :alt: Powered by Astropy Badge


This package wraps the Minkasi map mapker as an external map maker package
for the TolTEC camera.


Minkasi Map Maker
-----------------
Minkasi is a Python/C-based mapper for Mustang.

TODO: add credit and license of Minkasi.


Installation
------------

Minkasi depends on fftw3, and requires an OpenMP-capable C compiler to work.

On macOS, this can be done with Homebrew:

.. code:: text

   $ brew install llvm libomp fftw3
   $ export CC=/usr/local/opt/bin/clang
   $ export LDFLAGS=-L/usr/local/opt/llvm/lib
   $ export CPPFLAGS=-I/usr/local/opt/llvm/include

On Ubuntu, do:

.. code:: text

    TODO: add Ubuntu instruction.


Finally, install minkasi_wrapper with

.. code:: text

    $ pip install git+https://github.com/toltec-astro/minkasi_wrapper


License
-------

This project is Copyright (c) Zhiyuan Ma and licensed under
the terms of the BSD 3-Clause license. This package is based upon
the `Astropy package template <https://github.com/astropy/package-template>`_
which is licensed under the BSD 3-clause license. See the licenses folder for
more information.
