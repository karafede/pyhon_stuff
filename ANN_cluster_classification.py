
# In the following program, we train a neural network to classify two clusters in a 2-dimensional space.
# We show this in the following diagram with the two classes class1 and class2. We will create those points randomly
# with the help of a line, the points of class2 will be above the line and the points of class1 will be below the line.

import numpy as np
import matplotlib.pyplot as plt

class Perceptron:

# in the following the word "self" is referred to the class Perceptron
    def __init__(self, input_length, weights=None):
        if weights is None:
            self.weights = np.ones(input_length) * 0.5
        else:
            self.weights = weights
    @staticmethod
    def unit_step_function(x):
        if x > 0.5:
            return 1
        return 0

    def __call__(self, in_data):
        weighted_input = self.weights * in_data
        weighted_sum = weighted_input.sum()
        return Perceptron.unit_step_function(weighted_sum)

# print(np.array([0.5, 0.5]))

# we have created a static function above: the Perceptron
p = Perceptron(2, np.array([0.5, 0.5]))
# print(p)
data_in = np.empty((2,))
# print(data_in)

# print 0, 1 == data_in
# for i in range(2):
#     print(i)

# define empty arrays
points_in = []
perceptron_out = []

for in1 in range(2):
    for in2 in range(2):
        data_in = (in1, in2)
        data_out = p(data_in)
        print(data_in, data_out)
        points_in.append(data_in)
        perceptron_out.append(data_out)

print(points_in)
print(perceptron_out)


# display point onto a diagram

### settings for plot
fig, ax = plt.subplots()
ax.set_xlabel("class")
ax.set_ylabel("class")
ax.set_xlim([-1, 3])
ax.set_ylim([-1, 3])
colors = ["r", "blue"]  # for the classes
size = 10

# data = np.array(points_in)
# x, y = data.T
# plt.scatter(x,y)
# plt.show()


for (perceptron_out, (x, y)) in enumerate(points_in):
        if perceptron_out == 0:
           ax.plot(x, y, "o",
                 color="darkorange",
                 markersize=size)
        else:
            ax.plot(x, y, "oy",
                    color="blue",
                    markersize=size)

plt.show()

# my_list = ['apple', 'banana', 'grapes', 'pear']
# for c, value in enumerate(my_list, 1):
#     print(c, value)

###############################################################
###############################################################

import numpy as np
from collections import Counter

class Perceptron:

    def __init__(self, input_length, weights=None):
        if weights == None:
            self.weights = np.random.random((input_length)) * 2 - 1
        self.learning_rate = 0.1

    @staticmethod
    def unit_step_function(x):
        if x < 0:
            return 0
        return 1

    def __call__(self, in_data):
        weighted_input = self.weights * in_data
        weighted_sum = weighted_input.sum()
        return Perceptron.unit_step_function(weighted_sum)

    def adjust(self,
               target_result,
               calculated_result,
               in_data):
        error = target_result - calculated_result
        for i in range(len(in_data)):
            correction = error * in_data[i] * self.learning_rate
            self.weights[i] += correction


def above_line(point, line_func):
    x, y = point
    if y > line_func(x):
        return 1
    else:
        return 0


points = np.random.randint(1, 100, (100, 2))
p = Perceptron(2)


def lin1(x):
    return x + 4

for point in points:
    p.adjust(above_line(point, lin1),
             p(point),
             point)

    print(p(point))
    print(point)
evaluation = Counter()
for point in points:
    if p(point) == above_line(point, lin1):
        evaluation["correct"] += 1
    else:
        evaluation["wrong"] += 1
print(evaluation.most_common())












