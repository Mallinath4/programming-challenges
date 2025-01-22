class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Singlelinkedlist:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
            
    def insert_at_position(self,pos,data):
        if pos ==0:
            print("Empty list")
            return
        new_node = Node(data)
        if pos ==1:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        for _ in range(pos - 2):
            if not temp:
                print("position is out of bound")
                return
            temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            
    def delete_at_begining(self):
        if not self.head:
            print("List is empty")
            return
        self.head = self.head.next
    
    def delete_at_end(self):
        if not self.head:
            print("List is empty")
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
        
    def delete_at_position(self,pos):
        if pos<1:
            print("Empty list")
            return
        if not self.head:
            print("empty list")
            return
        if pos==1:
            self.head = self.head.next
            return
        temp = self.head
        for _ in range(pos -2):
            if not temp:
                print("position is out of bound")
                return
            temp = temp.next
        if not temp.next:
            print("Position out of range")
            return
        temp.next = temp.next.next
        
    def display(self):
        if not self.head:
            print("Empty list")
            return
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")
        
        
def menu():
    sll = Singlelinkedlist()
    
    while True:
        print("\nOptions:")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Insert at Specific Position")
        print("4. Delete at Beginning")
        print("5. Delete at End")
        print("6. Delete at Specific Position")
        print("7. Display List")
        print("8. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data to insert at the beginning: "))
            sll.insert_at_beginning(data)

        elif choice == 2:
            data = int(input("Enter data to insert at the end: "))
            sll.insert_at_end(data)

        elif choice == 3:
            data = int(input("Enter data to insert: "))
            position = int(input("Enter position to insert at: "))
            sll.insert_at_position(data, position)

        elif choice == 4:
            sll.delete_at_begining()

        elif choice == 5:
            sll.delete_at_end()

        elif choice == 6:
            position = int(input("Enter position to delete from: "))
            sll.delete_at_position(position)

        elif choice == 7:
            sll.display()

        elif choice == 8:
            print("Exiting program.")
            break

        else:
            print("Invalid choice, please try again.")

# Start the program
menu()
            
            
            