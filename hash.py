# Node class to store key-value pairs in the chain
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# HashTable class using chaining to handle collisions
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  # Initialize the hash table with empty slots

    # Hash function to map keys to table indices
    def hash_function(self, key):
        return hash(key) % self.size

    # Insert key-value pair into the hash table
    def insert(self, key, value):
        index = self.hash_function(key)
        new_node = Node(key, value)
        
        # Insert the node into the chain at the index
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current:
                # If the key already exists, update its value
                if current.key == key:
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = new_node

    # Search for a value by key
    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None  # Key not found

    # Delete a key-value pair from the hash table
    def delete(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return
            prev = current
            current = current.next
        
        print(f"Key {key} not found")

    # Print the hash table for visualization
    def display(self):
        for i in range(self.size):
            print(f"Index {i}: ", end="")
            current = self.table[i]
            while current:
                print(f"({current.key}: {current.value}) -> ", end="")
                current = current.next
            print("None")

# Test the hash table
def main():
    h = HashTable(10)  # Create a hash table of size 10
    
    # Insert key-value pairs
    h.insert("apple", 100)
    h.insert("banana", 200)
    h.insert("orange", 300)
    h.insert("grape", 400)
    
    # Display the hash table
    print("Hash Table:")
    h.display()
    
    # Search for values
    print("\nSearching for 'banana':", h.search("banana"))
    print("Searching for 'grape':", h.search("grape"))
    print("Searching for 'pear':", h.search("pear"))  # Should return None

    # Delete a key-value pair
    h.delete("banana")
    print("\nAfter deleting 'banana':")
    h.display()

if __name__ == "__main__":
    main()
