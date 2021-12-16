# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        # Write your code here.
        first_parent_index = (len(array) - 1 - 1) // 2
        for current_index in reversed(range(first_parent_index)):
            self.siftDown(current_index, len(array)-1, array)

        return array

    def siftDown(self, current_index, end_index, heap):
        # Write your code here.
        left_child = 2 * current_index + 1
        while left_child <= end_index:
            right_child = 2 * current_index + 2 if 2 * current_index + 2 <= end_index else None

            if right_child and heap[right_child] < heap[left_child]:
                index_to_swap = right_child
            else:
                index_to_swap = left_child

                
            if heap[current_index] > heap[index_to_swap]:
                self.swap(current_index, index_to_swap, heap)
                current_index = index_to_swap
                left_child = 2 * current_index + 1
            else:
                break

    def siftUp(self, current_index, heap):
        # Write your code here.
        parent_index = (current_index - 1) // 2
        while current_index > 0 and heap[current_index] < heap[parent_index]:
            self.swap(current_index, parent_index, heap)
            current_index = parent_index
            parent_index = (current_index - 1) // 2


    def peek(self):
        # Write your code here.
        return self.heap[0]

    def remove(self):
        # Write your code here.
        self.swap(0, len(self.heap) - 1, self.heap)
        removed_item = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return removed_item

    def insert(self, value):
        # Write your code here.
        self.heap.append(value)
        self.siftUp(len(self.heap)-1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]