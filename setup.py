from distutils.core import setup
from Cython.Build import cythonize
from pathlib import Path

setup(
    name="round2",
    ext_modules=cythonize(
        [
            str(Path(__file__).parent / "round2" / "round2.pyx"),
        ]
    ),
    zip_safe=False,
)
