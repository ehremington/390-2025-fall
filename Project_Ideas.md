# Project Ideas

## Romberg Integration. 

Sophomore only? Figure out Romberg Integration and explain it and compare it to Trapezoid and Simpson's Method. Needs some extension here. 

## Gauss-Laguerre, Gauss-Hermite Quadrature

I mentioned these other quadratures, but what is a quadrature? Use the explanation found in the textbook for Gauss-Legendre Quadrature to figure out how to these other quadratures. For what kinds of problems are they useful? Make a comparison of these methods with Gauss-Legendre and a change in variables to handle the infinite range.

## Scattering by Yukawa Potential

The Yukawa Potential is an important potential energy that is used in materials science. 

$$U(r) = \frac{k}{r} e^{-r/a} $$

To calculate the scattering angle of a particle through this spherical potential

$$\phi = \int_{r_0}^{\infty} \frac{b}{r^2} \frac{1}{\sqrt{1 - \displaystyle\frac{b^2}{r^2}-\displaystyle\frac{U(r)}{E}}} dr\,  $$

and the lower limit of that integral can only be found by solving

$$1 - \frac{b^2}{r_0^2}-\frac{U(r_0)}{E} = 0\,$$

So that's fun. I have more to say about this one but that's the gist. 

## Classical Turning Points

The period of oscillation for a particle confined in a potential energy profile of U(x) is given by

$$T = 2 \int_{x_1}^{x_2} \frac{1}{v(x)} dx $$

and the speed v(x) of the particle is given by


$$ v(x) = \sqrt{\frac{2(E-U(x)}{m}} $$

The integral bounds are found by solving \(v(x) = 0\), which uses root finding methods. But aside from this problem there is another problem that the integral is improper since \\(v(x_1) = 0\\). So that needs to be figured out. We could do this with a few different potentials but here is one:

$$U(x) = U_0 \left[\sin \left(\frac{2 \pi x}{L}\right) - \frac{1}{4} \sin \left(\frac{4 \pi x}{L}\right) \right] $$

The turning points are when \\(U(x) = E\\)

## Diffraction and Bessel Functions

This is mostly following problem 5.4, but with the extension that you do some root finding to find the first several zeros of the Bessel Functions. You will have to go back to chapter 3 to learn about contour plotting and show the Airy pattern rings. 

## 6.18 and Golden Ratio Search

This is mostly out of the textbook, but it will require you to dig into a section and teach us all what is going on there. 
