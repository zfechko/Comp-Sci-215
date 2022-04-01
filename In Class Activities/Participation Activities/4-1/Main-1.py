###
# Simple Demo Application for Binary Heap
# Author: Srini Badri
# Version: 1.0
###

from Heap import BinaryHeap
import random

def main():
    h = BinaryHeap()

    for i in range(1, 11):
        x = random.randint(1, 100)
        h.insert(x)

    for i in range(20, 14, -1):
        h.insert(i)

    print("Original number of items in the priority list:", len(h))
    print("Priority list:", h)

    h.remove(15)
    print("Priority list after remove:", h)

    print("Top 5 priority items:")
    for i in range(1, 6):
        print("item:", h.del_min())
        print("Priority List:", h)
    print()

    print("Updated number of items in the priority list - Updated:", len(h))
    print("Updated priority list:", h)

if __name__ == "__main__":
    main()
