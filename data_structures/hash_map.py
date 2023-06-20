# Program to demonstrate working of a Hash Map
# NOTE: This implementation of Hash Map does not handle hash value collisions

class HashMap:
    def __init__(self, size):
        self.size = size    # size of hash map
        self.array = [None for element in range(size)]  # using array to simulate storage for hash map i.e. hash bucket

    def hash(self, key):
        # generate hash code for given input key
        key_in_bytes = key.encode() # convert string into bytes
        hash_code = sum(key_in_bytes)   # hash code = sum of bytes in key
        return hash_code
    
    def compressor(self, hash_code):
        # generate hash value based on size of hash map
        return hash_code % self.size
    
    def assign(self, key, value):
        # assign a key-value pair to the hash map
        hash_code = self.hash(key)
        hash_val = self.compressor(hash_code)
        self.array[hash_val] = value    # assign value to it's key's hash value

    def retrieve(self, key):
        # retrieve value from hash map given it's corresponding key
        hash_code = self.hash(key)
        hash_val = self.compressor(hash_code)
        return self.array[hash_val] # retrieve value from hash map

# DRIVER PROGRAM
if __name__ == "__main__":
    hm = HashMap(10)    # initialize a hash map of size 10

    # assign key-value pairs
    hm.assign("name", "Adam")
    hm.assign("age", "25")
    hm.assign("sex", "male")
    
    # retrieve values given key
    print(hm.retrieve("name"))
    print(hm.retrieve("age"))
    print(hm.retrieve("sex"))