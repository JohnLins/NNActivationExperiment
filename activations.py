import numpy as np
e = np.exp(1)

def sigmoid(x):
    return 1 / (1 + e**(-x))

def Dsigmoid(x):
    return x * (1.0 - x)  


def binaryStep(x):
    if x >= 0:
        return 1
    else:
        return 0
def DbinaryStep(x):
    return 0


def ReLU(x):
    if x > 0:
        return x
    else:
        return 0

def DReLU(x):
    if x <= 0:
        return 0
    else:
        return 1;