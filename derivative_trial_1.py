from sympy import*
x = Symbol('x')

def linear_function():

    print('welcome to linear function differentiation')
    a=int (input('enter coefficient of degree 2:'))
    b=int(input('enter constatnt:'))

    return(diff(a*x+b))

def quadractic_function():

        print('welcome to quadractic function differentiation')
        a = int(input('enter coefficient of degree 2:'))
        b = int(input('enter coefficient of degree 1:'))
        c = int(input('enter constant:'))

        return(diff(a * x ** 2 + b * x + c))

def cubic_function():

    print('welcome to cubic equation differentiation')
    a=int(input('enter the coefficient of degree 3:'))
    b=int(input('enter the coefficient of degree 2:'))
    c=int(input('enter the coefficient of degree 1:'))
    d=int(input('enter the constant:'))

    return(diff(a*x**3+b*x**2+c*x+d))

def quartic_function():
    print('welcome to cubic equation differentiation')
    a = int(input('enter the coefficient of degree 4:'))
    b = int(input('enter the coefficient of degree 3:'))
    c = int(input('enter the coefficient of degree 2:'))
    d = int(input('enter the coefficient of degree 1:'))
    e = int(input('enter the constant:'))

    return(diff(a*x**4+b*x**3+c*x**2+d*x+e))

