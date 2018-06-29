# Natural Gradient Method

## Description
This repository provides the description and the implementation of the natural gradient method.

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

Now that we defined the assumption of the natural gradient method, and before digging into its technical details, we should review the basic concepts behind standard gradient descent and understand some of its performance limitations.

## Review of the standard gradient descent method

To describe standard gradient descent method, we consider a function <img src="https://latex.codecogs.com/gif.latex?f%28%5Ctextbf%7Bw%7D%29"> to minimize with respect to its parameters:
<!--
\textbf{w}(k) = [\;w_1(k), w_2(k), \dots, w_n(k)\;]^T
-->
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Ctextbf%7Bw%7D%28k%29%20%3D%20%5B%5C%3Bw_1%28k%29%2C%20w_2%28k%29%2C%20%5Cdots%2C%20w_n%28k%29%5C%3B%5D%5ET">
</p>

where <img src="https://latex.codecogs.com/gif.latex?w_i%28k%29"> is the ith parameter value at time k.

The standard descent method is an iterative procedure for locally-minimizing <img src="https://latex.codecogs.com/gif.latex?f%28%5Ctextbf%7Bw%7D%29"> with respect to <img src="https://latex.codecogs.com/gif.latex?%5Ctextbf%7Bw%7D">, defined as:
<!--
\textbf{w}(k+1) = \textbf{w}(k) - \eta \; \frac{\partial f(\textbf{w}(t))}{\partial \textbf{w}}
-->
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Clarge%20%5Ctextbf%7Bw%7D%28k&plus;1%29%20%3D%20%5Ctextbf%7Bw%7D%28k%29%20-%20%5Ceta%20%5C%3B%20%5Cfrac%7B%5Cpartial%20f%28%5Ctextbf%7Bw%7D%28t%29%29%7D%7B%5Cpartial%20%5Ctextbf%7Bw%7D%7D">
</p>

where <img src="https://latex.codecogs.com/gif.latex?%5Ceta"> is a fixed step size. Many adaptative variants of the standard gradient descent makes the step size dependent on time using different strategies. However, we choose to <img src="https://latex.codecogs.com/gif.latex?%5Ceta"> to be constant since this is not related to the deep understanding of the natural gradient.

The standard gradient descent equation tells us that a fraction <img src="https://latex.codecogs.com/gif.latex?%5Ceta"> of the gradient of the function <img src="https://latex.codecogs.com/gif.latex?f%28%5Ctextbf%7Bw%7D%29"> with respect to each parameter is subtracted from each parameter <img src="https://latex.codecogs.com/gif.latex?w_i%28k%29">. This process is continued indefinitely or until the value of <img src="https://latex.codecogs.com/gif.latex?%5Ctextbf%7Bw%7D%28k%29"> reaches a suitably-small value, at which point <img src="https://latex.codecogs.com/gif.latex?%5Ctextbf%7Bw%7D%28k%29"> is close to <img src="https://latex.codecogs.com/gif.latex?%5Ctextbf%7Bw%7D%5E*">.

### Limitation of the standard gradient descent:

The transient behavior of any gradient descent method depends on the form of <img src="https://latex.codecogs.com/gif.latex?f%28%5Ctextbf%7Bw%7D%29">. One major limitation stems from the fact that the gradient components <img src="https://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20f%28%5Ctextbf%7Bw%7D%28k%29%29%7D%7B%5Cpartial%20w_i%7D"> **vary widely
in magnitude in different directions** from <img src="https://latex.codecogs.com/gif.latex?%5Ctextbf%7Bw%7D%5E*">.
---
We define the optimization problem as:
<!--
\textbf{x}^* = \min\limits_{\textbf{x}} \;f(\textbf{x})
-->
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Clarge%20%5Ctextbf%7Bx%7D%5E*%20%3D%20%5Cmin%5Climits_%7B%5Ctextbf%7Bx%7D%7D%20%5C%3Bf%28%5Ctextbf%7Bx%7D%29">
</p>



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
\upsilon^* = -\big[ \nabla^2 f(x) \big]^{-1} \;\nabla f(x)
-->
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Clarge%20%5Cupsilon%5E*%20%3D%20-%5Cbig%5B%20%5Cnabla%5E2%20f%28x%29%20%5Cbig%5D%5E%7B-1%7D%20%5C%3B%5Cnabla%20f%28x%29">
</p>

<img src="https://latex.codecogs.com/gif.latex?%5Csmall%20%5Cupsilon%5E*"> is know as the Newton step. It is the descent direction that Newton's method uses to minimize f.

## Pros and cons:

If the function f is quadratic, then x + <img src="https://latex.codecogs.com/gif.latex?%5Csmall%20%5Cupsilon"> is the exact minimizer of f. If the function f is nearly quadratic, intuition suggests that <img src="https://latex.codecogs.com/gif.latex?%5Csmall%20x&plus;%5Cupsilon"> should be a very good estimate of the minimizer of f, i.e., <img src="https://latex.codecogs.com/gif.latex?%5Csmall%20x%5E*">. In other words, the performance of Newton's method depends on how good the quadratic approximation is.


## Implementation

We implemented the Newton's method in Python 3 using PyTorch. We chose the function <img src="https://latex.codecogs.com/gif.latex?%5Csmall%20f%28%5Ctextbf%7Bx%7D%29%20%3D%20%24%5Csum%20x_i%5E4%24"> where <img src="https://latex.codecogs.com/gif.latex?%5Csmall%20x%20%5Cin%20%5Cmathbb%7BR%7D%5E%7Bm%20%5Ctimes%20n%7D">.

You can simply use the code by running:
``` shell
python3 Newton_Method.py
```

## References
* [Newton's method section of Stephen Boyd's book](http://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf#page=498)
* [Stephen Boyd's Stanford lecture](https://www.youtube.com/watch?v=sTCtkkqrY8A#t=1924)
