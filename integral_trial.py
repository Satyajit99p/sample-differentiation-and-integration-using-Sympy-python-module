from sympy import*

x=Symbol('x')


def tangent():
          p = int(input('enter the coefficient:'))
          return(integrate((p*tan(x)),x))
def cotangent():
          p = int(input('enter the coefficient:'))
          return(integrate((p*cot(x)),x))
def cosine():
          p = int(input('enter the coefficient:'))
          return(integrate((p*cos(x)),x))
def sine():
          p = int(input('enter the coefficient:'))
          return(integrate((p*sin(x)),x))
def cosecant():
          p = int(input('enter the coefficient:'))
          return(integrate((p*csc(x)),x))
def secant():
          p = int(input('enter the coefficient:'))
          return(integrate((p*sec(x)),x))
def exponent():
    q=int(input('eter the coeffciient:'))
    return(integrate((q*exp(x)),x))

def linear_function():
      print('welcome to linear function integration')
      a = int(input('enter coefficient of degree 2:'))
      b = int(input('enter constant:'))

      return (integrate((a * x + b),x))

def quadractic_function():
      print('welcome to quadractic function integration')
      a = int(input('enter coefficient of degree 2:'))
      b = int(input('enter coefficient of degree 1:'))
      c = int(input('enter constant:'))

      return (integrate((a * x ** 2 + b * x + c),x))

def cubic_function():
      print('welcome to cubic equation integration')
      a = int(input('enter the coefficient of degree 3:'))
      b = int(input('enter the coefficient of degree 2:'))
      c = int(input('enter the coefficient of degree 1:'))
      d = int(input('enter the constant:'))

      return (integrate((a * x ** 3 + b * x ** 2 + c * x + d),x))

def quartic_function():
      print('welcome to cubic equation integration')
      a = int(input('enter the coefficient of degree 4:'))
      b = int(input('enter the coefficient of degree 3:'))
      c = int(input('enter the coefficient of degree 2:'))
      d = int(input('enter the coefficient of degree 1:'))
      e = int(input('enter the constant:'))

      return (integrate((a * x ** 4 + b * x ** 3 + c * x ** 2 + d * x + e),x))
def logarithm():
      r=int(input('enter the coefficient:'))
      return(integrate(r*log(x),x))


def arctangent():
          s = int(input('enter the coefficent:'))
          return(integrate(s*atan(x),x))
def arccotangent():
          s = int(input('enter the coefficent:'))
          return(integrate(s*acot(x),x))
def arccosine():
          s = int(input('enter the coefficent:'))
          return(integrate(s*acos(x),x))
def arcsine():
          s = int(input('enter the coefficent:'))
          return(integrate(s*asin(x),x))
def arccosecant():
          s = int(input('enter the coefficent:'))
          return(integrate(s*acsc(x),x))
def arcsecant():
          s = int(input('enter the coefficent:'))
          return(integrate(s*asec(x),x))











