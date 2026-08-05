import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
    sigmoid = 1 / (1 + np.exp(x)**-1)
    return x * sigmoid