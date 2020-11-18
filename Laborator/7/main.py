#!/usr/bin/python3.8

from NeuralNetwork import NeuralNetwork
import pickle
import gzip
import numpy as np


if __name__ == '__main__':
    f = gzip.open('mnist.pkl.gz', 'rb')
    train_set, validation_set, test_set = pickle.load(f, encoding='latin1')
    f.close()

    X_train = train_set[0]
    X_test = np.array([
        np.array([
            1. if i == y else 0. for i in range(10)
        ])
        for y in train_set[1]
    ])

    X_valid_data = validation_set[0]
    X_valid_test = np.array([
        np.array([
            1. if i == y else 0. for i in range(10)
        ])
        for y in validation_set[1]
    ])

    X_test_data = test_set[0]
    X_test_test = np.array([
        np.array([
            1. if i == y else 0. for i in range(10)
        ])
        for y in test_set[1]
    ])

    neural_network = NeuralNetwork().fit(X_train, X_test, X_valid_data, X_valid_test, X_test_data, X_test_test, 10000, 0.0001)
    print(neural_network.compute_accuracy(X_train, X_test))
