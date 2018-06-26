# Newton's Method

## Description
This repository provides the description and the implementation of the Newton's method.

Newton's method is an optimization algorithm which, in the convex setting, iteratively minimizes **quadratic approximations** to the objective function. It can be impractical for high-dimensional problems because it requires inverting the Hessian matrix, but many highly effective optimization algorithms can be viewed as approximations to Newton's method.

We define the optimization problem as:

<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5CLARGE%20%5Cmathbf%7Bx%5E*%7D%20%3D%20%5C%3B%24%5Cmin%5Climits_%7B%5Cmathbf%7Bx%7D%7D%20%5C%3B%20f%28%5Cmathbf%7Bx%7D%29%24" height="42" width="42">
</p>

## Assumptions of the Newton's method

To guarantee the convergence, this method assume the following assumptions:

* f is *twice differentiable* (i.e. twice Lipschitz continuously):

<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5CLARGE%20%5ClVert%20%5Cnabla%5E%7B2%7Df%28x%29%20-%20%5Cnabla%5E%7B2%7Df%28y%29%20%5ClVert%20%5C%3B%5Cleq%20%5Cgamma%20%5C%3B%20%5ClVert%20x-y%20%5ClVert">
</p>

* first order stationarity assumption:
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5CLARGE%20%5ClVert%20%5Cnabla%20f%28x%5E*%29%20%5ClVert%20%5C%3B%20%3D%5C%3B%200">
</p>

* the Hessian of f is positive definite (i.e. all the eigenvalues of the Hessian are strictly positive)

## Newton's method for a one variable function

In the one-dimensional problem, Newton's method finds the roots attempts to construct a sequence x\_n from an initial guess x0 that converges towards some value x* satisfying f'(x*)=0. This x* is a stationary point of f.

<p align="center">
  <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/e06f508d23a4ee050f8af7b46f2e345b9dd6b2f2">
</p>

<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5CLARGE%20%5Chat%7Bx%7D_%7Bn&plus;1%7D%20%3D%20%5Chat%7Bx%7D_%7Bn%7D%20-%20%5Cfrac%7Bf%28%5Chat%7Bx%7D_%7Bn%7D%29%7D%7Bf%27%28%5Chat%7Bx%7D_%7Bn%7D%29%7D">
</p>

## Newton's method for a multi-variable function

<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5CLARGE%20%5Chat%7B%5Ctextbf%7Bx%7D%7D_%7Bn&plus;1%7D%20%3D%20%5Chat%7B%5Ctextbf%7Bx%7D%7D_%7Bn%7D%20-%20f%28%5Chat%7B%5Ctextbf%7Bx%7D%7D_%7Bn%7D%29%20%5Cbig%5B%20%5Cnabla%20f%28%5Chat%7B%5Ctextbf%7Bx%7D%7D_%7Bn%7D%29%20%5Cbig%5D%5E%7B-1%7D">
</p>

# References
* [Newton's method section of Stephen Boyd's book](http://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf#page=498)
* [Stephen Boyd's Stanford lecture](https://www.youtube.com/watch?v=sTCtkkqrY8A#t=1924)

