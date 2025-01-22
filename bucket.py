def insertionsort(arr):
    n = len(arr)
    j = 0
    
    for i in range(1,n):
        curr = arr[i]
        j = i-1
        
        while j >=0 and curr <arr[j]:
            arr[j+1] = arr[j]
            
            j -=1
        
        arr[j+1] = curr

def bucketsort(arr):
    n = len(arr)
    if n==0:
        return arr
    
    buckets = [[] for _ in range(n)]
    
    for value in arr:
        index = int(n * value)
        buckets[index].append(value)
    
    for bucket in buckets:
        insertionsort(bucket)
    
    sorted_array =[]
    
    for bucket in buckets:
        sorted_array.extend(bucket)
    
    return sorted_array

def main():
    # Get input from the user as a string of floating-point numbers separated by spaces
    user_input = input("Enter floating-point numbers between 0 and 1 separated by spaces: ")
    
    # Split the input string into a list of strings, then convert each to a float
    arr = list(map(float, user_input.split()))
    
    print("Unsorted array:", arr)
    
    # Call the bucket_sort function to sort the array
    sorted_arr = bucketsort(arr)
    
    # Print the sorted array
    print("Sorted array:", sorted_arr)

# Run the main function
if __name__ == "__main__":
    main()