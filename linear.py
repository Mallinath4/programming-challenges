def linearsearch(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1


def main():
    arr = [10,20,30,40,50,60]
    target = int(input("Enter the number"))
    
    result = linearsearch(arr,target)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in the list")

if __name__=="__main__":
    main()

    