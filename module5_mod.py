class DataProcessor:
    def __init__(self):
        self.numbers = []

    def initialize_data(self, n):
        """Initialize the data with N numbers."""
        if n <= 0:
            raise ValueError("N must be a positive integer.")
        
        for i in range(n):
            try:
                num = int(input(f"Enter number {i+1}: "))
            except:
                print("Please enter a valid integer instead of other characters.")
                exit()
            self.insert_data(num)

    def insert_data(self, num):
        """Insert a number into the data set."""
        self.numbers.append(num)

    def search_data(self, x):
        """Search for X in the data and return its 1-based index or -1 if not found."""
        try:
            index = self.numbers.index(x) + 1  # Convert to 1-based index
            return index
        except ValueError:
            return -1
