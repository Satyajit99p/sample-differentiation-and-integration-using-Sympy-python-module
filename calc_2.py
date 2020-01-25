from integral_trial import*
print('enter 1 to choose linear function')
print('enter 2 to choose quadractic function')
print('enter 3 to choose cubic function')
print('enter 4 to choose quartic function')
print('enter 5 to choose trigonometric function')
print('enter 6 to choose exponential function')
print('enter 7 to choose logarithmic function')
print('enter 8 to choose inverse function')
print('enter 9 to choose compound equation')
a=int(input('enter your choice:'))
if(a==1):
    print(linear_function())
if(a==2):
    print(quadractic_function())
if(a==3):
    print(cubic_function())
if(a==4):
    print(quartic_function())
if(a==5):
    print('enter 1 to choose sine function')
    print('enter 2 to choose cosine function')
    print('enter 3 to choose secant function')
    print('enter 4 to choose cosecant function')
    print('enter 5 to choose tangent function')
    print('enter 6 to choose cotangent function')
    p=int(input('enter your choice:'))
    if(p==1):
        print(sine())
    if (p == 2):
        print(cosine())
    if (p == 3):
        print(cosecant())
    if (p == 4):
        print(secant())
    if (p == 5):
        print(tangent())
    if (p == 6):
        print(cotangent())

if(a==6):
    print(exponent())
if(a==7):
    print(logarithm())
if(a==8):
    print('enter 1 to choose arcsine function')
    print('enter 2 to choose arccosine function')
    print('enter 3 to choose arcsecant function')
    print('enter 4 to choose arccosecant function')
    print('enter 5 to choose arctangent function')
    print('enter 6 to choose arccotangent function')
    q = int(input('enter your choice:'))
    if (q == 1):
        print(arcsine())
    if (q == 2):
        print(arccosine())
    if (q == 3):
        print(arccosecant())
    if (q == 4):
        print(arcsecant())
    if (q == 5):
        print(arctangent())
    if (q == 6):
        print(arccotangent())
if(a==9):
    s=0
    while true:
        print('enter 1 to choose linear function')
        print('enter 2 to choose quadractic function')
        print('enter 3 to choose cubic function')
        print('enter 4 to choose quartic function')
        print('enter 5 to choose sine function')
        print('enter 6 to choose cosine function')
        print('enter 7 to choose secant function')
        print('enter 8 to choose cosecant function')
        print('enter 9 to choose tangent function')
        print('enter 10 to choose cotangent function')
        print('enter 11 to choose arcsine function')
        print('enter 12 to choose arccosine function')
        print('enter 13 to choose arcsecant function')
        print('enter 14 to choose arccosecant function')
        print('enter 15 to choose arctangent function')
        print('enter 16 to choose arccotangent function')
        print('enter 17 to choose exponential function')
        print('enter 18 to choose logarithmic function')
        print("enter 0 to terminate")
        b=int(input('enter the choice'))

        if(b==1):
            s=s+linear_function()
        elif(b==2):
            s=s+quadractic_function()
        elif(b==3):
            s=s+cubic_function()
        elif (b == 4):
            s = s + quartic_function()
        elif (b == 5):
            s = s + sine()
        elif (b == 6):
            s = s + cosine()
        elif (b == 7):
            s = s + secant()
        elif (b == 8):
            s = s + cosecant()
        elif (b == 9):
            s = s + tangent()
        elif (b == 10):
            s = s + cotangent()
        elif (b == 11):
            s = s + arcsine()
        elif (b == 12):
            s = s + arccosine()
        elif (b == 13):
            s = s + arcsecant()
        elif (b == 14):
            s = s + arccosecant()
        elif (b == 15):
            s = s + arctangent()
        elif(b==16):
            s=s+arccotangent()
        elif(b==17):
            s=s+exponent()
        elif(b==18):
            s=s+logarithm()
        else:
            break

    print(s)
