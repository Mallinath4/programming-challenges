def interpolationsearch(arr,target):
    low = 0
    high = len(arr)-1
    
    while low <=high and target >=arr[low] and target<=arr[high]:
        if low==high:
            if arr[low]==target:
                return low
            return -1
        
        
        mid = low + (target - arr[low])*(high - low)//(arr[high]-arr[low])
        
        if arr[mid]==target:
            return mid
        elif arr[mid]< target:
            low = mid +1
        else:
            high = mid-1
    return -1

def main():
    arr= [10,20,30,40,50,60]
    target = int(input("Enter the number:"))
    
    result = interpolationsearch(arr,target)
    
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in the list")

if __name__ == "__main__":
    main()