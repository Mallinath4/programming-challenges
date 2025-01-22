def countsort(arr):
    if len(arr)==0:
        return arr
    
    min_val = min(arr)
    max_val = max(arr)
    
    count_range = max_val - min_val +1
    count = [0]* count_range
    
    for num in arr:
        count[num - min_val] +=1
    
    for i in range(1,len(count)):
        count[i] += count[i-1]
        
    output = [0]* len(arr)
    
    for num in reversed(arr):
        output[count[num - min_val]-1] = num
        count[num - min_val] -=1
        
    for i in range(len(arr)):
        arr[i] = output[i]
        
def main():
    user_input = input("Enter integers separated by spaces: ")
    
    # Split the input string into a list of strings, then convert each to an integer
    arr = list(map(int, user_input.split()))
    
    print("Unsorted array:", arr)
    
    # Call the counting_sort function to sort the array
    countsort(arr)
    
    # Print the sorted array
    print("Sorted array:", arr)

# Run the main function
if __name__ == "__main__":
    main()