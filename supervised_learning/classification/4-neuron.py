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
        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        return self.__W

    @property
    def b(self):
        return self.__b

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
        Z = np.dot(self.__W, X) + self.__b
        self.__A = 1 / (1 + np.exp(-Z))
        return self.__A

    def cost(self, Y, A):
        """
        Calculate the cross-entropy loss function.

        Parameters:
        Y (numpy array): Ground truth labels, shape (1, m).
        A (numpy array): Predicted probabilities, shape (1, m).

        Returns:
        float: Cross-entropy loss.
        """
        m = Y.shape[1]
        cost = -(1 / m) * np.sum(Y * np.log(A) + (1 - Y) * np.log(1 - A))
        return cost

    def evaluate(self, X, Y):
        """
        Evaluate the model's predictions and cost on given input data.

        Parameters:
        X (numpy array): Input data, shape (input_size, m).
        Y (numpy array): Ground truth labels, shape (1, m).

        Returns:
        tuple: A tuple containing:
            - numpy.ndarray: Labelized predictions (0 or 1).
            - float: Cost of the model.
        """
        A = self.forward_prop(X)
        cost = self.cost(Y, A)
        predictions = np.where(A >= 0.5, 1, 0)
        return predictions, cost
