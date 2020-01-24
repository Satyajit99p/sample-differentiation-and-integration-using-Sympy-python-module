from derivative_trial_1 import*
print('enter 1 to choose linear function')
print('enter 2 to choose quadractic function')
print('enter 3 to choose cubic function')
print('enter 4 to choose quartic function')
a=int(input('enter your choice:'))
if(a==1):
    print(linear_function())
if(a==2):
    print(quadractic_function())
if(a==3):
    print(cubic_function())
if(a==4):
    print(quartic_function())
