def febonaccisearch(arr,target):
    n = len(arr)
    
    fib2 =0
    fib1 = 1
    
    fibM = fib1 + fib2
    
    while fibM <n:
        fib2 = fib1
        fib1 = fibM
        fibM = fib1 + fib2
        
    offset = -1
    
    while fibM >1:
        i = min(offset + fib2, n-1)
        
        if arr[i]<target:
            fibM = fib1
            fib1 = fib2
            fib2 = fibM - fib1
            offset = i
            
        elif arr[i]>target:
            fibM = fib2
            fib1= fib1 - fib2
            fib2= fibM - fib1
        
        else:
            return i
        
    if fib1 and arr[offset +1]==target:
        return offset + 1
    
    return -1

def main():
    arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]  # Sorted array
    target = int(input("Enter the element to search: "))
    
    result = febonaccisearch(arr, target)
    
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in the list")

if __name__ == "__main__":
    main()