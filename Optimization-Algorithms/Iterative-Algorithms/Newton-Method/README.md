# Newton's Method

## Description
This repository provides the description and the implementation of the Newton's method.

Like any standard optimization problem, we define the optimization problem as follows:

<p align="center">
![optimization_problem_definition](https://latex.codecogs.com/gif.latex?%5CLARGE%20%24%5Cmin%5Climits_%7B%5Cmathbf%7Bx%7D%7D%20%5C%3B%20f%28%5Cmathbf%7Bx%7D%29%24)
</p>

## Assumptions of the Newton's method
By a local convergence method we mean one that requires that the initial iterate x0 is close to a
local minimizer x∗ at which the sufficient conditions hold.

## Newton's method for a one variable function
![newton_onevariable_equation](https://latex.codecogs.com/gif.latex?%5CLARGE%20%5Chat%7Bx%7D_%7Bn&plus;1%7D%20%3D%20%5Chat%7Bx%7D_%7Bn%7D%20-%20%5Cfrac%7Bf%28%5Chat%7Bx%7D_%7Bn%7D%29%7D%7Bf%27%28%5Chat%7Bx%7D_%7Bn%7D%29%7D)
## Newton's method for a multi-variable function
![newton_multivariable_equation](https://latex.codecogs.com/gif.latex?%5CLARGE%20%5Chat%7B%5Ctextbf%7Bx%7D%7D_%7Bn&plus;1%7D%20%3D%20%5Chat%7B%5Ctextbf%7Bx%7D%7D_%7Bn%7D%20-%20f%28%5Chat%7B%5Ctextbf%7Bx%7D%7D_%7Bn%7D%29%20%5Cbig%5B%20%5Cnabla%20f%28%5Chat%7B%5Ctextbf%7Bx%7D%7D_%7Bn%7D%29%20%5Cbig%5D%5E%7B-1%7D)
