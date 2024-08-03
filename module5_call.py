from module5_mod import DataProcessor
def main():
    # Create an instance of DataProcessor
    processor = DataProcessor()
    
    # Ask the user for input N
    try:
        N = int(input("Enter a positive integer N: "))
    except:
        print("Please enter a valid integer instead of other characters.")
        exit()
    
    # Initialize data
    try:
        processor.initialize_data(N)
    except ValueError as e:
        print(e)
        return

    # Ask the user for input X
    X = int(input("Enter an integer X: "))
    
    # Search for X and output the result
    result = processor.search_data(X)
    print(result)

if __name__ == "__main__":
    main()
