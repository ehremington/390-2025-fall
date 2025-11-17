#!/usr/bin/env python

# this is my file where i am putting things that i use all the time in here

import numpy as np
import pandas as pd

def factorial(x):
    f = 1
    if x<0:
        print('undefined')
    else:
        for i in range(1,x+1):
            f = f*i

        return(f)

def binomial(n,k):
    if k>n:
        print('Learn more about Pascals Triangle')
    else:
        return(factorial(n)/factorial(k)/factorial(n-k))

def trap0(func, a, b, steps):
    dx = (b-a)/steps
    x = np.linspace(a, b, steps+1)
    y = func(x)
    s = dx/2*(func(a)+func(b))
    s = s + np.sum(y[1:steps]*dx)
    return(s)

def trap(x_data, y_data):
    if type(x_data)==pd.core.series.Series:
        x_data = np.asarray(x_data)
        y_data = np.asarray(y_data)
    dx = (x_data[-1]-x_data[0])/len(x_data)
    s = dx/2*(y_data[0]+y_data[-1])
    s = s + np.sum(y_data[1:-2]*dx)
    return(s)

def simp(func, a, b, steps):
    if steps%2!=0:
        steps = steps + 1
        print('i added one step')
    dx = (b-a)/steps
    x = np.linspace(a, b, steps+1)
    y = func(x)
    s = dx/3*(func(a)+func(b))
    s = s + dx/3*(4*np.sum(y[1:steps:2]) + 2*np.sum(y[2:steps-1:2]))
    return(s)


def integrate(x, y):
    '''simpson's rule for integration with simpson’s 3/8 rule adjustment for even-length data'''

    if isinstance(x, pd.Series):
        x = x.to_numpy()
        y = y.to_numpy()

    steps = len(y)

    h = (x[-1] - x[0]) / (steps - 1)  # step size (ensuring correct intervals)

    if steps % 2 == 1:  # odd number of points -> use standard Simpson's 1/3 rule
        s = (h / 3) * (y[0] + y[-1] + 4 * np.sum(y[1:steps-1:2]) + 2 * np.sum(y[2:steps-2:2]))

    else:  # even number of points -> use Simpson’s 1/3 rule for first n-3 and 3/8 rule for last three
        s_simpson = (h / 3) * (y[0] + y[-3] + 4 * np.sum(y[1:steps-3:2]) + 2 * np.sum(y[2:steps-4:2]))
        s_three_eighth = (3 * h / 8) * (y[-3] + 3 * y[-2] + 3 * y[-1] + y[-1])  # last 3 points
        s = s_simpson + s_three_eighth

    return s

def GaussLagQuad8(function):
    x=np.asarray([1.7027963230510100e-1, 9.0370177679937991e-1,\
       2.2510866298661307,    4.2667001702876588,\
       7.0459054023934657,    1.0758516010180995e+1,\
       1.5740678641278005e+1, 2.2863131736889264e+1])
    w=np.asarray([3.6918858934163753e-1, 4.1878678081434296e-1,\
       1.7579498663717181e-1, 3.3343492261215652e-2,\
       2.7945362352256725e-3, 9.0765087733582131e-5,\
       8.4857467162725315e-7, 1.0480011748715104e-9])
    integral = np.sum(w*function(x))
    return(integral)

def gaussHermQuad8(function):
    x = np.asarray([-0.38118699,-1.157193712,-1.981656757,-2.93063742,0.38118699,1.157193712,1.981656757,2.93063742])
    w = np.asarray([0.661147013,0.207802326,0.017077983,0.000199604,0.661147013,0.207802326,0.017077983,.000199604])
    integral = np.sum(w*function(x))
    return(integral)

def gaussLegQuad8(function):
    x = np.asarray([0.183434643,0.52553241,0.796666477,0.960289857])
    # x = np.asarray([-0.183434643,-0.52553241,-0.796666477,-0.960289857,0.183434643,0.52553241,0.796666477,0.960289857])
    w = np.asarray([0.362683783,0.313706646,0.222381035,0.101228536])
    # w = np.asarray([0.362683783,0.313706646,0.222381035,0.101228536,0.362683783,0.313706646,0.222381035,0.101228536])
    integral = np.sum(w*function(x))
    return(integral)

