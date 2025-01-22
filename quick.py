# Helper function to partition the array
def partition(arr, low, high):
    pivot = arr[high]  # Choose the last element as the pivot
    i = low - 1        # Pointer for the smaller element
    
    # Rearrange the elements based on the pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements
    
    # Place the pivot in the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Main function to implement quicksort
def quick_sort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pi = partition(arr, low, high)
        
        # Recursively sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Taking input from the user
def main():
    # Get input from the user as a string of integers separated by spaces
    user_input = input("Enter integers separated by spaces: ")
    
    # Split the input string into a list of strings, then convert each to an integer
    arr = list(map(int, user_input.split()))
    
    print("Unsorted array:", arr)
    
    # Call the quick_sort function to sort the array
    quick_sort(arr, 0, len(arr) - 1)
    
    # Print the sorted array
    print("Sorted array:", arr)

# Run the main function
if __name__ == "__main__":
    main()
