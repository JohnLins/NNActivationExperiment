import numpy as np
import matplotlib.pyplot as plt
from data import trainingInputs, trainingOutputs

from activations import *

np.random.seed(1)

#                                    _ number of elements in input
weights = 2 * np.random.random((16, 1)) - 1


def activation(x):
    return johnStep(x)
 
def activationDerivative(x):
    return DjohnStep(x)


def node(inputs):
    inputs = inputs.astype(float) 

    #WHERE THE MAGIC HAPPENS
    return activation(np.dot(inputs, weights))

lossHistory = []
def train(trainingInputs, trainingOutputs, trainingIterations):
    global weights
    global lossHistory

    for iteration in range(trainingIterations):
        output = node(trainingInputs)
        loss = trainingOutputs - output
        lossHistory = np.append(lossHistory, loss)
        
        adjustments = np.dot(trainingInputs.T, loss * activationDerivative(output))

        weights += adjustments

train(trainingInputs, trainingOutputs, 200)

def predict(inputs):
    inputs = inputs.astype(float) 

    output = node(inputs)

    plt.title("Loss Graph")  
    plt.xlabel("Iterations")
    plt.ylabel("LOSS")  

    slash = 1 - output
    o = output - 0

    if slash < o:
        return output, "Slash \\"
    elif o < slash:
        return output, "Letter O"
    else:
        return output, "Both"


    


































