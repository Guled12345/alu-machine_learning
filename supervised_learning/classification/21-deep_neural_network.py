#!/usr/bin/env python3
"""Creating a deep neural network"""

import numpy as np


class DeepNeuralNetwork:
    """Deep neural network"""

    def __init__(self, nx, layers):
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if not isinstance(layers, list):
            raise TypeError("layers must be a list of positive integers")
        if len(layers) < 1:
            raise TypeError("layers must be a list of positive integers")

        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}

        for i in range(self.__L):
            if not isinstance(layers[i], int) or layers[i] < 1:
                raise TypeError('layers must be a list of positive integers')

            if i == 0:
                # He-et-al initialization
                self.__weights['W' + str(i + 1)] = np.random.randn(
                    layers[i], nx) * np.sqrt(2 / nx)
            else:
                # He-et-al initialization
                self.__weights['W' + str(i + 1)] = np.random.randn(
                    layers[i], layers[i - 1]) * np.sqrt(2 / layers[i - 1])

            # Zero initialization
            self.__weights['b' + str(i + 1)] = np.zeros((layers[i], 1))

    @property
    def L(self):
        """Number of layers in the neural network"""
        return self.__L

    @property
    def cache(self):
        """Intermediary values of the network"""
        return self.__cache

    @property
    def weights(self):
        """Hold all weights"""
        return self.__weights

    def forward_prop(self, X):
        """Forward propagation of the neural network"""
        self.__cache["A0"] = X
        for i in range(1, self.__L + 1):
            W = self.__weights['W' + str(i)]
            b = self.__weights['b' + str(i)]
            A = self.__cache['A' + str(i - 1)]
            z = np.matmul(W, A) + b
            sigmoid = 1 / (1 + np.exp(-z))
            self.__cache["A" + str(i)] = sigmoid
        return self.__cache["A" + str(self.__L)], self.__cache

    def cost(self, Y, A):
        """Calculate the cost"""
        cost = - ((Y * np.log(A)) + (1 - Y) * np.log(1.0000001 - A))
        mean_cost = np.mean(cost)
        return mean_cost

    def evaluate(self, X, Y):
        """Evaluate the neural network"""
        output, _ = self.forward_prop(X)
        cost = self.cost(Y, output)
        predict = np.where(output >= 0.5, 1, 0)
        return predict, cost

    def gradient_descent(self, Y, cache, alpha=0.05):
        """Perform gradient descent"""
        m = Y.shape[1]

        for i in range(self.__L, 0, -1):
            A_prev = cache["A" + str(i - 1)]
            A = cache["A" + str(i)]
            W = self.__weights["W" + str(i)]

            if i == self.__L:
                dz = A - Y
            else:
                dz = da * (A * (1 - A))
            db = dz.mean(axis=1, keepdims=True)
            dw = np.matmul(dz, A_prev.T) / m
            da = np.matmul(W.T, dz)
            self.__weights['W' + str(i)] -= alpha * dw
            self.__weights['b' + str(i)] -= alpha * db
