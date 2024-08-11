import numpy as np

class KNNRegressor:
    def __init__(self):
        self.points = np.empty((0, 2))
    def initialize_data(self, n):
        """Initialize the data with N points."""
        if n <= 0:
            raise ValueError("N must be a positive integer.")
        
        for i in range(n):
            x = float(input(f"Enter x value for point {i+1}: "))
            y = float(input(f"Enter y value for point {i+1}: "))
            self.insert_data(x, y)

    def insert_data(self, x, y):
        """Insert a new point into the data set."""
        new_point = np.array([[x, y]])
        self.points = np.vstack((self.points, new_point))

    def calculate_knn(self, X, k):
        """Calculate the k-NN regression result for a given X value."""
        if k > len(self.points):
            raise ValueError("k cannot be greater than the number of points N.")
        
        # Calculate the distances between X and all x values in the data
        distances = np.abs(self.points[:, 0] - X)
        
        # Get the indices of the k nearest neighbors
        k_indices = np.argsort(distances)[:k]
        
        # Calculate the mean of the y values of the k nearest neighbors
        knn_result = np.mean(self.points[k_indices, 1])
        
        return knn_result

def main():
    # Create an KNNRegressor object
    regressor = KNNRegressor()
    
    # Ask the user for input N
    N = int(input("Enter a positive integer N: "))
    
    # Initialize data
    try:
        regressor.initialize_data(N)
    except ValueError as e:
        print(e)
        return
    
    k = int(input("Enter a positive integer k: "))
    X = float(input("Enter the X value: "))
    
    # Calculate the k-NN regression result
    try:
        result = regressor.calculate_knn(X, k)
        print(f"The result of k-NN regression is: {result}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
