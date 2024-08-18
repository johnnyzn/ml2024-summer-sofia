# Ning Zhang
# 2024 Summer MSCS2202-1: Machine Learning
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

class DataProcessor:
    def __init__(self):
        self.points = np.array([])

    def initialize_data(self, n):
        """Initialize the data with N (x, y) points."""
        if n <= 0:
            raise ValueError("N must be a positive integer.")
        
        points = []
        for i in range(n):
            x = float(input(f"Enter x value for point {i+1}: "))
            y = float(input(f"Enter y value for point {i+1}: "))
            points.append([x, y])
        
        self.points = np.array(points)

    def insert_data(self, x, y):
        """Insert a point (x, y) into the data set."""
        if self.points.size == 0:
            self.points = np.array([[x, y]])
        else:
            self.points = np.vstack([self.points, [x, y]])

    def calculate_variance(self):
        """Calculate the variance of the y-values (labels)."""
        if self.points.size == 0:
            return None
        y_values = self.points[:, 1]
        return np.var(y_values)

class KNNRegression:
    def __init__(self, k):
        self.k = k
        self.model = KNeighborsRegressor(n_neighbors=k)

    def fit(self, X, y):
        """Fit the k-NN model using the provided dataset."""
        self.model.fit(X, y)

    def predict(self, X):
        """Predict the y-value for the given x using the fitted model."""
        return self.model.predict(X)

def main():
    # Create an instance of DataProcessor
    processor = DataProcessor()
    
    # Ask the user for input N (number of points)
    N = int(input("Enter a positive integer N: "))
    
    # Initialize data with N (x, y) points
    try:
        processor.initialize_data(N)
    except ValueError as e:
        print(e)
        return
    
    # Calculate and display the variance of y-values
    variance = processor.calculate_variance()
    if variance is not None:
        print(f"Variance of the labels (y-values) in the training data: {variance}")
    
    # Ask the user for input k
    k = int(input("Enter a positive integer k: "))
    
    # Check if k <= N
    if k > N:
        print("Error: k cannot be greater than the number of points (N).")
        return
    
    # Ask the user for input X
    X_input = float(input("Enter a real number X: "))
    
    # Prepare the data for fitting the model
    X = processor.points[:, 0].reshape(-1, 1)
    y = processor.points[:, 1]
    
    # Create and train the k-NN regression model
    knn_regressor = KNNRegression(k)
    knn_regressor.fit(X, y)
    
    # Predict the y-value for the input X
    y_pred = knn_regressor.predict(np.array([[X_input]]))
    
    # Output the prediction
    print(f"The predicted Y value for X = {X_input} using k-NN Regression with k = {k} is: {y_pred[0]}")

if __name__ == "__main__":
    main()
