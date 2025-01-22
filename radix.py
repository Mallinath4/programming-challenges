# Helper function to do counting sort based on the current digit place (exp)
def counting_sort(arr, exp):
    n = len(arr)
    
    # Output array to store sorted numbers based on the current digit
    output = [0] * n
    # Initialize count array
    count = [0] * 10  # For digits 0 to 9
    
    # Count the occurrences of each digit in the current place
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    
    # Accumulate the count array to get the actual positions
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build the output array
    for i in range(n - 1, -1, -1):  # Traverse the input array in reverse to maintain stability
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    
    # Copy the sorted array back to arr
    for i in range(n):
        arr[i] = output[i]

# Main function to implement radix sort
def radix_sort(arr):
    # Find the maximum number to determine the number of digits
    max_num = max(arr)
    
    # Do counting sort for every digit (exp represents the current digit place: 1, 10, 100, etc.)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Taking input from the user
def main():
    # Get input from the user as a string of integers separated by spaces
    user_input = input("Enter integers separated by spaces: ")
    
    # Split the input string into a list of strings, then convert each to an integer
    arr = list(map(int, user_input.split()))
    
    print("Unsorted array:", arr)
    
    # Call the radix_sort function to sort the array
    radix_sort(arr)
    
    # Print the sorted array
    print("Sorted array:", arr)

# Run the main function
if __name__ == "__main__":
    main()
