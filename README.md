# Daily Log


---
# day 36 | 251121 F

We are going to look at the heat equation, also known as the diffusion equation. The method to solve this partial differential equation is known as *Forward-Time Centered-Space* Method, or *FTCS* for short. What this means is actually very simple, we are going to solve for the temperature along a rod as time is ticking by. The amount that the temperature is going to advance is equal to the second derivative of how the temperature is arranged over space. This will continue until the second derivative is zero, which means that the temperature is no longer changing along the rod. The PDE for this is the equation:

$$\frac{\partial^2 T}{\partial x^2} = \frac{d T}{d t} $$

The boundary conditions for this PDE are simply the temperatures that this is being held at the two ends. We know that eventually the temperature will change in a linear fashion along this length (\\(\frac{\partial^2 T}{\partial x^2} = 0\\)), but we are also curious about how this changes over time. So what we will do is code up a method for solving this as time is ticking by and then save a few of these temperature profiles to plot at some interesting times.

I would like for you to solve exercise 9.4. 

---
# day 35 | 251119 W


---
# day 34 | 251117 M


---
# day 33 | 251114 F


---
# day 32 | 251112 W

We began by talking through what a partial differential equation actually is. To understand this, you first need to understand what a partial derivative is:

$$f(x, y, z) = 4 x y^2 z^4 $$ 

$$\frac{\partial f}{\partial x} = 4 y^2 z^4$$

$$\frac{\partial f}{\partial y} = 8 x y z^4 $$

So a partial derivative is a derivative of a function with respect to one single variable, treating the other variables as constants. Not too bad right. Furthermore, second partial derivatives are second derivatives treating the other variables as constants, but this can be a little bit trickier:

$$\frac{\partial^2 f}{\partial x^2} = 0$$

$$\frac{\partial^2 f}{\partial x \partial y} = 8 y z^4$$

Do you see that? I can take a partial derivative with respect to one variable on a function that is already a partial derivative of a different variable. Tricky stuff and you have do be careful. BUT!

We are not solving partial derivatives using analytical techniques, but using **numerical techniques**. Which actually eases the burden quite a bit. However each partial differential equation, will need to be taken one at a time, in order to come up with a method to numerically solve it. Fortunately, most second order partial differential equations in physics take on just a few forms, so we should be able to learn a couple of techniques, and the apply them to many equations.

So first, we will take **Laplace's Equation**, and solve it in 2 dimensions. Laplace's equation looks like this:

$$\nabla^2 V = 0 $$

Now that upside down *delta* character looks bad. But another way to write this equation is like this:

$$\frac{\partial^2 V}{\partial x^2}+\frac{\partial^2 V}{\partial y^2} = 0 $$

So, to solve such an equation we also need **boundary conditions**. These will take the form of what is the potential around the outside of this region? For a square/rectangleish region this might be something like the potential (V) is zero along all of the edges except the top boundary (have a look at p 407). So, in order to solve this, we will use the relaxation technique, where we the solution at any particular point is the average of the solution at all of the points all around it. You may be seeing the circularity of the kind of calculation we are about to do. The value of the potential at any point depends on the value at every other point, which depends on the value at the other points and so on...

So to pull this off, first we are going to use excel to do this. You have to enable a setting that allows recursive calculations. But once you have done this you can run that method over and over (Ctrl+Shift+F9 on my computer/program) and this will eventually give you the answer that you can plot. Plotting this in excel is horrible, so I recommend plotting it in jupyter, and I show you below how to do that.

---
# day 31 | 251110 M

Adding a startup script to `~/.ipython/profile_default/startup` is a very handy way to have common imports handled automatically for lab notebook style managment.

File naming is weird. Mine is `00-myImports.ipy`. For some reason this is necessary I think. See the README in the directory for more info.

Currently my script is the following:

```python
%matplotlib ipympl

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
```

This goes just fine for Mac users, but Windows users need to be careful to turn on showing file extensions. You can do this in File Explorer by clicking on View -> More -> Show file extensions. 

## also our custom library of scripts

For linux users, add the following to `.bashrc` in your home folder. For Mac users, add the same thing to the file `.zshrc`. Note that after `$HOME` your path might be different than mine.

```
# adding ph390 to my PATH but make sure the path is correct
export PYTHONPATH="${PYTHONPATH}:$HOME/Dropbox/390-fall-2025/scripts/"
```

One way that you can check is by doing this in a jupyter lab cell:

```python
import sys
print(sys.path)
```

