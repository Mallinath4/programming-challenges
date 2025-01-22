class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self,data):
        self.stack.append(data)
        print(f"Pushed {data} onto the stack.")
        
    def pop(self):
        if self.is_empty():
            print("Stack Underflow. No element to pop.")
            return None
        popped_elements = self.stack.pop()
        print("Popped {popped_element} from the stack.")
        return popped_elements
    
    def peek(self):
        if self.is_empty():
            print("Stack is Empty")
            return None
        print(f"Top element is {self.stack[-1]}")
        self.stack[-1]
    
    
    def is_empty(self):
        return len(self.stack) == 0
    
    # Display all elements in the stack
    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return
        print("Stack elements are:", " -> ".join(map(str, reversed(self.stack))))

# Main function to test stack operations
def main():
    stack = Stack()
    
    while True:
        print("\nMenu:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Check if stack is empty")
        print("5. Display")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            data = int(input("Enter data to push onto stack: "))
            stack.push(data)
        elif choice == '2':
            stack.pop()
        elif choice == '3':
            stack.peek()
        elif choice == '4':
            if stack.is_empty():
                print("Stack is empty.")
            else:
                print("Stack is not empty.")
        elif choice == '5':
            stack.display()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    