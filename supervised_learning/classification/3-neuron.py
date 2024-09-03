#!/usr/bin/env python3
"""
Neural Class
"""
import numpy as np


class Neuron:
    """
    Neuron class represents a single neuron in a neural network.

    Attributes:
        nx (int): The number of input features.
        W (ndarray): The weights vector for the neuron.
        b (float): The bias for the neuron.
        A (float): The activated output of the neuron (forward propagation).
    """

    def __init__(self, nx):
        """
        Initializes a neuron.

        Args:
            nx (int): The number of input features.

        Raises:
            TypeError: If nx is not an integer.
            ValueError: If nx is not a positive integer.
        """
        if type(nx) != int:
            raise TypeError('nx must be an integer')
        if nx < 1:
            raise ValueError('nx must be a positive integer')
        self.nx = nx
        self.__W = np.random.normal(size=(1, nx))
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        return self.__W

    @W.setter
    def W(self, value):
        self.__W = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        self.__b = value

    @property
    def A(self):
        return self.__A

    def forward_prop(self, X):
        """
        Forward propagates the input data through the neuron.

        Arguments:
        X: numpy.ndarray - Input data with shape (nx, m).

        Returns:
        numpy.ndarray - The activated output of the neuron.
        """
        Z = np.matmul(self.W, X) + self.b
        sigmoid = 1 / (1 + np.exp(-Z))
        self.__A = sigmoid
        return self.__A

    def cost(self, Y, A):
        """
        Calculates the cost using logistic regression.

        Args:
            Y: numpy.ndarray - The correct labels for the input data.
            A: numpy.ndarray - The activated output of the neuron.

        Returns:
            float: The cost value.
        """
        m = Y.shape[1]
        # Clip A to avoid log(0) issues
        A_clipped = np.clip(A, 1e-10, 1 - 1e-10)
        cost = -(1 / m) * np.sum(Y * np.log(A_clipped) + (1 - Y) * np.log(1 - A_clipped))
        return cost
