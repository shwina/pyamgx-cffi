from _amgx_cffi import ffi, lib


def initialize():
    lib.AMGX_initialize()

def finalize():
    lib.AMGX_finalize()
