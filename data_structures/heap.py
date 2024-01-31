from random import randrange

# class representation of a min heap data structure using array data structure
class MinHeap:
    def __init__(self):
        self.heapList = []
        self.size = 0
    
    # method to push a new element into the heap
    def pushVal(self, value):
        print("Adding {0} to {1}".format(value, self.heapList))
        self.heapList.append(value)
        self.size += 1
        self.heapifyUp()

    # method to heapify up the heap
    def heapifyUp(self):
        print("Heapifying up...")
        child_idx = self.size - 1
        parent_idx = (child_idx - 1) // 2
        while parent_idx >= 0 and self.heapList[parent_idx] > self.heapList[child_idx]:
            print("Swapping {0} with {1}".format(self.heapList[parent_idx], self.heapList[child_idx]))
            self.heapList[parent_idx], self.heapList[child_idx] = self.heapList[child_idx], self.heapList[parent_idx]
            child_idx = parent_idx
            parent_idx = (child_idx - 1) // 2
        print("Heap restored", self.heapList)
    
    # method to pop the minimum element from the heap
    def popVal(self):
        if self.size == 0:
            print("No elements in the heap to remove")
            return
        print("Removing {0} from {1}".format(self.heapList[0], self.heapList))
        self.heapList[0] = self.heapList[self.size - 1] # replace the root with the last element
        self.heapList.pop()  # remove the last element
        self.size -= 1
        print("Heap after replacing root with last element", self.heapList)
        self.heapifyDown()
    
    # method to heapify down the heap
    def heapifyDown(self):
        print("Heapifying down...")
        parent_idx = 0
        left_child_idx = 2 * parent_idx + 1
        right_child_idx = 2 * parent_idx + 2
        # while the parent has at least one child
        while left_child_idx < self.size:
            min_child_idx = left_child_idx  # assume left child is the minimum
            # if right child exists and is less than left child
            if right_child_idx < self.size and self.heapList[right_child_idx] < self.heapList[left_child_idx]:
                min_child_idx = right_child_idx
            # if the parent is less than or equal to the minimum child
            if self.heapList[parent_idx] <= self.heapList[min_child_idx]:
                break
            print("Parent {0} is greater than minimum child {1}".format(self.heapList[parent_idx], self.heapList[min_child_idx]))
            print("Swapping {0} with {1}".format(self.heapList[parent_idx], self.heapList[min_child_idx]))
            self.heapList[parent_idx], self.heapList[min_child_idx] = self.heapList[min_child_idx], self.heapList[parent_idx]
            # move to the next level
            parent_idx = min_child_idx
            left_child_idx = 2 * parent_idx + 1
            right_child_idx = 2 * parent_idx + 2
        print("Heap restored", self.heapList)

# Test the functionality of min heap
if __name__ == "__main__":
    minHeap = MinHeap()
    # push random numbers into the heap
    randomNums = [randrange(1, 101) for n in range(6)]
    for val in randomNums:
        minHeap.pushVal(val)

    # pop the minimum element from the heap till the heap is empty
    while minHeap.size > 0:
        minHeap.popVal()