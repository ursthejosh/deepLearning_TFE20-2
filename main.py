# We will first do some experiments in numpy, no worries there will be enough tensorflow soon.
import numpy as np

x = np.array([[0.2], [2]])
W = np.array([[-0.3, 0.8]])
y = 1

def print_hi(name):
    print(f'Hi, {name}')

def print_version(package):
    print(package.__version__)

def multiplication(W, x):
    q = np.multiply(W, x)
    print(q)
    return q
def prediction(q):
    f_1 = q
    y_pred = multiplication(q, f_1)

    return y_pred


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print_version(np)
    multiplication(W,W)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
