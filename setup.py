#Obtain the necessary Cython Libraries
from setuptools import setup
from distutils.extension import Extension
from Cython.Build import cythonize

#Inform Cython the filename, source code file, and language to be used
ext_modules = [
    Extension("CythonApplication",sources = ['CythonApplication.pyx','functions.cpp'],language="c++")
]

#Inform Cython where to find the application
setup(
    name ='CythonApplication',
    ext_modules = cythonize(ext_modules)
)

#To build the necessary C library for the main application use the commandline option: python setup.py build_ext --inplace

#This code outputs after building the main
if __name__ == "__main__":
    print("Build Completed")