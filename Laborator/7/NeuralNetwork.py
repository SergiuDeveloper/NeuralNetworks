#!/usr/bin/python3.8

import numpy as np


class NeuralNetwork:
    def __init__(self):
        self.__w_hidden = np.array((0, 0))
        self.__w_output = np.array((0, 0))

    def fit(self, X_train, X_test, max_epochs, learning_rate):
        self.__w_hidden = np.random.uniform(low=-1, high=1, size=(784, 100))
        self.__w_output = np.random.uniform(low=-1, high=1, size=(100, 10))

        momentum = 101 / 100
        for epoch in range(1, max_epochs + 1):
            l1_in, l1_out, l2_in, l2_out = self.__forward_prop(X_train)

            l2_err = l2_out - X_test
            l2_delta = np.dot(l1_out.T, l2_err * self.__sigmoid_derivative(l2_in))

            l1_err = np.dot(l2_err * self.__sigmoid_derivative(l2_in), self.__w_output.T)
            l1_delta = np.dot(X_train.T, self.__sigmoid_derivative(l1_in) * l1_err)

            self.__w_output -= l2_delta * learning_rate
            self.__w_hidden -= l1_delta * learning_rate

            learning_rate *= momentum

            print('Epoch {0}'.format(epoch))
            print('Accuracy = {0}%'.format(self.compute_accuracy(X_train, X_test) * 100))
            print()

        return self

    def predict(self, X):
        return np.argmax(self.__forward_prop(X)[3])

    def compute_accuracy(self, X_test, y_test):
        correct_predictions = 0
        for i in range(len(X_test)):
            if self.predict(X_test[i]) == np.argmax(y_test[i]):
                correct_predictions += 1
        return correct_predictions / len(X_test)

    def __forward_prop(self, X_train):
        l1_in = np.dot(X_train, self.__w_hidden)
        l1_out = self.__sigmoid_activation(l1_in)
        l2_in = np.dot(l1_out, self.__w_output)
        l2_out = self.__sigmoid_activation(l2_in)

        return l1_in, l1_out, l2_in, l2_out

    def __sigmoid_activation(self, val):
        try:
            sig = 1 / (1 + np.exp(-val))
            return sig
        except FloatingPointError:
            return 1

    def __sigmoid_derivative(self, val):
        return self.__sigmoid_activation(val) * (1 - self.__sigmoid_activation(val))
