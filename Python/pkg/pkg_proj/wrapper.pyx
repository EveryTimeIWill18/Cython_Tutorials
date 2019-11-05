# wrapper.pyx

cimport extwrap

def calc(double x):
  return extwrap.f(x)
