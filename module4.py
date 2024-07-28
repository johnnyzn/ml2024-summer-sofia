def main():
    # Ask for the number of inputs N
    N = int(input("Enter a positive integer N: "))
    
    # Ensure N is positive
    if N <= 0:
        print("N should be a positive integer.")
        return
    
    # Read N numbers one by one
    numbers = []
    for i in range(N):
        num = int(input(f"Enter number {i+1}: "))
        numbers.append(num)
    
    # Ask for the integer X
    X = int(input("Enter an integer X: "))
    
    # Check if X is in the list of numbers
    try:
    	# Adding 1 to convert it to 1-based index
        index = numbers.index(X) + 1  
        print(index)
    except ValueError:
        print(-1)

if __name__ == "__main__":
    main()
