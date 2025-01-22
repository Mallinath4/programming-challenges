class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Circularlinkedlist:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
        else:
            new_node.next = self.head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            self.head = new_node
    
    
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
    
    
    def insert_at_position(self,pos,data):
        if pos ==0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        count = 0
        
        while current.next != self.head and count < pos -1:
            current = current.next
            count +=1
        if current.next ==self.head and count != pos - 1:
            print("position is out of bound")
        else:
            new_node.next = current.next
            current.next = new_node
            
    def delete_at_beginning(self):
        if self.head is None:
            print("Empty list")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head
            self.head = self.head.next
    
    def delete_at_end(self):
        if self.head is None:
            print("Empty list")
            return
        if self.head.next == self.head:
            self.head =None
        else:
            current = self.head
            prev = None
            while current.next != self.head:
                prev = current
                current = current.next
            prev.next = self.head
    
    def delete_at_position(self, position):
        if self.head is None:
            print("List is empty.")
            return
        if position == 0:
            self.delete_at_beginning()
            return
        
        current = self.head
        prev = None
        count = 0
        
        while current.next != self.head and count < position:
            prev = current
            current = current.next
            count += 1
        
        if current.next == self.head and count != position:
            print("Position out of bounds.")
        else:
            prev.next = current.next
    
    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        nodes = []
        current = self.head
        while True:
            nodes.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        print("->".join(nodes))

def main():
    circular_list = Circularlinkedlist()
    while True:
        print("\nMenu:")
        print("1. Insert at beginning")
        print("2. Insert at end")
        print("3. Insert at specific position")
        print("4. Delete at beginning")
        print("5. Delete at end")
        print("6. Delete at specific position")
        print("7. Display")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            data = int(input("Enter data to insert at beginning: "))
            circular_list.insert_at_beginning(data)
        elif choice == '2':
            data = int(input("Enter data to insert at end: "))
            circular_list.insert_at_end(data)
        elif choice == '3':
            position = int(input("Enter the position to insert at: "))
            data = int(input("Enter data to insert at specific position: "))
            circular_list.insert_at_position(position, data)
        elif choice == '4':
            circular_list.delete_at_beginning()
        elif choice == '5':
            circular_list.delete_at_end()
        elif choice == '6':
            position = int(input("Enter the position to delete at: "))
            circular_list.delete_at_position(position)
        elif choice == '7':
            circular_list.display()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
            
            
            
            
                