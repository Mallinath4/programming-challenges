class Node:
    def __init__(self,data):
        self.data =data
        self.next = None

class Queuelinkedlist:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def enqueue(self,data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            print(f"Enqueued {data} into queue")
            return
        self.rear.next = new_node
        self.rear = new_node
        print(f"Enqueued {data} into queue")
        return
    
    def dequeue(self):
        if self.front is None:
            print("Queue Underflow. No element to dequeue.")
            return None
        dequeued_node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
            print(f"Dequeued {dequeued_node.data} from queue")
        return dequeued_node.data
    
    def peek(self):
        if self.front is None:
            print("Queue is empty.")
            return None
        print(f"Front element is {self.front.data}")
        return self.front.data
    
    # Check if the queue is empty
    def is_empty(self):
        return self.front is None
    
    # Display the queue elements
    def display(self):
        if self.front is None:
            print("Queue is empty.")
            return
        current = self.front
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))

# Main function to test queue operations
def main():
    queue = Queuelinkedlist()
    
    while True:
        print("\nMenu:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Check if queue is empty")
        print("5. Display")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            data = int(input("Enter data to enqueue into queue: "))
            queue.enqueue(data)
        elif choice == '2':
            queue.dequeue()
        elif choice == '3':
            queue.peek()
        elif choice == '4':
            if queue.is_empty():
                print("Queue is empty.")
            else:
                print("Queue is not empty.")
        elif choice == '5':
            queue.display()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
        