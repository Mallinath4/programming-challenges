class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"Pushed {data} onto stack")
    
    def pop(self):
        if self.top is None:
            print("Stack is Underflow.No element to pop")
            return None
        popped_node = self.top
        self.top = self.top.next
        print(f"Popped {popped_node.data} from stack")
        return popped_node.data
    
    def peek(self):
        if self.top is None:
            print("Empty Stack:")
            return None
        print(f"Top element is {self.top.data}")
        return self.top.data
    
    def is_empty(self):
        return self.top is None
    
    def display(self):
        if self.top is None:
            print("Empty Stack")
            return
        current = self.top
        elements = []
        
        while current:
            elements.append(str(current.data))
            current = current.next
        print('->'.join(elements))


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
        
    
    
        
        