import numpy as np

from \
    validate_trial import print_function_error, print_weight_error, plot


def function(x, _params):
    """
    Example function:  y = k x^2

    ----------------------------------------------------------------
    Arguments:
        x (np.ndarray): Point(s) to evaluate the function at

        _params (list(float)): Parameters of the function

    Returns:
        (np.ndarray): Value(s) of the function
    """
    k = params[0]
    return k * x**2


if __name__ == '__main__':

    params = [0.5]

    # Print the difference between the predicted & true function on the data
    print_function_error(function, params)

    # Print the error on the weights (a simple regularisation)
    print_weight_error(params)

    # And plot the function, generating function.png in the current wd
    plot(function, params)
