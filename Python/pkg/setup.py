# setup.py
from setuptools import setup
from Cython.Build import cythonize

setup(
    name="MyPackage",
    ext_modules=cythonize([
        'pkg_proj/wrapper.pyx',
        'pkg_proj/cymod/utils.pyx'
    ]),
)
