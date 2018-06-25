# Newton's Method

## Description
This repository provides the description and the implementation of the Newton's method.

Like any standard optimization problem, we define the optimization problem as follows:

<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5CLARGE%20%24%5Cmin%5Climits_%7B%5Cmathbf%7Bx%7D%7D%20%5C%3B%20f%28%5Cmathbf%7Bx%7D%29%24">
</p>

## Assumptions of the Newton's method
* f is *twice differentiable* (i.e. twice Lipschitz continuously):

<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5CLARGE%20%5ClVert%20%5Cnabla%5E%7B2%7Df%28x%29%20-%20%5Cnabla%5E%7B2%7Df%28y%29%20%5ClVert%20%5C%3B%5Cleq%20%5Cgamma%20%5C%3B%20%5ClVert%20x-y%20%5ClVert">
</p>


## Newton's method for a one variable function

<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5CLARGE%20%5Chat%7Bx%7D_%7Bn&plus;1%7D%20%3D%20%5Chat%7Bx%7D_%7Bn%7D%20-%20%5Cfrac%7Bf%28%5Chat%7Bx%7D_%7Bn%7D%29%7D%7Bf%27%28%5Chat%7Bx%7D_%7Bn%7D%29%7D">
</p>

## Newton's method for a multi-variable function

<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5CLARGE%20%5Chat%7B%5Ctextbf%7Bx%7D%7D_%7Bn&plus;1%7D%20%3D%20%5Chat%7B%5Ctextbf%7Bx%7D%7D_%7Bn%7D%20-%20f%28%5Chat%7B%5Ctextbf%7Bx%7D%7D_%7Bn%7D%29%20%5Cbig%5B%20%5Cnabla%20f%28%5Chat%7B%5Ctextbf%7Bx%7D%7D_%7Bn%7D%29%20%5Cbig%5D%5E%7B-1%7D">
</p>
