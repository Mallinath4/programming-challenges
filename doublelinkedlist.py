class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Doublylinkedlist:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def insert_at_end(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
    
    def insert_at_position(self,pos,data):
        if pos ==0:
            print("Empty list")
            return
        new_node = Node(data)
        current = self.head
        for _ in range(pos -2):
            if current is None:
                print("position is out of bound")
                return
            current = current.next
            if current.next is not None:
                current.next.prev = new_node
            current.next = new_node
            new_node.prev = current
                
    def delete_at_beginning(self):
        if self.head is None:
            print("Empty List")
            return
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None
    
    def delete_at_end(self):
        if self.head is None:
            print("Empty List")
            return
        if self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next:
                current = current.next
            current.prev.next = None
            
    
    def delete_at_position(self,pos):
        if pos==0:
            print("Empty List")
            return
        if self.head is None:
            print("Empty List")
            return
        if pos ==1:
            self.delete_at_beginning()
            return
        current = self.head
        for _ in range(pos -2):
            if current is None:
                print("postion is out of Bound")
                return
            current = current.next
            if current.next is None:
                print("postion is out of bound")
                return
            temp = current.next
            current.next = temp.next
            if temp.next is not None:
                temp.next.prev = current
            
    def display_forward(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        print("->".join(nodes))
    
    def display_backward(self):
        nodes =[]
        current = self.head
        while current and current.next :
            current = current.next
        
        while current:
            nodes.append(str(current.data))
            current = current.prev
        print("->".join(nodes))
        
# Main Function to interact with user
def main():
    dll = Doublylinkedlist()

    while True:
        print("\nOptions:")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Insert at Specific Position")
        print("4. Delete at Beginning")
        print("5. Delete at End")
        print("6. Delete at Specific Position")
        print("7. Display List Forward")
        print("8. Display List Backward")
        print("9. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data to insert at the beginning: "))
            dll.insert_at_beginning(data)

        elif choice == 2:
            data = int(input("Enter data to insert at the end: "))
            dll.insert_at_end(data)

        elif choice == 3:
            data = int(input("Enter data to insert: "))
            position = int(input("Enter position to insert at: "))
            dll.insert_at_position(data, position)

        elif choice == 4:
            dll.delete_at_beginning()

        elif choice == 5:
            dll.delete_at_end()

        elif choice == 6:
            position = int(input("Enter position to delete from: "))
            dll.delete_at_position(position)

        elif choice == 7:
            dll.display_forward()

        elif choice == 8:
            dll.display_backward()

        elif choice == 9:
            print("Exiting program.")
            break

        else:
            print("Invalid choice, please try again.")

# Start the program
if __name__ == "__main__":
    main()
                   
        