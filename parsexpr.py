'''ParsExpr'''

import sys
import sympy
import numpy

def polynom(expr):
    '''Parses a string containing a polynom (or an equation) with one unknown
    variable and returns a function for the polynom. The function can be called
    with one argument for the unknown variable.

    Example:
        p = polynom('x^2+3x=(2x+1)^2')
        print(p(-0.5))
        print(p)
    '''

    UNKNOWN = 'x'

    def cleanup(expr):
        '''Removes whitespace and uppercase symbols from the expression.'''
        expr = expr.replace(' ', '')
        expr = expr.replace('\t', '')
        expr = expr.lower()
        return expr

    def convert_equ_to_poly(expr):
        '''Converts any equation into a polynom by removing equal sign.'''
        pos = expr.find('=')
        if pos > 0:
            expr = expr[pos+1:] + '-(' + expr[:pos] + ')'
        return expr

    def replace_caret(expr):
        '''Replaces any caret for Python syntax.'''
        return expr.replace('^', '**')

    def add_mul_oper(expr):
        '''Adds multiplication operator for Python syntax.'''
        new_expr = ''
        for i in range(len(expr)):
            if i < len(expr)-1 and expr[i].isnumeric() and \
               (expr[i+1] == '(' or expr[i+1] == UNKNOWN):
                new_expr += expr[i] + '*'
            else:
                new_expr += expr[i]
        return new_expr

    expr = cleanup(expr)
    expr = convert_equ_to_poly(expr)
    expr = replace_caret(expr)
    expr = add_mul_oper(expr)
    x = sympy.Symbol(UNKNOWN)
    try:
        poly = sympy.polys.polytools.poly_from_expr(expr)[0]
        result = numpy.poly1d(poly.coeffs())
    except: #FIXME: Specify exception type(s)
        print(f"Error when parsing '{expr}'!", file = sys.stderr)
        result = None
    return result

def derive(poly):
    '''Derives a function representing a polynom with one unknown variable and
    returns a function for the derivative. The function can be called with one
    argument for the unknown variable.

    Example:
        d = derive(polynom('x^2+3x=(2x+1)^2'))
        print(d(-0.5))
        print(d)
    '''
    try:
        result = numpy.polyder(poly)
    except: #FIXME: Specify exception type(s)
        print(f"Error when deriving '{poly}'!", file = sys.stderr)
        result = None
    return result

if __name__ == '__main__':
    p = polynom('3x + 5 = 3(1/2x - 4)')
    assert p(-34/3) == 0.0
    d = derive(p)
    assert d(-34/3) == -1.5
    p = polynom('3(1/2x-4)-3x-5')
    assert p(-34/3) == 0.0
    d = derive(p)
    assert d(-34/3) == -1.5
    p = polynom('x^2 + 3x = (2x + 1) ^ 2')
    assert p(-0.5) == 1.25
    d = derive(p)
    assert d(-0.5) == -2.0
    p = polynom('3x=(2y+1)^2-x^2')
    assert p is None
    d = derive(p)
    assert d is None
