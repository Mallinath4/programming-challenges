def shellsort(arr):
    n = len(arr)
    
    gap = n//2
    while gap>0:
        for i in range(gap,n):
            temp = arr[i]
            j = i
            
            while j >=gap and arr[j - gap]> temp:
                arr[j] = arr[j - gap]
                
                j -= gap
                
            arr[j] = temp
        
        gap //=2
    
def main():
    user_input = input("Enter numbers separated by spaces: ")
    
    # Split the input string into a list of strings, then convert each to an integer
    arr = list(map(int, user_input.split()))
    
    print("Unsorted array:", arr)
    
    # Call the shell_sort function to sort the array
    shellsort(arr)
    
    # Print the sorted array
    print("Sorted array:", arr)

# Run the main function
if __name__ == "__main__":
    main()