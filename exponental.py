def binary_search(arr, low, high, target):
    while low <= high:
        mid = (low + high) // 2
        # Check if the target is at the middle
        if arr[mid] == target:
            return mid
        # If target is smaller, discard the right half
        elif arr[mid] > target:
            high = mid - 1
        # If target is larger, discard the left half
        else:
            low = mid + 1
    return -1

def exponential_search(arr, target):
    # If the target is at the first position
    if arr[0] == target:
        return 0
    
    n = len(arr)
    i = 1
    
    # Find range for binary search by repeatedly doubling `i`
    while i < n and arr[i] <= target:
        i *= 2
    
    # Perform binary search within the range [i//2, min(i, n-1)]
    return binary_search(arr, i // 2, min(i, n - 1), target)

# Test the exponential search function
def main():
    arr = [3, 7, 12, 19, 23, 35, 42, 47, 53, 61, 68, 73, 80]  # Sorted array
    target = int(input("Enter the element to search: "))
    
    result = exponential_search(arr, target)
    
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in the list")

if __name__ == "__main__":
    main()
