# wrapper.pyx
# distutils: libraries = "external"
# distutils: library_dirs = "pkg/extlib"
cimport extwrap

def calc(double x):
  return extwrap.f(x)
