import numpy as np

def ons_update(weights, gradient, A, beta=1.0):
    A += np.outer(gradient, gradient)
    A_inv = np.linalg.inv(A)
    update = -beta * A_inv @ gradient
    new_weights = weights + update
    new_weights = np.clip(new_weights, 0, 1)
    new_weights /= np.sum(new_weights)
    return new_weights, A
