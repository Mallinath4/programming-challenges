class Queue:
    def __init__(self):
        self.queue =[]
    
    def enqueue(self,data):
        self.queue.append(data)
        print(f"Enqueued {data} into the queue.")
    
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow. No element to dequeue.")
            return None
        dequeued_element = self.queue.pop(0)  # Remove the first element (front of the queue)
        print(f"Dequeued {dequeued_element} from the queue.")
        return dequeued_element
    
    # Peek operation: View the front element without removing it
    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        print(f"Front element is {self.queue[0]}")
        return self.queue[0]
    
    # Check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0
    
    # Display all elements in the queue
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        print("Queue elements are:", " -> ".join(map(str, self.queue)))

# Main function to test queue operations
def main():
    queue = Queue()
    
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