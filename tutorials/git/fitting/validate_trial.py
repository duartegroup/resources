import numpy as np
import matplotlib.pyplot as plt

xs = np.array([0.21121121, -0.4034034, 0.39139139, 0.78578579, -0.55155155,
               0.56556557, 0.92392392, -0.6996997, 0.95795796, -0.91591592])

ys = np.array([0.23533653, -0.31035679, 0.45911638, 0.31506996, -0.29502177,
               0.60401143, -0.50146046, -0.04222024, -0.82460688, 1.27242725])


def print_function_error(function, params):
    """Print the loss of a trial function fitting some data"""
    return print(f'|f(x) - y|    =    '
                 f'{np.linalg.norm(function(xs, params) - ys):.5f}')


def print_weight_error(params):
    """Print the difference between the true and trial polynomial weights,
    as the sum of the squares """

    true_ss_w = 11.230715512200469
    ss_w = np.sum(np.square(np.array(params)))

    return print(f'|SS_true - SS_f| = {np.abs(true_ss_w - ss_w):.5f}')


def plot(function, params):
    """Plot the trial function over the data"""

    plt.scatter(xs, ys, marker='s', facecolors='none', edgecolors='tab:blue')

    smooth_xs = np.linspace(-1., 1.)

    plt.plot(smooth_xs, function(smooth_xs, params), c='tab:orange')
    plt.plot([-1, 1], [0., 0.], c='k', lw=0.5)
    plt.plot([0., 0.], [2., -2.], c='k', lw=0.5)

    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.xlim(-1, 1)
    plt.ylim(-2, 2)
    plt.tight_layout()
    plt.savefig('function.png', dpi=300)

    return None
