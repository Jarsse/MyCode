
class Perceptron:
    """
    Perceptron example class
    """
    weights = []

    def __init__(self, learning_rate, threshold, iterations, inputs):
        """
        :param learning_rate: learning rate of the perceptron
        :param threshold: threshold for perceptron output
        :param iterations: number of training iterations
        :param inputs: inputs of type [[[x,y],z],[[x1,y1],z1],...,[[xn,yn],zn],] where x, y inputs, z target output
        """
        self.learning_rate = learning_rate
        self.threshold = threshold
        self.iterations = iterations
        self.inputs = inputs
        self.init_weights()
        self.run()

    def init_weights(self):
        """
        initializes the weights for the perceptron based on the length of the input
        """
        self.weights = [0 for i in range(len(self.inputs[0][0]))]

    def update_weights(self, inp, outp, actual):
        """
        updates the weights of the perceptron
        :param inp: input values
        :param outp: output given by perceptron
        :param actual: true output
        """
        for i in range(len(self.weights)):
            self.weights[i] += self.learning_rate * (actual - outp) * inp[i]

    def err(self, target, actual):
        """
        calculates the current error value
        :param target: true output
        :param actual: actual output given by Perceptron
        :return:
        """
        return target-actual

    def calc_output(self, inp):
        """
        Calculates output for given input inputs inp
        :param inp: x and y value
        :type inp: list<int>
        :return:
        """
        y = 0
        for i in range(len(inp)):
            y += inp[i]*self.weights[i]
        if y >= self.threshold:
            return 1
        else:
            return 0

    def run(self):
        """
        At each iteration calcs output, prints input, output and target output.
        Then updates weights.
        :return:
        """
        for _ in range(self.iterations):
            for i in range(len(self.inputs)):
                outp = self.calc_output(self.inputs[i][0])
                print("Round: {}   Input: {}".format(_, self.inputs[i][0]))
                print("Perceptron's output: {}".format(outp))
                print("Target output:       {}".format(self.inputs[i][1]))
                #print("Weights: {}".format(self.weights))
                self.update_weights(self.inputs[i][0], outp, self.inputs[i][1])


def test():
    """
    Testing perceptron with and, or, xor inputs
    """
    and_input = [[[0,0],0],
                 [[0,1],0],
                 [[1,0],0],
                 [[1,1],1]]

    or_input = [[[0,0],0],
                [[0,1],1],
                [[1,0],1],
                [[1,1],1]]

    xor_input = [[[0,0],0],
                 [[0,1],1],
                 [[1,0],1],
                 [[1,1],0]]

    Perceptron(0.1,10,100, and_input)
    #Perceptron(0.1,10,100, or_input)
    #Perceptron(0.1,10,100, xor_input)


test()