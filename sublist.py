class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
def sublistsearch(main_list,sublist):
    
    if sublist is None:
        return True
    
    if main_list is None:
        return False
    
    current_main = main_list
    while current_main is not None:
        current_sublist = sublist
        temp_main = current_main
        
        while temp_main is not None and current_sublist is not None and temp_main.data == current_sublist.data:
            temp_main = temp_main.next
            current_sublist = current_sublist.next 
        
        if current_sublist is None:
            return True
        
        current_main = current_main.next 
    
    return False

def print_list(head):
    current = head
    while current:
        print(current.data, end='->')
        current = current.next
    print("None")
    

def create_linked_list(arr):
    if not arr:
        return None
    
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next
    return head


def main():
    main_list = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
    sublist = create_linked_list([4, 5, 6])
    
    print("Main List:")
    print_list(main_list)
    
    print("\nSublist:")
    print_list(sublist)
    
    if sublistsearch(main_list, sublist):
        print("\nSublist found in main list!")
    else:
        print("\nSublist not found in main list.")

if __name__ == "__main__":
    main()
    
        