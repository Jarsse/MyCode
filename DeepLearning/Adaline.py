import math
import matplotlib.pyplot as plt
import numpy as np


class Adaline:
    """
    example class for Adaline with input signals for testing
    """
    weights = []
    output = []

    def __init__(self, learning_rate, iterations, inputs):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.inputs = inputs[0]
        self.desired = inputs[1]
        self.init_weights()
        self.run()

    def init_weights(self):
        """
        initializes weights for each input as 0.1.
        """
        self.weights.extend(0.1 for i in range(len(self.inputs)))

    def calc_error(self, desired, actual):
        """
        Calculates the error using desired output and actual output
        :param desired: Desired output
        :param actual: Actual output given by Adaline
        :return: error amount
        """
        return 0.5*(desired - actual)**2

    def calc_output(self):
        out = []
        for i in range(len(self.inputs)):
            out.append(self.inputs[i] * self.weights[i])
        return out

    def change_in_weight(self, desired, actual, inp):
        """
        calculates the change in weight according to the input, desired output and the output adaline gave
        :param desired: desired output
        :param actual: actual output
        :param inp: input
        :return: change in weight
        """
        change = self.learning_rate * (desired - actual) * inp
        return change

    def update_weights(self, desired, actual, inp):
        """
        updates the weights after each run
        :param desired: list of desired outputs of each input
        :param actual: list of actual outputs given by the network
        :param inp: list of inputs
        """
        for i in range(len(self.weights)):
            self.weights[i] += self.change_in_weight(desired[i], actual[i], inp[i])

    def plot(self):
        plt.title("Inputs:Green\nTesting:Red\nOutput:Blue")
        plt.plot(self.inputs, "g-")
        plt.plot(self.desired, "r-")
        plt.plot(self.output, "b.")
        plt.show()

    def run(self):
        """
        Run the Adaline for iteratrions amount. calculates output for each input and updates weight accordingly
        after iterations plots the input, desired, and output
        """
        for i in range(self.iterations):
            for j in range(len(self.inputs)):
                self.output = self.calc_output()
                self.update_weights(self.desired,self.output,self.inputs)
        self.plot()


def testing(t):
    # x(t)=cos[2t*cos(t)].
    x = math.cos(2*t*math.cos(t))
    return x


def identification(t):
    #  x(t)=sin[10t*sin(t)],
    x = math.sin(10*t*math.sin(t))
    return x


def input_signal(t, id=True):
    # y(t)=x(t)+0.5x(t-1)-1.5x(t-2)
    if id == True:
        y = identification(t) + 0.5*identification(t-1) - 1.5 * identification(t-2)
    else:
        y = testing(t) + 0.5 * identification(t - 1) - 1.5 * identification(t - 2)
    return y


inputs = [[],[]]
steps = np.arange(0,5,0.01)
for i in steps:
    inputs[0].append(input_signal(i))
    inputs[1].append(input_signal(i, False))

Adaline(0.1,100,inputs)
