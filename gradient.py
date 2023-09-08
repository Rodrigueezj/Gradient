import numpy as np 
import matplotlib as plt

def y_function(y):
    r1 = 24.37
    r2 = 30.14
    return 2 * pow((pow(r2,2) - pow(y,2)), 1/2) * (y-r1)


def y_gradient(y):
    return -y *  pow((pow(r2,2) - pow(y,2)), -1/2) * (y - r1) + 2 * pow((pow(r2,2) - pow(y,2)), 1/2)


x = np.arange(r1, r2, 0.01) #
y = y_function(x)

current_pos = (29, y_function(80))

learning_rate =  0.001

for _ in range(1000):
    new_x = current_pos[0] - learning_rate * y_gradient(current_pos[0])
    new_y = y_function(new_x)
    current_pos = ()