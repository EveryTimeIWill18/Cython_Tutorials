# wrapper.pyx
# distutils: sources = "pkg_proj/extlib/external.c"
cimport extwrap

def calc(double x):
  return extwrap.f(x)
