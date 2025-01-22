def insertionsort(arr):
    n = len(arr)
    
    for i in range(1,n):
        curr = arr[i]
        
        j = i-1
        
        while j>=0 and curr< arr[j]:
            arr[j+1]= arr[j]
            j-=1
            
        arr[j+1] = curr


def main():
    # Get input from the user as a string of numbers separated by spaces
    user_input = input("Enter numbers separated by spaces: ")
    
    # Split the input string into a list of strings, then convert each to an integer
    arr = list(map(int, user_input.split()))
    
    print("Unsorted array:", arr)
    
    # Call the insertion_sort function to sort the array
    insertionsort(arr)
    
    # Print the sorted array
    print("Sorted array:", arr)

# Run the main function
if __name__ == "__main__":
    main()