# extwrap.pxd
# Path is relative to the pxd files

cdef extern from "extlib/external.h":
  double f(double x)
