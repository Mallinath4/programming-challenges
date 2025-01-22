# Function to perform Selection Sort
def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Assume the current element is the minimum
        min_index = i
        
        # Find the minimum element in the remaining unsorted array
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Taking input from the user
def main():
    # Get input from the user as a string of numbers separated by spaces
    user_input = input("Enter numbers separated by spaces: ")
    
    # Split the input string into a list of strings, then convert each to an integer
    arr = list(map(int, user_input.split()))
    
    print("Unsorted array:", arr)
    
    # Call the selection_sort function to sort the array
    selection_sort(arr)
    
    # Print the sorted array
    print("Sorted array:", arr)

# Run the main function
if __name__ == "__main__":
    main()
