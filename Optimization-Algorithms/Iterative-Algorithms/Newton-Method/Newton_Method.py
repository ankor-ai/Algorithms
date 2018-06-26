import torch
from torch.autograd import Variable
from torch.autograd import grad

def nth_derivative(f, wrt, n):
    """
    Computes the nth derivative of a multivariable function

    Args:
        param1: the function f to minimize.
        param2: the variable we use to compute the derivative with respect to.
        param3: the order of the derivative.
    Returns:
        a PyTorch tensor containing the the nth derivative of f.
    """

    for i in range(n):

        # We set the optional parameter create_graph to True so that the graph of the derivative will be constructed,
        # allowing to compute higher order derivative, which is what we want in this case.
        grads = grad(f, wrt, create_graph=True)[0]
        f = grads.sum()

    return grads


def newton_step(f, x0):
    """
    Computes the newton step

    Args:
        param1: the function f to minimize.
        param2: the current point where to evaluate the next best direction.
    Returns:
        The newton step.
    """

    gradient = nth_derivative(f(x0), x0, 1)
    hessian = nth_derivative(f(x0), x0, 2)

    return - torch.mm(hessian.inverse(), gradient)


def f(x):
    """
    Computes the function value to minimize. Make sure tohave a function that meets the assumption of the newton's method

    Args:
        param1: the current point in which we want to evaluate the function f.
    Returns:
        The function value at the given point.
    """
    f = (x ** 4).sum()
    return f

def newton(f, x0, threshold = 1e-2):
    """
    Runs the Newton's Method

    Args:
        param1: the function f to minimize.
        param2: the starting point.
        param3: the threshold as a stopping condition to the Newton's method.

    Returns:
        The minimum of the functionf, x star found by the Newton's method.
    """

    x0 = Variable(x0, requires_grad=True)
    value = f(x0)
    while abs(value.data.numpy()) > threshold:
        value = f(x0)
        value.backward()
        x0.data += newton_step(f, x0).data
        x0.grad.data.zero_()
    return x0.data


if __name__ == "__main__":

    # start we an initial point
    x0 = torch.arange(4, requires_grad=True).reshape(2, 2)

    # Run the Newton's method
    x_star = newton(f, x0)
    print("x star = %s" % x_star.numpy())
    print("f(x) = %s" % f(x_star).numpy())
