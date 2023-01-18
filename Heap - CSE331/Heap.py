    
class Heap:
    """
    A heap-based priority queue
    Items in the queue are ordered according to a comparison function
    """

    def __init__(self, comp):
        """
        Constructor
        :param comp: A comparison function determining the priority of the included elements
        """
        self.comp = comp
        self.heapList = []
        self.currentSize = 0
        # Added Members

    def __len__(self):
        """
        :return: returns the size of the current list - must run in constant time
        """
        return self.currentSize #return size

    def peek(self):
        """
        looks at the element, returns it, doesn't remove
        If heap is empty throw error - must run in constant time
        :return:
        """
        if len(self.heapList) == 0: #if empty throw error
            raise IndexError
        return self.heapList[0]

    def insert(self, item):
        """
        This function places our item into the heap and makes sure this doesn't
        violate the heap order property - must run in log n time
        :param item: item we are inserting into heap
        :return:
        """

        self.heapList.append(item) #append
        self.currentSize += 1 #increase list
        self.__upHeap__(self.currentSize-1)  #make sure the heap follows heap order property

    def extract(self):
        """
        This function peeks the item called and returns it
        If heap is empty throw error - must run in log n time
        :return: item called
        """
        if len(self.heapList) == 0: #if empty throw error
            raise IndexError
        else: #from slides
            min = self.heapList[0]  #copy first to temp
            self.heapList[0] = self.heapList[-1]  #swap last with first
            self.heapList.pop()  #pop it
            self.currentSize -= 1  #shrink
            self.__heapify__(0)  #apply heapify to make sure heap follows heap order proprty
            return min




    def extend(self, seq):
        """
        Adds all elements of a given sequence to your heapf - must run in (m + n) time
        :param seq:
        :return:
        """
        self.heapList.extend(seq) #extend sequence to list
        self.currentSize += len(seq)  #create room
        middle = self.currentSize // 2  #start from middle, heapify from middle to zero going backwards
        for i in range(0,middle+1):
            self.__heapify__(middle - i)
        pass

    def clear(self):
        """
        Clears the heap - must run in n time
        :return:
        """
        self.heapList = [] #clear list
        self.currentSize = 0  #make size 0
        pass

    def __iter__(self):
        """
        Enumerates all items - must run in n time
        :return:
        """
        for i in self.heapList:  #iterates thru the heap
            yield i

    # Supplied methods

    def __bool__(self):
        """
        Checks if this heap contains items
        :return: True if the heap is non-empty
        """
        return not self.is_empty()

    def is_empty(self):
        """
        Checks if this heap is empty
        :return: True if the heap is empty
        """
        return len(self.heapList) == 0

    def __repr__(self):
        """
        A string representation of this heap
        :return:
        """
        return 'Heap([{0}])'.format(','.join(str(item) for item in self))

    # Added methods

    def __parent__(self,x):
        """
        Finds parent of item
        ::return: parent of item
        """
        return (x-1)//2

    def __upHeap__(self, x):
        """
        Restores the heap order property by comparing item to parents
        :param x: current item
        :return:
        """
        parent = self.__parent__(x)  #set parent
        if x > 0 and self.comp(self.heapList[x], self.heapList[parent]):  #if size isn't 0 and
            parent_temp = self.heapList[parent]                           #out of priority, swap
            self.heapList[parent] = self.heapList[x]
            self.heapList[x] = parent_temp
            self.__upHeap__(parent)





    def __heapify__(self,x):
        """
        Creates the heap
        :param x:  index of the list
        :return: copied from book
        """
        l = self.__left__(x)
        r = self.__right__(x)
        if l < self.currentSize and self.comp(self.heapList[l],self.heapList[x]):
            small = l
        else:
            small = x
        if r < self.currentSize and self.comp(self.heapList[r], self.heapList[small]):
            small = r
        if small != x:
            temp_x = self.heapList[x]
            self.heapList[x] = self.heapList[small]
            self.heapList[small] = temp_x
            self.__heapify__(small)

    def __left__(self, x):
        """
        :param x: item that we want left object of
        :return: item left of object passed in
        """
        return (2*x)+1 #from book

    def __right__(self, x):
        """
        :param x: item that we want right object of
        :return: item right of object passed in
        """
        return (2*x)+2 #from book



# Required Non-heap member function

def find_median(seq):
    """
    Finds the median (middle) item of the given sequence.
    Ties are broken arbitrarily. - find must be faster than sorting the sequence and finding the middle item,
    use heaps in solution
    :param seq: an iterable sequence
    :return: the median element
    """
    if not seq: #if empty throw error
        raise IndexError
    min_heap = Heap(lambda a, b: a <= b)
    min_heap.extend(seq) #extend sequence to list
    for i in range(0,len(seq) // 2):
        min_heap.extract()
    return min_heap.heapList[0]
