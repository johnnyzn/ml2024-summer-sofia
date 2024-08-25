simport numpy as np
from sklearn.metrics import precision_score, recall_score

class DataProcessor:
    def __init__(self, n):
        """Initialize the processor with the expected number of points."""
        self.n = n
        self.true_labels = np.zeros(n, dtype=int)
        self.predicted_labels = np.zeros(n, dtype=int)

    def initialize_data(self):
        """Collects N (x, y) points."""
        for i in range(self.n):
            x = int(input(f"Enter true label (0 or 1) for point {i+1}: "))
            if x not in [0, 1]:
                raise ValueError("Labels must be either 0 or 1.")
            y = int(input(f"Enter predicted label (0 or 1) for point {i+1}: "))
            if y not in [0, 1]:
                raise ValueError("Labels must be either 0 or 1.")
            self.true_labels[i] = x
            self.predicted_labels[i] = y

class MetricsCalculator:
    def calculate_precision(true_labels, predicted_labels):
        """Calculate and return the precision score."""
        return precision_score(true_labels, predicted_labels)

    def calculate_recall(true_labels, predicted_labels):
        """Calculate and return the recall score."""
        return recall_score(true_labels, predicted_labels)

def main():
    # Ask the user for input N (number of points)
    N = int(input("Enter a positive integer N: "))
    
    # Create an instance of DataProcessor with N
    processor = DataProcessor(N)
    
    # Initialize data with N (x, y) points
    try:
        processor.initialize_data()
    except ValueError as e:
        print(e)
        return
    
    # Calculate Precision and Recall
    precision = MetricsCalculator.calculate_precision(processor.true_labels, processor.predicted_labels)
    recall = MetricsCalculator.calculate_recall(processor.true_labels, processor.predicted_labels)
    
    # Output the results
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")

if __name__ == "__main__":
    main()
