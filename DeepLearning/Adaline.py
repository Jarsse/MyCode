import math
import matplotlib.pyplot as plt
import numpy as np
import random


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
        self.weights.extend(random.random() for i in range(len(self.inputs)))

    def calc_error(self, desired, actual):
        """
        Calculates the error using desired output and actual output
        :param desired: Desired output
        :param actual: Actual output given by Adaline
        :return: error amount
        """
        return desired-actual

    def calc_output(self, inputs=None):
        if not inputs:
            inputs = self.inputs
        # otherwise testing
        sum = 0
        for j in range(len(inputs)):
            sum += inputs[j] * self.weights[j]
        return sum

    def change_in_weight(self, desired, actual, inp):
        """
        calculates the change in weight according to the input, desired output and the output adaline gave
        :param desired: desired output
        :param actual: actual output
        :param inp: input
        :return: change in weight
        """
        change = self.learning_rate * self.calc_error(desired,actual) * inp

        return change

    def update_weights(self, desired, actual, inp):
        """
        updates the weights after each run
        :param desired: list of desired outputs of each input
        :param actual: list of actual outputs given by the network
        :param inp: list of inputs
        """
        for i in range(len(inp)):
            self.weights[i] += self.change_in_weight(desired, actual, inp[i])

    def test(self, inputs, desireds):
        """
        Test the Adaline with given inputs
        :param inputs: testing inputs
        :param desireds: desired outputs for testing inputs
        """
        outputs = []
        for i in inputs:
            outputs.append(self.calc_output(i))
        self.plot(inputs, outputs, desireds)

    def plot(self, inputs=None, outputs=None, desireds=None):
        """
        plot the input values, testing values and output values given by adaline
        """
        if not inputs:
            inputs = self.inputs
        if not outputs:
            outputs = self.output
        if not desireds:
            desireds = self.desired
        plt.title("Inputs:Green\nDesired:Red\nOutput:Blue")
        #plt.plot(inputs, "g-")
        plt.plot(desireds, "r-")
        plt.plot(outputs, "b-.")
        plt.show()

    def run(self):
        """
        Run the Adaline for iteratrions amount. calculates output for each input and updates weight accordingly
        after iterations plots the input, desired, and output
        """
        for iteration in range(self.iterations):
            self.output = []
            for i in range(len(self.inputs)):
                self.output.append(self.calc_output(self.inputs[i]))
                self.update_weights(self.desired[i], self.output[i], self.inputs[i])
        self.plot()


def testing(t):
    """Used in generating testing input for testing purposes."""
    x = math.cos(2*t*math.cos(t))
    return x


def identification(t):
    """Used in generating input for testing"""
    x = math.sin(10*t*math.sin(t))
    return x


def y_signal(t, id=True):
    """Used for generating the desired output for input and testing input for testing purposes."""
    if id == True:
        y = identification(t) + 0.5*identification(t-1) - 1.5 * identification(t-2)
    else:
        y = testing(t) + 0.5*testing(t-1) - 1.5 * testing(t-2)
    return y

# generate inputs and testing inputs
inputs = [[],[]]
test_inputs = [[],[]]
steps = np.arange(0,5,0.01)

for i in steps:
    inputs[0].append([identification(i), identification(i-1), identification(i-2)])
    inputs[1].append(y_signal(i, True))
    test_inputs[0].append([testing(i), testing(i-1), testing(i-2)])
    test_inputs[1].append(y_signal(i, False))
# run adaline and test it
adaline = Adaline(0.1,100,inputs)

adaline.test(test_inputs[0], test_inputs[1])
