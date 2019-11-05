# setup.py
from setuptools import setup, Extension
from Cython.Build import cythonize

ext1 = Extension('pkg_proj.wrapper', sources=[
            'pkg_proj/wrapper.pyx',
            'pkg_proj/extlib/external.c'
        ])

ext2 = Extension('pkg_proj.cymod.utils', sources=[
    'pkg_proj/cymod/utils.pyx'])


setup(
    name="MyPackage",
    ext_modules=cythonize([ext1, ext2]),
)
