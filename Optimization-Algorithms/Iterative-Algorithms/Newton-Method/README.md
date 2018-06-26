# Newton's Method

## Description
This repository provides the description and the implementation of the Newton's method.

Newton's method is an optimization algorithm which, in the convex setting, iteratively minimizes **quadratic approximations** to the objective function. It can be impractical for high-dimensional problems because it requires inverting the Hessian matrix, but many highly effective optimization algorithms can be viewed as approximations to Newton's method.

We define the optimization problem as:
<!--
\textbf{x}^* = \min\limits_{\textbf{x}} \;f(\textbf{x})
-->
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Clarge%20%5Ctextbf%7Bx%7D%5E*%20%3D%20%5Cmin%5Climits_%7B%5Ctextbf%7Bx%7D%7D%20%5C%3Bf%28%5Ctextbf%7Bx%7D%29">
</p>

## Assumptions of the Newton's method

To guarantee the convergence, this method assume the following assumptions:

* f is *twice differentiable* (i.e. twice Lipschitz continuously):
<!--
\| \nabla^2f(x) - \nabla^2f(y)\| \leq \gamma \; \| x -y\|
-->
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Clarge%20%5C%7C%20%5Cnabla%5E2f%28x%29%20-%20%5Cnabla%5E2f%28y%29%5C%7C%20%5Cleq%20%5Cgamma%20%5C%3B%20%5C%7C%20x%20-y%5C%7C">
</p>

* first order stationarity assumption:
<!--
\| \nabla f(\textbf{x}^*)\| = \textbf{0}
-->
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Clarge%20%5C%7C%20%5Cnabla%20f%28%5Ctextbf%7Bx%7D%5E*%29%5C%7C%20%3D%20%5Ctextbf%7B0%7D">
</p>

* the Hessian of f is positive definite (i.e. all the eigenvalues of the Hessian are strictly positive)

## Newton's method

The Newton's method approximate the function f using a second-order Tayolor expansion:
<!--
f(x+\upsilon) \approx \hat{f}(x+\upsilon) = f(x) + \nabla f(x)^T \upsilon + \frac{1}{2}\; \upsilon^T \;\nabla^2 f(x)\; \upsilon
-->
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Clarge%20f%28x&plus;%5Cupsilon%29%20%5Capprox%20%5Chat%7Bf%7D%28x&plus;%5Cupsilon%29%20%3D%20f%28x%29%20&plus;%20%5Cnabla%20f%28x%29%5ET%20%5Cupsilon%20&plus;%20%5Cfrac%7B1%7D%7B2%7D%5C%3B%20%5Cupsilon%5ET%20%5C%3B%5Cnabla%5E2%20f%28x%29%5C%3B%20%5Cupsilon">
</p>

which is a convex quadratic function of <img src="https://latex.codecogs.com/gif.latex?%5Csmall%20%5Cupsilon">. In other words, the newton's method tries to find what should be the direction <img src="https://latex.codecogs.com/gif.latex?%5Csmall%20%5Cupsilon"> added to the point x to minimize the second-order approximation of f at x, <img src="https://latex.codecogs.com/gif.latex?%5Csmall%20f%28x&plus;%5Cupsilon%29">.

In order to do find the best <img src="https://latex.codecogs.com/gif.latex?%5Csmall%20%5Cupsilon">, we set the derivative of the quadratic approximation to 0 and solve it with respect to <img src="https://latex.codecogs.com/gif.latex?%5Csmall%20%5Cupsilon">:
<!--
\textbf{0} = \nabla f(x+\upsilon) \approx \nabla \hat{f}(x+\upsilon) = \nabla f(x) + \nabla^2 f(x)\; \upsilon
-->
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Clarge%20%5Ctextbf%7B0%7D%20%3D%20%5Cnabla%20f%28x&plus;%5Cupsilon%29%20%5Capprox%20%5Cnabla%20%5Chat%7Bf%7D%28x&plus;%5Cupsilon%29%20%3D%20%5Cnabla%20f%28x%29%20&plus;%20%5Cnabla%5E2%20f%28x%29%5C%3B%20%5Cupsilon">
</p>

Thus, we can conclude that the best <img src="https://latex.codecogs.com/gif.latex?%5Csmall%20%5Cupsilon"> is:
<!--
\upsilon^* = \big[ \nabla^2 f(x) \big]^{-1} \;\nabla f(x)
-->
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Clarge%20%5Cupsilon%5E*%20%3D%20%5Cbig%5B%20%5Cnabla%5E2%20f%28x%29%20%5Cbig%5D%5E%7B-1%7D%20%5C%3B%5Cnabla%20f%28x%29">
</p>

<img src="https://latex.codecogs.com/gif.latex?%5Csmall%20%5Cupsilon%5E*"> is know as the Newton step. It is the descent direction that Newton's method uses to minimize f.

## Pros and cons:

If the function f is quadratic, then x + <img src="https://latex.codecogs.com/gif.latex?%5Csmall%20%5Cupsilon"> is the exact minimizer of f. If the function f is nearly quadratic, intuition suggests that x + <img src="https://latex.codecogs.com/gif.latex?%5Csmall%20%5Cupsilon"> should be a very good estimate of the minimizer of f, i.e., <img src="https://latex.codecogs.com/gif.latex?%5Csmall%20x%5E*">. In other words, the performance of Newton's method depends on how good the quadratic approximation is.


## Implementation
TO ADD

## References
* [Newton's method section of Stephen Boyd's book](http://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf#page=498)
* [Stephen Boyd's Stanford lecture](https://www.youtube.com/watch?v=sTCtkkqrY8A#t=1924)