######################################################################
#
# Functions to calculate integration points and weights for Gaussian
# quadrature
#
# x,w = gaussxw(N) returns integration points x and integration
#           weights w such that sum_i w[i]*f(x[i]) is the Nth-order
#           Gaussian approximation to the integral int_{-1}^1 f(x) dx
# x,w = gaussxwab(N,a,b) returns integration points and weights
#           mapped to the interval [a,b], so that sum_i w[i]*f(x[i])
#           is the Nth-order Gaussian approximation to the integral
#           int_a^b f(x) dx
#
# This code finds the zeros of the nth Legendre polynomial using
# Newton's method, starting from the approximation given in Abramowitz
# and Stegun 22.16.6.  The Legendre polynomial itself is evaluated
# using the recurrence relation given in Abramowitz and Stegun
# 22.7.10.  The function has been checked against other sources for
# values of N up to 1000.  It is compatible with version 2 and version
# 3 of Python.
#
# Written by Mark Newman <mejn@umich.edu>, June 4, 2011
# You may use, share, or modify this file freely
#
######################################################################

def gaussxw(N):

    # Initial approximation to roots of the Legendre polynomial
    a = np.linspace(3,4*N-1,N)/(4*N+2)
    x = np.cos(np.pi*a+1/(8*N*N*np.tan(a)))

    # Find roots using Newton's method
    epsilon = 1e-15
    delta = 1.0
    while delta>epsilon:
        p0 = np.ones(N,float)
        p1 = np.copy(x)
        for k in range(1,N):
            p0,p1 = p1,((2*k+1)*x*p1-k*p0)/(k+1)
        dp = (N+1)*(p0-x*p1)/(1-x*x)
        dx = p1/dp
        x -= dx
        delta = max(abs(dx))

    # Calculate the weights
    w = 2*(N+1)*(N+1)/(N*N*(1-x*x)*dp*dp)

    return x,w

def gaussxwab(N,a,b):
    x,w = gaussxw(N)
    return 0.5*(b-a)*x+0.5*(b+a),0.5*(b-a)*w

# For differentiating a function!

def back(function,x_value, stepSize):
    return (function(x_value)-function(x_value-stepSize))/stepSize

def forward(function,x_value, stepSize):
    return (function(x_value+stepSize)-function(x_value))/stepSize

def mid(function,x_value, stepSize):
    return (function(x_value+stepSize)-function(x_value-stepSize))/(2*stepSize)

def doubled(function, x_value, stepSize):
    return (function(x_value+stepSize)-2*function(x_value)+function(x_value-stepSize))/(stepSize**2)

# for differentiating data, just use np.gradient!

    
def bisection(function, lower_guess, upper_guess, tolerance=2**-32):
    midpoint = (lower_guess + upper_guess)/2
    n = 0
    while upper_guess - lower_guess > tolerance:
        if function(lower_guess)*function(midpoint)<0:
            upper_guess = midpoint
            midpoint = (lower_guess + upper_guess)/2
        elif function(midpoint)*function(upper_guess)<0:
            lower_guess = midpoint
            midpoint = (lower_guess + upper_guess)/2
        elif function(lower_guess)*function(midpoint)>0 and function(midpoint)*function(upper_guess)>0:
            print('no unique root in that bracket')
            break
        n = n+1
    return(midpoint, n)

def secant(f, guess, delta=1, tolerance = 2**-32):
    x0 = guess
    x1 = x0 + delta
    n = 0
    while abs(f(x1))>tolerance:
        x2 = x1 - (x1-x0)/(f(x1)-f(x0))*f(x1)
        x0 = x1
        x1 = x2
        n += 1
    return(x1, n)


if __name__ == "__main__":
    print('you didn\'t mean to do this')