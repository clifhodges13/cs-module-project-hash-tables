class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.hash_table = [None] * self.capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        non_null_entries = 0
        for item in self.hash_table:
            if item != None:
                non_null_entries += 1
        return non_null_entries / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for char in key:
            hash = (( hash << 5 ) + hash) + ord(char)
        return hash & 0xFFFFFFFF



    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here

        # Day 1
        # self.hash_table[self.hash_index(key)] = value
        # return value

        # Day 2
        index = self.hash_index(key)
        current = self.hash_table[index]
        
        if current == None:
            self.hash_table[index] = HashTableEntry(key, value)
            return self.hash_table[index].value

        if current.key == key:
            # replace the value
            current.value = value
            return current.value
        
        while current != None:
            # if the key is equal to the key passed:
            if current.next == None:
                # Create a new node and place it after the current node
                current.next = HashTableEntry(key, value)
                return current.next
            elif current.next != None and current.next.key == key:
                current.next.value = value
                return current.next.value
            else:
                current = current.next


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here

        # Day 1
        index = self.hash_index(key)
        if self.hash_table[index]:
            self.hash_table[index] = None
            return
        else:
            print(f'Error: "{key}" not found in table.')

        # Day 2
        # Get the Linked List at the hashed index
        # Search through the Linked List for the key
        # If it exists,
            # Return the value
        # else,
            # Return None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        current = self.hash_table[index]

        # if the item at the current index is None, return None
        if current == None:
            return None
        # else if the current item's key is equal to the key passed,
        elif current.key == key:
            # we've found our key, so return the value!
            return current.value
        # else if the current is not None,
        elif current != None:
            # loop as long as the current's next is not None
            while current != None:
                # at each loop, check if the current item matches the key we passed
                if current.key == key:
                    # if it does, return the value
                    return current.value
                # otherwise
                else:
                    #set the current variable to it's next node, and loop again
                    current = current.next



    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        self.capacity = new_capacity



if __name__ == "__main__":
    ht = HashTable(8)

    # ht.put("line_1", "'Twas brillig, and the slithy toves")
    # ht.put("line_2", "Did gyre and gimble in the wabe:")
    # ht.put("line_3", "All mimsy were the borogoves,")
    # ht.put("line_4", "And the mome raths outgrabe.")
    # ht.put("line_5", '"Beware the Jabberwock, my son!')
    # ht.put("line_6", "The jaws that bite, the claws that catch!")
    # ht.put("line_7", "Beware the Jubjub bird, and shun")
    # ht.put("line_8", 'The frumious Bandersnatch!"')
    # ht.put("line_9", "He took his vorpal sword in hand;")
    # ht.put("line_10", "Long time the manxome foe he sought--")
    # ht.put("line_11", "So rested he by the Tumtum tree")
    # ht.put("line_12", "And stood awhile in thought.")

    ht.put("key-0", "val-0")
    ht.put("key-1", "val-1")
    ht.put("key-2", "val-2")
    ht.put("key-3", "val-3")
    ht.put("key-4", "val-4")
    ht.put("key-5", "val-5")
    ht.put("key-6", "val-6")
    ht.put("key-7", "val-7")
    ht.put("key-8", "val-8")
    ht.put("key-9", "val-9")

    ht.put("key-0", "new-val-0")
    ht.put("key-1", "new-val-1")
    ht.put("key-2", "new-val-2")
    ht.put("key-3", "new-val-3")
    ht.put("key-4", "new-val-4")
    ht.put("key-5", "new-val-5")
    ht.put("key-6", "new-val-6")
    ht.put("key-7", "new-val-7")
    ht.put("key-8", "new-val-8")
    ht.put("key-9", "new-val-9")

    # print(ht.get('line_1'))

    # print("")

    # # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))
    
    for i in ht.hash_table:
        if i.next is not None:
            print('i.next  ', i.next.value)
        if i is not None:
            print('i       ', i.value)
        if i is None:
            print('None')

    # # Test resizing
    # old_capacity = ht.get_num_slots()
    # print(old_capacity)
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()
    # print(new_capacity)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    print("")