For Windows users, you need to click Start and type in Environment Variables and select Edit the System Environment Variables. Under user variables add one named PYTHONPATH and give it the value `%USERPROFILE%\Dropbox\390-2025-fall\scripts`. Saving and exiting should do it. Verify by starting jupyter and entering the code above.

to check on things and see whether they are working:

1. just try `np.linspace(1,20)` and see whether that executes without a hiccup.
2. next try `import ph390` and see if that complains. note that this will only work once you have `__inti__.py` and `ph390.py` in that `scripts` folder, even if they are empty. Put a bisection method script in there and see whether you can call it.


---
# day 30 | 251107 F
Projects are due today! Or at least nearly today! I have told some students that if you can make your project 50% better by turning it in on Sunday then that is ok with me. So take that into account. I know many students are happy to have it off their plate and have turned it in already, but if you hit some snags along the way, you may turn it in as late as Sunday.

Now, today we are doing to talk about our differential equations and how to move to higher dimensions. This is a relatively easy change give how we have constructed our solver. With this change we can both solve initial value problems as well as solve boundary value problems. 

--- 
# day 29 | 251105 W

Today we worked on the shooting method. This is a way of solving differential equations by using the **boundary condition** rather than the **initial conditions**. This method is more difficult to do in terms of computational resources, but method is straightforward. We simply try a bunch of times with different initial conditions until we get really close to the other boundary. It is not very smart, but it is effective and it is easy to code up, because we define a function that solves the differential equation and then we plug that into a root finding algorithm to keep evaluating that function until we find the root. That root means that we hit our target. 

We'll start this today with one dimensional motion, which is a little weird to imagine. We have a ball that we are going to toss straight up into the air. How fast will we need to throw it to land on the ground 10 seconds later. This is a little strange because we normally would want to know how long it takes to come back down given we threw it as hard as we could. Another way that you could frame our current question is, "If I time how long it takes to go up and come down, then how fast did I throw it?" This is what we will work through today.

---
# day 28 | 251103 M

Today we worked on our projects in class and I had a chance to see everyone's and give some pointers.

---
# day 27 | 251031 F

This is where I'll record hopefully before class what we will be doing. Please check here and read before class, so you'll have an idea of what we will cover that day. 

We are now ready to handle 2nd order differential equations. The method will be similar to coupled first order equations because that is exactly how we will treat any second order equation: as a set of coupled first order equations like below.

Let's take an example second order equation and look at the technique. We will take a mass on a spring under damped conditions:

$$ ma = -c v - k x$$

The first thing we want to do is put this in terms of all of the derivative:

$$m\frac{d^2 x}{dt^2} = -c\frac{dx}{dt} - k x $$

Then we want to isolate the second derivative. 

$$\frac{d^2 x}{dt^2} = -\frac{c}{m}\frac{dx}{dt} - \frac{k}{m} x $$

Then we want to break this up into two first order differential equations. And this looks a little bit backwards, but we need to realize that we just replaced \$v$ with \$\frac{dx}{dt}$ so what if we went backwards that in terms of the substitution of variables.

$$\frac{d v}{dt} = -\frac{c}{m} v - \frac{k}{m} x $$

and then 

$$ \frac{dx}{dt} = v$$

So now we can run this exactly the same way that we did coupled first order equations, because that is what they are! And we can choose almost any kind of differential equation that we want to. To start off with we may just choose an object falling from some height. The initial height is an important initial value and the fact that we are dropping it is important since the initial velocity will be equal to zero.

$$a = -g\ =>\  \frac{d^2x}{dt^2}\ =>\ \frac{dv}{dt} = -g \quad \mbox{and} \quad \frac{dx}{dt} = v $$

And this same logic can be applied to other sets, so we could cover linear drag:

$$\frac{dv}{dt} = -g - \frac{c}{m} v \quad \mathrm{and} \quad \frac{dx}{dt} = v $$

Or we can do quadratic drag but you do have to be more careful since the signs are more tricky:

$$\frac{dv}{dt} = -g + \frac{c}{m} v^2 \quad \mathrm{and} \quad \frac{dx}{dt} = v$$

For this case you have to watch out for the *SIGNS* of the velocity because they are squared and there is not an easy way to handle them if the object comes to rest and changes direction.

Work on exercise 8.5 after you have reviewed the example 8.6 and exercise 8.4.

---
# day 26 | 251029 W

Today we will review coupled first order differential equations. There are some significant changes we need to make to portions of our code, but at the end of the day these changes will set us up nicely for the next topic (second order differential equations!). The most important different is that we will be plugging in an array in the place of our dependent variables (like x and y), and this change will allow our program to handle the variation of these variables all at once, a rather elegant solution but one that requires you to really follow what is going on. In class, you will likely have time to complete the homework assignment which is exercises 5.2 and 5.3. 

