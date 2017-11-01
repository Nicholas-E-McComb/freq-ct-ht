import numpy as np

#ref: hash_object = hashlib.md5(b'Hello World')

class hashtable:


    def __init__(self):
        self.primes = [11, 19, 41, 79, 163, 317, 641, 1279, 2557, 5119, 10243, 20479, 40961, 81919, 163841, 327673]
        self.numElems = 0                       #Number of hashed elements
        self.capacity = self.primes[0]      #Number of "bins" in the hash table
        self.capIndex = 0                   #Keeps track of where in the primes array the capacity is
        #self.table = np.empty(self.capacity, dtype = object)
        #for i in np.nditer(self.table,flags=["refs_ok"],op_flags=["readwrite","allocate"]): i = []
        #self.valuesTable = np.empty(self.capacity, dtype = object)
        #for i in np.nditer(self.valuesTable,flags=["refs_ok"],op_flags=["readwrite","allocate"]): i = []
        self.table = np.empty(self.capacity, dtype=object)
        self.table.fill([])
        self.table = np.frompyfunc(list,1,1)(self.table)
        self.valuesTable = np.empty(self.capacity, dtype=object)
        self.valuesTable.fill([])
        self.valuesTable = np.frompyfunc(list,1,1)(self.table)


        #Checks if the specified key is present in the hash table
        #
        #Input:
        #   key = the key you want to search for
    def contains(self,key):
        bin_num = hash(key) % self.capacity
        if key in self.table[bin_num]:
            return True
        else:
            return False


        #maps the specified key to to the specified value in the table
        #
        #Inputs
        #   value = the value you wish to put into the hash table
        #   key = the above value's associated key
    def put(self,key,value):
        bin_num = hash(key) % self.capacity
        #If the table already contains the specified key, overwrite the value, otherwise append the key/value to their respective lists
        if self.contains(key):
            slot = self.table[bin_num].index(key)
            self.valuesTable[bin_num][slot] = value
        else:
            self.table[bin_num].append(key)
            self.valuesTable[bin_num].append(value)
            self.numElems += 1

        if self.numElems / self.capacity > .75:
            self.rehash()


        #Finds the specified key in the hash table and returns its associated value.  If the hash table does not contain
        #the specified key, this function returns zero
        #
        #Input
        #   key = the key you want to search for
    def get(self,key):
        bin_num = (hash(key)) % self.capacity
        if self.contains(key):
            slot = self.table[bin_num].index(key)
            return self.valuesTable[bin_num][slot]
        else:
            return 0;

        #Deletes the specified value and its associated key from the hash table
        #
        #Input
        #   key = the key you want to delete from the table
    def delete(self,key):
        if self.contains(key):
            bin_num = hash(key) % self.capacity
            slot = self.table[bin_num].index(key)
            self.table[bin_num].remove(key)
            del self.valuesTable[bin_num][slot]
        else:
            print("error: specified word not found")

        #Creates a new hash table with a larger size and hashes every key in the existing hash table to the new one
    def rehash(self):
        if(self.primes[self.capIndex] < 200000):
            self.capIndex += 1
            newInd = self.primes[self.capIndex]
            self.capacity =  self.primes[self.capIndex]
        else:
            return
        tempKeys = np.copy(self.table)
        tempVals = np.copy(self.valuesTable)
        self.table = np.empty(self.capacity, dtype=object)
        self.table.fill([])
        self.table = np.frompyfunc(list,1,1)(self.table)
        self.valuesTable = np.empty(self.capacity, dtype=object)
        self.valuesTable.fill([])
        self.valuesTable = np.frompyfunc(list,1,1)(self.table)
        self.numElems = 0
        for i,hbin in enumerate(tempKeys):
            for j,element in enumerate(hbin):
                key = hbin[j]
                value = tempVals[i][j]
                self.put(key,value)

        #Returns the number of keys present in the array (i.e. the number of unique elements that have been inserted)
    def size(self):
        return self.numElems
