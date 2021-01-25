import numpy as np
import matplotlib.pyplot as plt
#from termcolor import colored
from data import trainingInputs, trainingOutputs

np.random.seed(1)

#                                       _ number of elements in input
weights = 2 * np.random.random((16, 1)) - 1

e = np.exp(1)
def activation(x):
    return 1 / (1 + e**(-x))
 
def activationDerivative(x):
    return x * (1.0 - x)


def node(inputs):
    inputs = inputs.astype(float) 

    #WHERE THE MAGIC HAPPENS
    return activation(np.dot(inputs, weights))

def train(trainingInputs, trainingOutputs, trainingIterations):
    global weights

    lossHistory = []
    #y = []
    for iteration in range(trainingIterations):
        
        loss = trainingOutputs - node(trainingInputs)
        lossHistory = np.append(lossHistory, loss)
        #y = np.append(y, iteration)
        
        adjustments = np.dot(trainingInputs.T, loss * activationDerivative(node(trainingInputs)))
        #lossHistory = np.append(lossHistory, adjustments)

        weights += adjustments

    #print(lossHistory)
    plt.title("Loss Graph")  
    plt.xlabel("Iterations")
    plt.ylabel("LOSS")  
    plt.plot(lossHistory, color ="red")  
    plt.show() 

#RUN



#Data from data.py
train(trainingInputs, trainingOutputs, 500)
#load()

#save()





inputs = [1, 1, 1, 1, \
          0, 1, 0, 1, \
          1, 0, 0, 1, \
          1, 1, 1, 1]          

print("Output: ", node(np.array(inputs)))
#predict(inputs)


#plot()






























