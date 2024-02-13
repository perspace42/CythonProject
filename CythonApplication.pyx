#Find C++ Function
cdef extern from "functions.h":
    bint validateNumber(float tip) #Note, this must be defined as returning a bint, instead of a bool

#Place in Wrapper Python Function
def pyValidateNumber(float tip):
    return validateNumber(tip) 