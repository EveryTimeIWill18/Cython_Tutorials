from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize([
    'ml_project/cy_script.pyx',
    'tools/kittens.pyx',
    'tools/kittens.pxd',
    'tools/utils/puppies.pyx',
    'tools/utils/puppies.pxd'
]))
