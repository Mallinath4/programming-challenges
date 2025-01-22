import math

def jumpsearch(arr,target):
    n= len(arr)
    step = int(math.sqrt(n))
    prev = 0
    
    while arr[min(step,n)-1]<target:
        prev = step
        step +=int(math.sqrt(n))
        
        
        if prev >=n:
            return -1
    
    
    for i in range(prev,min(step,n)):
        if arr[i]==target:
            return i
    
    return -1


def main():
    arr = [10,20,30,40,50,60,70]
    target = int(input("Enter the number:"))
    
    result = jumpsearch(arr,target)
    
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in the list")

if __name__ == "__main__":
    main()