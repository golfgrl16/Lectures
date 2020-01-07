"""
For this assignment you should NOT use any additional external library functions.

Of course your function must NOT use the actual sin function from any package
it should only use elementary operations like addition subtraction, multp, division
(although as complex as need for those).

You may also use math.pow for taking powers of floating point numbers. 

The Challenge is to write a function which approximates the sin function accurate at
least until the fourth decimal point. Your function will be evaluated by drawing random numbers 
in the range -2/5 < x < 2/5. 



"""

import math
import random
import numpy as np
import pylab as plt
import sys

def factorial(n):
    """
    I think you will need to write a factorial function as well, this can be used in the sin_approx
    function
    """
    

def sin_approx(x):
    """
    Define your function here. I have just put a placeholder here. 
    """
    y=[]
    for n in np.arange(0.0,10.0):
        term=np.power(-1.0,n)*np.power(x,2*n+1.0)/math.gamma(2*n+1.0)
        y.append(term)

    print(x, np.sin(x))
    print(y)
    print(np.sum(y))

    sys.exit(0)
    return(y)




def grade(plot=True):
    """
    Don't mess with this function. This will grade your input. You need to produce a close approximation
    for  random numbers drawn from -0.2 <= x <= 0.2. 
    """
    
    xIn=[random.uniform(-0.2,0.2) for i in range(0,100)]
    yApprox=list(map(sin_approx, xIn))
    yExact=list(map(math.sin, xIn))
    num_correct=sum(np.isclose(yApprox, yExact, atol=1e-2, rtol=1e-16))
    print("Number correct: ", num_correct)

    print(list(zip(yExact, yApprox)))

    if (plot):
        plt.scatter(xIn, yApprox)
        plt.plot(np.linspace(-0.2,0.2,100), np.sin(np.linspace(-0.2,0.2,100)))
        plt.show()
        

if __name__=="__main__":
    grade()
