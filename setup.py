from setuptools import Extension, setup
from Cython.Build import cythonize

# extensions = [Extension("*", ["*.pyx"],
#                 libraries=["textinput"],
#                 library_dirs=["textinput/"]),
#               ]

setup(
    name="guaicore",
    packages=['guaicore'],
    zip_safe=True,

    ext_modules = cythonize("textinput/*.pyx")
)
