import numpy as np
from scipy.optimize import minimize
from helper_functions import sum_square_error, plot


def trial_function(x, c):
    """Simple trial function:
        c_0 x + c_1 x^2
    """
    return c[0] * x + c[1] * x**2


if __name__ == '__main__':

    # Define an initial guess of the coefficients
    initial_c = np.array([0.1, 0.2])

    # Minimise the SS between true and predicted given the parameters
    result = minimize(sum_square_error,
                      initial_c,
                      args=(trial_function,))

    # and plot the function with the optimised parameters
    plot(function=trial_function,
         params=result.x)
