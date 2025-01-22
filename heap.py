def heapfiy(arr,n,i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    
    if left <n and arr[left]> arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
        
    if largest != i:
        
        arr[i], arr[largest] = arr[largest], arr[i]
        
        heapfiy(arr,n,largest)
        

def heapsort(arr):
    n = len(arr)
    
    for i in range(n//2-1, -1, -1):
        heapfiy(arr,n,i)
        
    
    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        
        heapfiy(arr,i,0)


def main():
    user_input = input("Enter numbers separated by spaces: ")
    
    # Split the input string into a list of strings, then convert each to an integer
    arr = list(map(int, user_input.split()))
    
    print("Unsorted array:", arr)
    
    # Call the shell_sort function to sort the array
    heapsort(arr)
    
    # Print the sorted array
    print("Sorted array:", arr)

# Run the main function
if __name__ == "__main__":
    main()       