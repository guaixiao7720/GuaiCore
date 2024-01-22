from setuptools import Extension, setup
from Cython.Build import cythonize

# extensions = [Extension("*", ["*.pyx"],
#                 libraries=["textinput"],
#                 library_dirs=["textinput/"]),
#               ]

setup(
    name="textinput",
    packages=['textinput'],
    zip_safe=False,

    ext_modules = cythonize("textinput/*.pyx")
)