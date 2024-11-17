from sympy import *
from sympy.parsing.sympy_parser import parse_expr

def derOperation(input='', constant=''):
    if not input:
        return "No input"
    if not constant:
        return "No constant"
    # Symbol('x','y', 'z')
    func = ''
    try:
        func = parse_expr(input+"+y**3+"+constant)
        err = false
    except TypeError:
        err = true
    
    # replace secures double backslash \
    return (latex(func).replace('\\', '\\\\'), err)