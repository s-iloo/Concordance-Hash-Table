from posixpath import join
from re import L



class HashTable:

    def __init__(self, table_size): # add appropriate attributes, NO default size
        ''' Initializes an empty hash table with a size that is the smallest
            prime number that is >= table_size (i.e. if 10 is passed, 11 will 
            be used, if 11 is passed, 11 will be used.)'''
        
        newtablesize = self.next_prime(table_size)
        
        self.table_size = newtablesize
        self.hash = [None] * self.table_size
        self.numItems = 0

    def insert(self, key, value=None):
        ''' Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is any object (e.g. Python List).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is is in the table, the new value replaces the existing value.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased
        to the next prime greater than 2*table_size.'''
        #print(key)
        index = self.horner_hash(key) % self.table_size
        #print(self.horner_hash(key))
        #tempIndex = index
        #print(self.hash[tempIndex][0])
        i = 1
        if self.in_table(key):
            self.hash[index] = (key, value)
            self.numItems -= 1
        #print(index)
        while self.hash[index] != None: #collision
            index = (self.horner_hash(key) + (i * i)) % self.table_size
            i += 1
        self.hash[index] = (key, value)
        self.numItems += 1
        if self.get_load_factor() > 0.5: #increases size of hashtable CHECK THIS IDK IF THIS RIGHT
            newTableSize = self.next_prime(2*self.table_size)
            newHash = [None] * newTableSize
            #MY REHASH IS WRONG RIGHT NOW
            for j in self.hash:
                if j != None:
                    #rehash into self.newHash
                    index = self.horner_hash(j[0]) % newTableSize
                    #print(i[0], index)
                    numCol = 1
                    while newHash[index] != None: #a collision
                        index = (self.horner_hash(j[0]) + (numCol * numCol)) % newTableSize
                        numCol += 1
                    #no collision
                    newHash[index] = (j[0], j[1])
 
            self.table_size = newTableSize
            self.hash = newHash

                #rehash        
    def horner_hash(self, key):
        ''' Compute the hash value by using Horner’s rule, as described in project specification.'''
        '''n = min(8, len(key))
        hashVal = 0
        for i in range(len(key)):
            hashVal += ord(key[i]) * (31 ** (n - 1 - i))

        return hashVal'''
        n = min(8,len(key))
        hashVal = 0 
        for i in range(n): 
            hashVal += ord(((key))[i]) * (31**(n - 1 ))
            n -=1 
        return hashVal

    def next_prime(self, n):
        ''' Find the next prime number that is > n.'''
        if n == 1:
            return 2

        if n > 1:
            for i in range(2, int(n/2)+1):
                if n % i == 0: #it not prime
                    j = 2
                    n += 1
                    while n % j == 0: #while still not prime
                        n += 1  
                        j += 1
            return n



    def in_table(self, key): #fix to make it o(1)
        ''' Returns True if key is in an entry of the hash table, False otherwise.'''
        #keys = [x[0] for x in self.hash if self.hash[x] != None]
        
        if self.numItems == 0:
            return False


        index = self.horner_hash(key) % self.table_size
        #print(index)
        #tempIndex = index
        i = 1
        while self.hash[index] != None:
            if self.hash[index][0] == key:
                return True
            index = (self.horner_hash(key) + (i * i)) % self.table_size
            i += 1
        return False


    def get_index(self, key): #fix this to make it o(1)
        ''' Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None.'''

        if self.in_table(key):
            index = self.horner_hash(key) % self.table_size
            tempIndex = index
            i = 1
            if self.hash[index][0] == key:
                return index
            else:
                while self.hash[tempIndex][0] != key:
                    tempIndex = (index + i * i) % self.table_size
                    i += 1
                return tempIndex
                
        return None


    def get_all_keys(self):
        ''' Returns a Python list of all keys in the hash table.'''
        keys = []
        for i in self.hash:
            if i != None:
                keys.append(i[0])
        return keys

    def get_value(self, key):
        ''' Returns the value associated with the key. 
        If key is not in hash table, returns None.'''
        if self.in_table(key):
            i = self.get_index(key)
            return self.hash[i][1]
        return None

    def get_num_items(self):
        ''' Returns the number of entries in the table.'''
        return self.numItems
    def get_table_size(self):
        ''' Returns the size of the hash table.'''
        return self.table_size

    def get_load_factor(self):
        ''' Returns the load factor of the hash table (entries / table_size).'''
        return self.numItems/self.table_size 


'''
a = HashTable(7)
a.insert("cat",123)
a.insert("tac",321)
a.insert("act",231)
a.insert("jack",231)
#a.insert("black")
#a.insert("cat", 22)
#print(a.numItems)
print(a.get_table_size()) 
print(a.get_index("cat"))
print(a.in_table("tac"))
print(a.get_all_keys())
#print(a.in_table("tac"))'''