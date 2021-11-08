from helper_functions import print_function_error, print_weight_error, plot


def function(x, c):
    """
    Example function:  y = c_0 x^2

    ----------------------------------------------------------------
    Arguments:
        x (np.ndarray): Point(s) to evaluate the function at

        c (list(float)): Parameters (coefficients) of the function

    Returns:
        (np.ndarray): Value(s) of the function
    """
    return c[0] * x**2


if __name__ == '__main__':

    coefficients = [0.5]

    # Print the difference between the predicted & true function on the data
    print_function_error(function, coefficients)

    # Print the error on the coefficients of the function
    print_weight_error(coefficients)

    # And plot the function, generating function.png in the current wd
    plot(function, coefficients)
