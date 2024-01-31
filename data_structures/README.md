# Data Structures
A data structure is a way of organizing and storing data in a computer so that it can be accessed and used efficiently. Mentioned below are data structures used in python and those which are used in fundamental to all languages.

## Fundamental to Python
- _List_: a mutable ordered collection of elements which can be of any data type.
- _Tuple_: an immutable ordered collection of elements which an contains different data types.
- _Set_: an unordered collection of unique elements which can be of any data type.
- _Dictionary_: a collection of key-value pairs where each key is unique, immutable, can be of any type. The key-value pairs are mutable after creation.

### Time Complexities
- *List and Tuples:*

- <img src="https://github.com/sreeharsha-rav/sw_basics/blob/main/images/list_bigO.png" width = 60% height = 60%>

- *Dictionary:*

- <img src="https://github.com/sreeharsha-rav/sw_basics/blob/main/images/dict_bigO.png" width = 60% height = 60%>

- *Set:*

- <img src="https://github.com/sreeharsha-rav/sw_basics/blob/main/images/set_bigO.png" width = 60% height = 60%>


## Fundamental to all languages
- Arrays: In python, arrays can be implemented using built-in list data structure or using the array module from NumPy. NumPy arrays are faster than it's list implementation.
- Linked Lists: Elements are not stored at contiguous location, instead elements are linked using pointers. Variants: Doubly Linked Lists.
- Stack: Elements follow last in, first out(LIFO) protocol where the latest added element is eligible to be removed first.
- Queue: Elements follow first in, first out(FIFO) protocol.
- Hash maps: Stores key-value pairs for efficient assignment and retrieval of data. Using key we can get associated the value/data.

## Non-Linear Data Structures
- Trees: a tree is a hierachical data structure that consists of nodes connected by edges. Each node can have multiple children. In python, there are different kinds of trees that can be implemented:
    - General Tree: Unrestricted tree where each node can have any number of children
    - Binary Trees: Tree where each node can have at most two children.
    - Binary Search Tree: Specific type of binary tree where the left child is lesser than it's parent, and right child is greater than it's parent.
    - Heap: Specialized tree-based data structure, that satisfies heap property. There are 2 types of heaps and the heap property is different for each of them. Heaps are implemented as binary heaps, where each node has 2 children.
        - Min-Heap: a complete binary tree where the value of the parent node is greater than or equal to the values of it's children nodes.
        - Max-Heap: A complete binary tree where the value of the parent node is lesser than or equal to the values of it's children nodes.
- Heap: A heap data structure can also be implemented using array. The location of each child or parent derives from a formula using the index:
    - left child = (index * 2) + 1
    - right child = (index * 2) + 2
    - parent = (index - 1) / 2  -> *not used on the root!*

### Time Complexities

<img src="https://github.com/sreeharsha-rav/sw_basics/blob/main/images/fund_bigO.png" width = 60% height = 60%>