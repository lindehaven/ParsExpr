# PARSEXPR

## polynom(expr)

    Parses a string containing a polynom (or an equation) with one unknown
    variable and returns a function for the polynom. The function can be called
    with one argument for the unknown variable.

    Example:
        p = polynom('x^2+3x=(2x+1)^2')
        print(p(-0.5))
        print(p)

## derive(poly)

    Derives a function representing a polynom with one unknown variable and
    returns a function for the derivative. The function can be called with one
    argument for the unknown variable.

    Example:
        d = derive(polynom('x^2+3x=(2x+1)^2'))
        print(d(-0.5))

