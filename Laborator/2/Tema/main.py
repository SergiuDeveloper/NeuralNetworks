#!/usr/bin/python3.8

import _pickle
import gzip
from datetime import datetime

import numpy as np
import concurrent.futures


def verify_classification(w, b, validation_set, error):
    overall_error = 0

    for i in range(len(validation_set[0])):
        x = validation_set[0][i]
        correct_value = validation_set[1][i]

        y = np.multiply(w, x) + b
        output = activation_function(y)

        result = sum(output.astype(int)) / len(output)

        if (result >= 0.5) != correct_value:
            overall_error += 1

    overall_error /= len(validation_set)

    return overall_error <= error


def activation_function(y):
    return y > 0


def perceptron_train(digit, training_set, validation_set, epochs, learning_rate, error):
    fair_classification = False

    w = np.full((28 * 28), 20.)
    b = 20.

    initial_epochs = epochs
    while not fair_classification and epochs > 0:
        print("Digit ", digit, ", epoch ", initial_epochs - epochs + 1)

        fair_classification = True

        for i in range(len(training_set[0])):
            x = training_set[0][i]
            correct_value = np.full((28 * 28), training_set[1][i]).astype(float)

            y = sum(np.multiply(w, x)) + b
            output = activation_function(y).astype(float)

            w += np.multiply((correct_value - output), x) * learning_rate
            b += (correct_value - output) * learning_rate

        if fair_classification:
            fair_classification = verify_classification(w, b, validation_set, error)

        epochs -= 1

    return w, b


if __name__ == '__main__':
    with gzip.open('Dataset/mnist.pkl.gz', 'rb') as dataset_file:
        training_set, validation_set, test_set = _pickle.load(dataset_file, encoding='bytes')

    begin_time = datetime.now()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(perceptron_train,
                                   i,
                                   (training_set[0], [t == i for t in training_set[1]]),
                                   (validation_set[0], [t == i for t in validation_set[1]]),
                                   10,
                                   0.1,
                                   0.05
                                   ) for i in range(10)]

    perceptron_results = [f.result() for f in futures]

    overall_accuracy = 0
    for i in range(len(test_set[0])):
        correct_output = test_set[1][i]
        data = test_set[0][i]

        output = 0
        top_accuracy = 0

        for j in range(len(perceptron_results)):
            w = perceptron_results[j][0]
            b = perceptron_results[j][1]

            current_result = sum(np.multiply(w, data)) + b
            current_result = sum(current_result.astype(int)) / len(current_result)

            if current_result > top_accuracy:
                top_accuracy = current_result
                output = j

        if output == correct_output:
            overall_accuracy += 1

    overall_accuracy /= len(test_set[0])

    print("Overall accuracy: ", overall_accuracy)

    end_time = datetime.now()

    print("Script execution time: ", end_time - begin_time)
