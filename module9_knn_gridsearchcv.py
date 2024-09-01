# Sofia University ML 9.2 Assignment
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

class DataProcessor:
    def __init__(self, n, m):
        """Initialize the processor with the expected number of points for TrainS and TestS."""
        self.trainS = np.zeros((n, 2))
        self.testS = np.zeros((m, 2))
        self.n = n
        self.m = m

    def initialize_train_data(self):
        """Collects N (x, y) pairs for the training set."""
        for i in range(self.n):
            x = float(input(f"Enter x value for training point {i+1}: "))
            y = int(input(f"Enter y value for training point {i+1}: "))
            if y < 0:
                raise ValueError("Class label y must be a non-negative integer.")
            self.trainS[i] = [x, y]

    def initialize_test_data(self):
        """Collects M (x, y) pairs for the test set."""
        for i in range(self.m):
            x = float(input(f"Enter x value for test point {i+1}: "))
            y = int(input(f"Enter y value for test point {i+1}: "))
            if y < 0:
                raise ValueError("Class label y must be a non-negative integer.")
            self.testS[i] = [x, y]

class KNNClassifier:
    def __init__(self, k_range):
        self.k_range = k_range
        self.best_k = None
        self.best_accuracy = 0

    def fit_and_evaluate(self, trainS, testS):
        """Trains and evaluates the k-NN classifier for different values of k."""
        X_train = trainS[:, 0].reshape(-1, 1)  # Extracting x values from training set
        y_train = trainS[:, 1]  # Extracting y values from training set
        X_test = testS[:, 0].reshape(-1, 1)  # Extracting x values from test set
        y_test = testS[:, 1]  # Extracting y values from test set

        for k in self.k_range:
            knn = KNeighborsClassifier(n_neighbors=k)
            knn.fit(X_train, y_train)
            y_pred = knn.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            if accuracy > self.best_accuracy:
                self.best_accuracy = accuracy
                self.best_k = k

        return self.best_k, self.best_accuracy

def main():
    # Ask the user for input N (number of training points)
    N = int(input("Enter a positive integer N (size of TrainS): "))
    
    # Ask the user for input M (number of test points)
    M = int(input("Enter a positive integer M (size of TestS): "))
    
    # Create an instance of DataProcessor with N and M
    processor = DataProcessor(N, M)
    
    # Initialize the training data (TrainS)
    try:
        processor.initialize_train_data()
    except ValueError as e:
        print(e)
        return
    
    # Initialize the test data (TestS)
    try:
        processor.initialize_test_data()
    except ValueError as e:
        print(e)
        return
    
    # Define the range for k
    k_range = range(1, min(N, 11))
    
    # Create and evaluate the k-NN classifier
    knn_classifier = KNNClassifier(k_range)
    best_k, best_accuracy = knn_classifier.fit_and_evaluate(processor.trainS, processor.testS)
    
    # Output the best k and corresponding test accuracy
    print(f"The best k for k-NN Classification is: {best_k}")
    print(f"The corresponding test accuracy is: {best_accuracy:.4f}")

if __name__ == "__main__":
    main()
