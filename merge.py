def mergesort(left,right):
    sorted_array = []
    i=j=0
    
    while i < len(left) and j< len(right):
        if left[i]< right[j]:
            sorted_array.append(left[i])
            i +=1
        
        else:
            sorted_array.append(right[j])
            j +=1
            
    while i< len(left):
        sorted_array.append(left[i])
        i +=1
        
    while j< len(right):
        sorted_array.append(right[j])
        j +=1
        
    return sorted_array

def merge(arr):
    if len(arr) <=1:
        return arr
    
    mid = len(arr)//2
    
    left_half = merge(arr[:mid])
    right_half = merge(arr[mid:])
    
    
    return mergesort(left_half,right_half)


def main():
    user_input = input("Enter numbers separated by spaces: ")
    
    # Split the input string into a list of strings, then convert each to an integer
    arr = list(map(int, user_input.split()))
    
    print("Unsorted array:", arr)
    
    # Call the merge_sort function to sort the array
    sorted_arr = merge(arr)
    
    # Print the sorted array
    print("Sorted array:", sorted_arr)

# Run the main function
if __name__ == "__main__":
    main()