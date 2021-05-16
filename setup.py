from setuptools import setup
from Cython.Build import cythonize


setup(
    ext_modules=cythonize("round2/round2.pyx"),
    zip_safe=False,
)
