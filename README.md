## How do various activation functions affect the output of a neural network?

# Activations Functions tested:

Sigmoid()     = 1/(1+e^(-x))

ReLU()        = MAX(0, x)

Softplus()    = log(1+exp(x))

Binary Step() = if x >=0 : x = 1; if x < 0 : x = 0

# Abstract


## ---------------------------------------------------------


What is an artificial Neural Network?
An Artificial Neural Network (or ANN) works similarly to the brain. It's a collection of nodes (AKA neurons) that are assigned certain values (Called weights)...

Essentially, you use neural networks when you have certain inputs, and you have preferred outputs, and you want to create a function that gives you these preferred outputs given different inputs.

Essentially think of ANN'S (And your brain) and one big regression calculator.

That's all what's going on! A super complex regression!


One key component in an ANN is what's called an "Activation Function," in fact, the output of the activation function is the output of that node/neuron.

So what's inputted into the neural network? Well, the inputs is just the dot product of the weight vector (We were talking about) and the input vector.

In mathematical notation, it looks like this:
ActivationFunction(dot(i, w))


## The question now arises, what is this magical activation function?

Well, it does a few things. It plays a significant role in the training process, and it sometimes limits outputs that get too small or too large.

Well, this brings us to another question, what activation function should I use for the task I'm trying to complete?

Well, we'll have to find out....


In this experiment, I'll be testing the following activation functions:

Sigmoid
<insert graph>

ReLU
<insert graph>

Binary Step
<insert graph>

And softplus
<insert graph>


The neural network that I'll be using has a simple task, recognizing patterns in matrix. More specifically, recognizing Xs and Os

## My hypothesis is that the Binary Step will produce the most accurate prediction (When it's right) but the Sigmoid will produce the most accurate prediction over the most tests.