---
# day 25 | 251027 M

Today we will continue in our study of differential equations by looking at exercise 8.1, and extending that a bit. Then we will look at differential equations with more than one variable. More than two variables actually. This will be a very important technique for us because this will lead us into second order differential equations, which is very much what physicists are interested in. This change will be slight, but important and we'll have to be careful about how we handle our variables. For this reason we will start to treat time t as our independent variable, and x and y (and z!) as our dependent variables. 

---
# day 24 | 251024 F

We have worked on Euler's method and have a decent way to do that. But there are other methods that work even better and don't take that much more calculation to do. These methods all go by the name Runge-Kutta. Newton's method is actually 1st order Runge-Kutta. 2nd order Runga-Kutta and 4th order Runga-Kutta are what we are going to talk about today. 


---
# day 23 | 251022 W

Today we will continue to work with Euler's Method for solving differential equations, but this time we will turn to python to solve this problem now that we have some experience with Excel. We will talk about how to handle these first order differential equations that have only one variable on the right hand side, and then we will talk about how to handle them if they have two variables. These look like these two equations:

$$
\begin{align}
\frac{dy}{dx} &= x^2 +x-1  \\\
\frac{dy}{dx} &= y^3 + \sin x
\end{align}
$$

Euler's Method is good, but the error grows over time as we have seen. This is part of every solution to differential equations, but it is something that we want to minimize. Next time, we will discuss some methods that will be better than Euler's method and won't take much longer to work through. 

Take a look at exercise 6.1 from the text book and we'll work on that next time.

---
# day 22 | 251020 M

I discovered a problem with our secant method and have a fix for it below. This is embarrassing but it is important to realize that it can be hard to figure out a bug with code when the code almost works. There was nothing telling me it was broken and the answers it gave were frequently correct, but the problem was deeply buried and finally raised its head the other day (day 20) when we were working on solving a fairly simple equation. So go check the updated notes from day 20 to see what happened, but here is the correct version (I have also corrected it everywhere else that I could find it.)

```python
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
```

We did this in class in excel but then bonked when things weren't working correctly. So here is a correct way to do it for next time. 

We were learning Euler's (pronounced Oilah's) method in class and it is very simple to put into play with Excel to start off with. We will start off with first order differential equations. So for example we came up with this equation:

$$\frac{dy}{dx} = x^2+x-1 \, \mathsf{where} \, y(0) = -1$$

