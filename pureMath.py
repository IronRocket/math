import math,time

PI = 3.1415926535897932384626433832795028841971693993751


def timer_func(func): 
    def wrap_func(*args, **kwargs):
        timer = False
        for key,value in kwargs.items():
            if key == 'timer' and value == True:
                del kwargs[key]
                timer = True
                break
        t1 = time.perf_counter()
        result = func(*args, **kwargs) 
        t2 = time.perf_counter()  

        if timer:
            return result,t2-t1
        return result
    return wrap_func 


def myFactorial(n):
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial*i
    return factorial

def mySin(x:float,accuracy:int=100)->float:
    '''
    return Σₙ₌₀= ( ((-1)^n)/(2n+1)! )*x^(2n+1)
    '''
    approx = 0
    for i in range(accuracy):
        coef = x**(2*i+1)
        numerator = (-1)**i
        denominator = myFactorial(2*i+1)
        approx += coef*(numerator/denominator)
    return approx

def myCos(x:float,accuracy:int=100)->float:
    '''
    return Σₙ₌₀= ( ((-1)^n)/(2n)! )*x^(2n)
    '''
    approx = 0
    for i in range(accuracy):
        coef = x**(2*i)
        numerator = (-1)**i
        denominator = myFactorial(2*i)
        approx += coef*(numerator/denominator)
    return approx

def myTan(x:float,accuracy:int=100)->float:
    '''
    tan(x) = sin(x)/cos(x)
    return tan(x)
    '''
    return mySin(x,accuracy=accuracy)/myCos(x,accuracy=accuracy)

def myArcSin(x:float,accuracy:int=100)->float:
    '''
    return Σₙ₌₀ = ( (2n)!/ 4^n * ((n)!^2) * (2n+1) )*x^(2n)
    '''
    approx = 0
    for i in range(accuracy):
        coef = x**(2*i+1)
        numerator = myFactorial(2*i)
        denominator = (4**i)*(myFactorial(i)**2)*(2*i+1)
        approx += coef*(numerator/denominator)
    return approx

def myArcCos(x:float,accuracy:int=100)->float:
    '''
    return (π/2) - Σₙ₌₀ = ( (2n)!/ 4^n * ((n)!^2) * (2n+1) )*x^(2n)
    '''
    approx = 0
    for i in range(accuracy):
        coef = x**(2*i+1)
        nnumerator = myFactorial(2*i)
        denominator = 4**i*(myFactorial(i)**2)*(2*i+1)
        approx += coef*(nnumerator/denominator)
    return (PI/2)-approx

def myArcTan(x:float,accuracy:int=100)->float:
    '''
    return Σₙ₌₀ = ( (-1)^i/ 2n+1 )*x^(2n+1)
    '''
    approx = 0
    for i in range(accuracy):
        coef = x**(2*i+1)
        numerator = (-1)**i
        denominator = 2*i+1
        approx += coef*(numerator/denominator)
    return

def arithmeticSeries(step,term):
    return ((term/2)*(2*step+(term-1)*(step)))

x= 0.5

print(math.sin(x),mySin(x))
