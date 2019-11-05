# cy_script.pyx


cpdef int cy_sum(int n):
  cdef int sum = 0
  cdef int i
  for i in range(n+1):
    sum += i
  return sum