This is easy enough to simply **integrate**, and that is a good thing to know! Very often in DiffEQ (that's what we call Differential Equations) simply integrating, or even guessing and checking is a good way to solve things. What we are doing in Computational Physics is learning a slightly different way to calculate the answer, but even we need something to compare our answer to. So back to it.

Using Euler's method we approximate the next place with the following bit of logic:

$$y_{n+1} = y_{n} + \frac{dy}{dx} \cdot dx $$

So that is exactly the logic we put into Excel. 

| x | y | dydx |
|---|---|---|
| 0 | initial condition | diff eq |
| step | =B2 + C2*(A3-A2) | diff eq |
| ... | ... | ... |

I don't know if that table helps but that is how we do it. And we can check this by plotting the actual solution, since this is a simple enough expression that we can use some simple math to find it. 

$$\int(x^2+x-1)dx = \frac{1}{3}x^3+\frac{1}{2}x^2-x +C$$

and we can find *C* by using our initial condition \\(y(0) = -1$\\). That means \\(C=-1\\). And this works great!

And we could do something like this for every **first order** differential equation. So another one we had in class was this: 

$$\frac{dy}{dx} = x^2 e^{-x} -1  \mathsf{where} \, y(0) = -1$$

and we got a solution for that which I won't even bother to check.

Another one is this one

$$\frac{dy}{dx} = -y $$

Now that one seems a little more difficult because it is not as straightforward to integrate. But it is still a *separable* differential equation, since I can separate the variables to their own sides. Like this:

$$\frac{dy}{y} = -dx $$

Now I can integrate both sides:

$$\int \frac{dy}{y} = -\int dx $$

and that means

$$ \ln(y) = -x + C$$

which further simplifies to 

$$ y = e^{-x + C} = A e^{-x} $$

And **THAT** is the step I bonked on in class today. But we are now able to solve for that constant `A` by doing this:

$$y(0) = -1 = A $$

So that tells us exactly what to do with our "correct" solution. Check out `day22-excel-file.xsls` for the details on how to plug this into excel and what the plots should look like. Below, I have included how to plot these files quickly using `pandas`. This is slightly different to how we have done it in the past but it is good to learn a few differences. Just make sure that the excel file is in the same directory as the jupyter file you are in.

```python
df = pd.read_excel('day22-excel-file.xlsx', sheet_name='Sheet2')

df.plot('x', 'y')
```


---
# day 21 | 251017 F

We are going to make a jump to solving differential equations. We are going to start with the simplest method of solving differential equations, Euler's method, and we are going to do it with excel or google sheets to get a sense of what is going on, then we will learn how to code it up in python. But seeing it in excel is a great way to start off.

Euler's Method is all about predicting the value of the function by knowing the value of the derivative and a time interval that has gone by. 

---
# day 20 | 251015 W

We want to practice using several methods together, and although I messed this up somewhat I'll show you how to do a better problem at the end. But here is the problem at the moment that I would like to solve.

We have the Stephan-Boltzmann Law that says 

$$W = \sigma T^4$$

And what I would like to know is how to solve for T, given that we know a value for W. So we can make W=20, and then apply some method to finding the root of the resulting equation, which is like asking for which value of T is the following function 0.

$$f(T) = \sigma T^4 - 20 => 0$$

So that is the function that we want to put into our secant method or bisection methods or whichever method you want. 

First you should plot it. That will give you some idea of where the zero is. Then use bisection or my favorite secant method to find the temperature T that will make this happen. It is easy enough to check this with algebra, so for our example 

$$T = \sqrt[4]{\frac{20}{\sigma}} = \sqrt[4]{\frac{20}{5.652\times10^{-8}}} = 137.15$$


---
# day 19 | 251010 F

Today, we continue to look into root finding, this time reviewing several techniques. I'll refer to the code at the bottom of this section.

The bisection method is very simple to think through. Take two guesses that are on either side of the root. Find the midpoint between these guesses, and then decide whether that midpoint should be the new upper bound or lower bound. That decision is then repeated over and over until you reach a *desired tolerance*. This method is easy and works well as long as you made decent guesses of upper and lower bound. You should probably graph the function first to determine these, since it can be difficult to do without a good guess.

Another clever way to do this is to use a line that is fit to an initial guess. This is known as Newton's Method, and in order to do this, we need to know the point as well as the derivative at that point. This is easy for many functions that we can write down algebraically but not all functions. But it works very quickly and is easy to understand. 

The final method is a very good one, because we only need to provide one guess and we don't need to use or know the derivative function. We evaluate the function at two different places that are "near" by and then fit a line to that. The method itself works similarly to the Newton's method from there. 

Homework is to do exercise 6.16, specifically part (B). 


```python
def bisection(function, lower_guess, upper_guess, tolerance=2**-32):
    midpoint = (lower_guess + upper_guess)/2
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
    return(midpoint)

def newton(f, df, guess, tolerance = 2**-32):
    x = guess
    n = 0
    while abs(f(x)) > tolerance:
        x = x - f(x)/df(x)
        n += 1
    return(x, n)

def secant(f, guess, delta, tolerance = 2**-32):
    x0 = guess
    x1 = x0 + delta
    n = 0
    while abs(f(x1))>tolerance:
        x1 = x1 - (x1-x0)/(f(x1)-f(x0))*f(x1)
        n += 1
    return(x1, n)
```

---
# day 18 | 251008 W

We began a series on root finding. What we mean by root finding is finding where (as in what x-value) a function is equal to zero. We can use these techniques to find the value of a function when it does not cleanly work out in the data that we have generated. It may in fact be difficult to interrogate a function backward like this. So we can employ several methods which we will look at in the coming days to help investigate this problem. 

The first of these methods is the *relaxation method*. This method involves us making a guess and evaluating a function. So as an example we can use

$$f(x) = x-e^{-x}$$

There is no algebraic way to find a value for x that results in the output of this function being equal to zero. But we can take this equation and rearrange it somewhat:

$$ x = e^{-x} $$

Now we are going to look for values of x that give the same value on both sides of this equation. One very clever hack for this method is to simply set the value and reuse that on the other side of the equation. This is the method at the heart of the relaxation method. I'll make a guess, evaluate \(e^-x)\), then set that value no matter what it is equal to x, and then continue to re-evaluate \(e^-x)\). This will *slowly* creep up to the value that I am looking for. Below is the code that we will use to do this:

```python
x = 2 # initial guess
error = 1 # initial error
count = 0 # counting index to see how many steps
while abs(error)>0.00001:
    x1 = np.exp(-x)
    error = x1 - x
    x = x1
    count = count + 1 
    if count > 100000:
        print('i couldnt find an answer so ignore this')
        break
print(x)
print(count)
```

---
# day 17 | 251006 M

We took a day to work on homework assignments that are long over due. We worked together and debugged some code in class today.

---
# day 16 | 251003 F

We will look at the question of whether decreasing the step size of a derivative always increases the accuracy (spoiler: it doesn't, and its complicated).

We will also look into methods for differentiating DATA, which is similar and easy, but there are some "gotchas" there as well that we need to be aware of.

Work exercise 5.15.

---
# day 15 | 251001 W

We need to clean up some things from last time (see my email about this to you all). Then we will turn to differentiation, while we also work on some above average homework problems. These are exercises 5.9 and 5.12.

We have been talking about how to do calculus, in particular the integral up till now. But how do we do the derivative? First of all, the calculus itself is nothing other than operations to find either the slope of a function (derivative) or the area under the curve of a function (integral). We often times lose track of what we are actually trying to do when we do this algebraically, so I think it is important to encounter the computational side of things to more fully grasp what is going on.

First off, numerically doing derivatives is very simple, but it is not often done using computers for this reason. If you can do them in your head then why use a computer? But, this is not true for integrals! There are many integrals that do not have a closed form, algebraic solution; so computational methods are necessary to evaluate them. There are also problems with calculating derivatives as we will see, and so they are less used. 

But, first of all we have the definition of the derivative from calculus class
$$\frac{df}{dx} = \lim_{h \rightarrow 0}\frac{f(x+h)-f(x)}{h}$$
And we can do this, just fine except that we cannot divide by zero. But we can make `h` small and maybe that is good enough. 
$$\frac{df}{dx} \approx \frac{f(x+h)-f(x)}{h}$$
This is an approximation that is known as the *forward difference*. And so naturally there is such a thing as the *backward difference*:
$$\frac{df}{dx} \approx \frac{f(x) - f(x-h)}{h}$$

Unfortunately, both of these methods have significant errors. Fortunately, they miss the true value in opposite directions. So we can simply *average* them and get a great approximation. This is known as the *central difference* or *mean finite difference* operator:
$$\frac{df}{dx} \approx \frac{f(x+h)-f(x-h)}{2 h}$$

If you need an even better method, then the symmetric four-point method is the one you want:
$$\frac{df}{dx} \approx \frac{f(x+2h)-8f(x+h)+8f(x-h)-f(x-2h)}{12h}$$

Now what do we choose for `h`? We already know that the smallest the computer can go is machine epsilon. But does that mean it is the best number to use? Let's take a simple function like 
$$ f(x) = \frac{1}{3}x^3$$
and evaluate the derivative of this function at x=1. And then we will compare the results to those we can do by hand. 

Second derivatives are easy to derive from first derivatives. Using the central difference method:
$$\frac{d^2f}{dx^2} \approx \frac{f'(x+h/2)-f'(x-h/2)}{h}$$
$$\frac{d^2f}{dx^2} \approx \frac{[f(x+h)-f(x)]/h - [f(x)-f(x-h)]/h}{h}$$
$$\frac{d^2f}{dx^2} \approx \frac{f(x+h)-2f(x) +f(x-h)}{h^2}$$

So implementing a double derivative is not that much more difficult than a single derivative. 

```

def back(function,x_value, stepSize):
    return (function(x_value)-function(x_value-stepSize))/stepSize

def forward(function,x_value, stepSize):
    return (function(x_value+stepSize)-function(x_value))/stepSize

def mid(function,x_value, stepSize):
    return (function(x_value+stepSize)-function(x_value-stepSize))/(2*stepSize)

def doubled(function, x_value, stepSize):
    return (function(x_value+stepSize)-2*function(x_value)+function(x_value-stepSize))/(stepSize**2)
```

---
# day 14 | 250929 M

We will discuss some other integration methods. We will talk though some quadritures (which is an old word for numerical integration). I have some defined below, but we will also use a function that is provided to us by the author, namely `gaussxy.py` which has a couple of methods within it that we will use. It is important to note that you need to have this python script put in the same folder that you are going to call it from, so whether that is here in `develop` for today, or a copy in `deliver` for any homework, you'll need it in both places. Also, as I mentioned in the email I sent you, this particular bit of script has been updated by the author, so the version that you have in your `data` folder will only work if you look at it and make it work for you. 

We also looked at integrals over infinite ranges, and we used a change in variables to handle those situations. In most cases you can make the following substitution:

$$z = \frac{x}{1+x} \quad \longleftrightarrow \quad x = \frac{z}{1-z}$$

There are other variations on this that you should be aware of like 

$$z = \frac{x-a}{1+x-a}$$ 

but in either case 

$$dx=\frac{dz}{(1-z)^2}$$

Now you can integrate either from 0 -> $\infty$ or a -> $\infty$. To do the other side like from $-\inf$ to 0 or to a, then make z -> -z up above.

---
# day 13 | 250926 F

These days got away from me with the notes. I think we worked on some homework problems as well as integrating a set of data rather than a function. This point is worth emphasizing. When you have data provided to you, or produced from a machine and recorded, there are limitations to how many points you can use to integrate up. So the trapezoid method is likely the best case since it is so simple to implement and use. Simpson's method is trickier because you have to have an odd number of points. So you can use Simpson's method for the odd number and then trapezoid at the end for the last point if you want, and that is what many codes do. Here is one that I cooked up last spring that beat scipy's integrate function in a contest that i am very proud of:

```
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
```

See if you can improve it!

---
# day 12 | 250924 W

I have no idea do you?

Katie Marie says refer to day 11.... 

---
# day 11 | 250922 M

Today we will continue with integration, but we will flip the script and you will work together to implement Simpson's Rule and do exercises 5.2 and 5.3. Simpson's Rule is based on fitting a parabola to a portion of the curve we are interested in and then iterating over each parabola. So look at equation 5.9 on page 146 in the textbook and figure out how to pull that off in python using the numpy.sum function.

Also while we are here I want to emphasize something to you. Look at the author's comment after the problem on page 148. He says, "Note that there is no known way to perform this particular integral analytically, so numerical approaches are the only way forward." This is a very important point and one worth keeping in mind as we go through this class. We are doing things that are increasingly impossible to be done any other way. So computational physics is often not a short cut or a way out of certain problems, but rather it is the only way to get a particular answer. 

---
# day 10 | 250919 F

Integration is essentially addition and so there are fewer problems with dividing by a small number like we had with differentiation. But we still need to be careful about errors like round off. Also similar to differentiation, there is a forward and backward way to integrate, and neither of these are accurate enough to be useful, but there is something in between, in the case of integration that is the trapezoidal rule. And like with differentiation there will be a slightly more complicated method, but also even better than trapezoidal and that is Simpson's rule. 

We will start with Riemann's definition of the integral:

$$\int^b_a f(x) \mathrm{d}x = \lim_{N\rightarrow \infty} \sum_{n=0}^{N-1} f(x_n) h = \lim_{N\rightarrow \infty} \sum_{n=1}^{N} f(x_n) h$$

This simply tells us that these right and left sums are the same when the divisions go to infinity. But of course we can't go to infinity. So, a trapezoidal rule is an average of both the right and left rectangle rules is a way of averaging both:

$$\int^b_a f(x) \mathrm{d}x \approx \sum_{n=0}^{N-1} \frac{f(x_{n+1}) +f(x_n)}{2}h$$
This has the effect after factoring out h/2 and expanding the sum of: 
$$\int^b_a f(x) \mathrm{d}x \approx \frac{h}{2}[f(x_0) + 2f(x_1) + 2f(x_3)+...+ 2f(x_{N-1}) + f(x_{N})]$$

Which can be rewritten as
$$\int^b_a f(x) \mathrm{d}x \approx \frac{h}{2}[f(a) + f(b)] + \sum_{n=1}^{N-1}f(x_n)h$$

And now we can calculate this sum much faster. Implementing this can have some "gotchas", so we have to be careful about how we go about pulling this calculation off. 

Do exercise 5.1 to practice this. But also go back and work on exercise 3.8 as a call back to that chapter on graphing. This is a classic example of a problem that *seems* very difficult, but actually the author walks you through nicely.

---
# day 9 | 250917 W

We used most of our time to talk about homework questions and clean up some previous comments. We also talked a good bit about calculus and specifically integration which we will do a lot of moving forward. We talked about Reimann sums and began to cook up a function that would do this for us, but ran out of time.

---
# day 8 | 250915 M

Today we will practice plotting with real data that would be gathered from some instrument and which you want to plot for your scientific notebook or for a paper. Now that we have the basics of plotting we need to practice this with some real data and see what trouble we run into. So today we will import and trim data, and then prepare some plots based on that data.  

To import some data to python, there are a variety of ways, each depending on how complex the data is. Today, we will start with a simple example of two columns of data in a file. The file extension is readable by python as simply a `comma separated value` or `csv` file. Many files that have various extensions are like this, and many/most experimental apparatus will have the ability to export data in such a format. 

After loading the data using `np.loadtxt()`, we have to take the transform of this file using `data.T`, and then we are able to use matplotlib to plot the data just like before.

Pandas has a more complicated but more capable function called `pd.read_csv()`. This is our first encounter with data stored as a pandas `dataframe` object, but we will practice how to use it to plot some data. 

---
# day 7 | 250912 F

Now that we have the basics of plotting we need to practice this with some real data and see what trouble we run into. So today we will import and trim data, and then prepare some plots based on that data. We also want to check in and follow up on the last few assignments that you have, namely finishing printing out Pascal's triangle as well as finding a python graphing module and showing that off to the class.

To import some data to python, there are a variety of ways, each depending on how complex the data is. Today, we will start with a simple example of two columns of data in a file. The file extension is readable by python as simply a comma separated value or csv file. Many files that have various extensions are like this, and many/most experimental apparatus will have the ability to export data in such a format.

After loading the data using np.loadtxt(), we have to take the transform of this file using data.T, and then we are able to use matplotlib to plot the data just like before.

Next, we will choose a more complicated file, and talk through how we can import it using pandas. Pandas is a python library specifically for handling more complicated data files than numpy is good for. Notice for instance that pandas handles text headers to give a column a particular name. Each pandas column acts like an individual numpy array.

In this case we have a file that has a large header that we need to deal with, as well as a format problem. We will use a statement like this to load the data into what is called a "Data Frame", which is really just python's word for a database.
```
data = pd.read_csv('filename.txt', header=55, sep='\t', encoding='windows-1252')
```
Now some of this is specific to this particular file, but these are some of the options you may need to use from time to time. Each column in this data file already has a name

This will lead us into a discussion of formats and what you can do with them. For example did you know that you can unzip a word document? 

From here, work exercises 3.1 and 3.2. 


---
# day 6 | 250910 W

### Pascal's Triangle

First we will work on Pascal's triangle, since I realized that you don't know about nested loops yet. So we'll get that to work and talk about those.

A nested loop always has a structure like this:

```
for i in some_kind_of_range:
    for j in some_other_range_or_list:
        do_some_stuff_with_i_and_j
    do_more_stuff_with_i
```

What this does is loop through one list and at each step loop through another list. These can be related to each other as in our example in class, or can be totally separate. 

### Chapter 3: plotting!

We will also begin working on plotting things. First we will just cook up some "data" by which I mean we will plot a particular function, and then we will look at some options around how to make this look nice. There are MANY options on how to plot things and change different settings, but we will stick to the simplest ones. Here is an example of how to plot:

```
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10)
y = x**2

fig0 = plt.figure()
ax0 = fig0.add_subplot()

ax0.plot(x, y, 'o', mfc='none')
```
This will plot $y=x^2$ from 0 to 10. Notice how I put in the option `'0'` and `mfc='none'` because that is the kind of plot that *I* like. 

---
# day 5 | 250908 M

Now that we have talked through the major operators in python, we need to put this altogether with the python function. Functions in python are small packages of code that can take in input and execute a series of steps based on that input, and optionally return an output. Functions are defined beginning with def statements so something like this:

```
def myFunction(inputs, go, here, if, necessary):
    print('this is a function')
    output = inputs*go*here**(if+necessary)
    return(output)
```

Now, we can write functions that can perform a particular calculation with different inputs, and we can begin to keep some of these so we can refer to them again later.

We wrote a couple of functions in class, one for calculating factorials and another for understanding spherical coordinates. For homework do exercise 2.11 and take an honest crack at 2.12.  

---
# day 4

First here is a Markdown Cheat sheet: [https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)


Today we need to get to our first new kind of operations in python, `if`, `while`, and `for`.

`if` is a conditional statement, that is if some kind of condition is met, then it will execute a block of code that is underneath it. If that condition is not met, then it won't. You can see how I use if/then statements in that last sentence, and that is basically how python works too. The `then` part of this command is what is executed inside of the `if` statement. IF that condition is not met, then a couple of things can be coded in to happening. Either nothing happens and the program continues with the next command that is issued, or you can put a `else` or `elif` commands and issue another set of instructions for the program to follow in the event that the `if` statement is not true. This true/false property gives us yet another data structure that we have not seen yet: the Boolean. It does not come up as a data type in its own right very often, but it is necessary to control `for` or `while` statements.

Similar to a `while` statement is a `for` loop. A `for` loop iterates over an input, and performs a function that is included within it. `for` and `while` loops can often be used interchangeably, but I find myself usually going to a `for` loop more often. The iterator can be many things, but we will start with base python `range` function and then also use numpy's functions `np.arange` and `np.linspace`. Much of what we do will be using `for` loops although there are some faster ways of doing things using a numpy array that will speed things up. 

As an example, in class we wrote a `while` statement that printed the Fibonacci numbers up to 1000. 

For homework, I want you to write a program that performs a sum of reciprocals. In mathematical language this would look like $s(k) = \sum_1^{100} \frac{1}{k}$. As a check on this, you should get about 5.187. I would use a `for` loop on this. 

---

# day 3

Today we will finish our discussion of data types, by talking about strings and talking about lists or arrays. We have already used strings to print statements in words to the terminal. They are an important class of data, but less used in physics simulations. However the most important data structure to us is the list, and the important upgrade to the array. We will learn to create and import a list, how to print it and will begin to see how to graph it. 

A string is any kind of data stored between single quotes, such as `'Hello World'`. A string can contain numbers, but they are not stored or used as numbers but rather essentially as letters. If a number happens to be stored as a string and you would like to use it as a number, then you can use the `float` or `int` functions for this. There are a few other properties of strings that we can talk about once we get through the next section on *lists*. 

A list is a collection of data structures, and while technically anything can go in the container, we will be dealing with lists mostly as a collection of float numbers. 

---

# day 2

Now that we have `conda` installed and working, we need to make sure it has all of the libraries that we will use. We will use matplotlib, numpy, pandas, and scipy for the most part although there may be others that would be nice. Let's try to use them first and then we will install them if necessary. To import these, we use an import statement like `import numpy as np`. This will bring all of the functions from the `numpy` package into our code, and then we can use them if we first use the `np` identifier. So for example we could now use `np.pi` to use numpy's value for pi. Keep in mind that this is slightly different from the way your book uses import statements. Our way might technically be slower overall, but we won't notice and this will allow us to explore things more easily.

We used a variable in Day 2, but a variable is simply a name or letter that stores a reference to another object in python. I have to _declare_ a variable in order to use it, and in python that means I have to give it a value (even if it won't keep that value). `x` vs `x=5` vs `x=y`.

Also, python is very limited in the math that it can do for you. `x = 5*10` works just fine but `x=y/2` does not nor can python solve for another variable like `y`. 

But something like `x = x + 1` works just fine (as long as x has been defined already), even though it makes no sense to us. In fact, we will do operations like this all the time!

Let's do a few examples (and we'll cover comments along the way):
1. a ball dropped from a tower, given a height and time, tell where the ball is.
2. conversion from polar coordinates to cartesian

# day 1

Quickly review what we talked about last time. 

1. Powershell/Terminal, cd ~, ls, pwd, mkdir
2. Opening a jupyter lab instance in a directory where you want to store things

What we want to talk about today are the various ways that you can run a script with python. So we are going to look at 

1. The interpretor
2. A python script
3. A jupyter lab/notebook session

We will mostly be using jupyter lab sessions as they are interactive and offer a lot of opportunity for experimentation.

We will also show along the way how variables work and how basic math operations work. Everything is mostly what you expect with the exception of exponents, where 2^5 would be written as 2**5 using python. We will also cover code comments along the way.


# day 0

This is where I have to tell you what you should install. Technically, I hope that everyone could install the following software on their computer. These are listed in order of priority

1. Anaconda distribution of Python
2. Mathematica
3. Dropbox (create account, but also download and install)
4. Keepassxc (not essential but a good habit)
5. git (extra special sauce)

If you could begin an account with the following:

1. Dropbox (from above)
2. Overleaf (free, student edition)
3. Github (extra if you get git working)

Talk about AI. I want students to learn to use it as much as they learn to use the computer itself. But start off without it. If you do use it, but big, bright lines around what you got it to teach you.

I talked through the python versions of 1. PowerShell/Terminal 2. Script 3. Jupyter Notebook/Lab. We did a very simple 'hello world' as well as a for loop just to show the differences in each, and went over some typo level gotcha's that come up. End on Jupyter Lab and showed them how that is a nice mid point between the interpreter and a script.

For the interpreter, you should just use terminal on Mac/Linux, and use Powershell for Anaconda on Windows.

For the script, I talk through using a shebang like #!/usr/bin/env python. We looked at mistakes and I showed them how to use the Traceback to kind of find where the problem is, although this is not perfect.

For jupyter, we will but using lab not notebook but they are very similar and students should know how to use both.

Here is chapter 2 of the book: [chapter 2](2-programming.pdf)


    [NbConvertApp] Converting notebook Daily_Log.ipynb to markdown
    [NbConvertApp] Writing 42338 bytes to README.md

