# PA 3 - AVL Trees

## Assignment Instructions

### Delete operations
Write a program that implements and tests an AVL tree `delete(data)` method. If the data is in the tree, the method finds the node containing `data`, removes it, and rebalances the tree, returning `True` once it does so. If the data is not in the tree the method returns `False`

Similar to BSTs the `delete(data)` method would need a recursive `remove(node)` method to remove the node containing the data. It's similar to a BST `remove` method except you need to make sure the tree is balanced as well


### Testing
Test your implementation by adding and removing the following items
```python
mytree = AVLTree()

mytree.put(131)
mytree.put(121)
mytree.put(122)
mytree.put(132)
mytree.put(115)
mytree.put(415)
mytree.put(321)
mytree.put(315)
mytree.put(111)

print("pre-order traversal:", end = " ")
mytree.pre_order_traversal()

print("level-order traversal:", end = " ")
mytree.level_order_traversal()
#expected output: 122, 115, 132, 111, 121, 131, 321, 315, 415

# no AVL delete implemented!!
del mytree[122]

print("pre-order traversal after delete:", end = " ")
mytree.pre_order_traversal()

print("level-order traversal after delete:", end = " ")
mytree.level_order_traversal()
```

### Tree Visualization
Visualize the tree using Python `pydot` module
- Define a field `self.graph` within the AVLTree class, initialize it to `None` within the constructor
- Define methods `visualize(file)` and `visualize_helper(node)` methods within the AVLTree class
- The `visualize(file)` method should initialize the `self.graph` field to a new graph object using `Graph()` constructor method. It should also add root node to the graph plot and call `visualize_helper(node)` with root node as an argument. Finally the the `visualize(file)` should render and save the tree visualization as a png
- The `visualize(node)` method should recursively add tree nodes and their parent-child relationships (edges) to `self.graph` for visualization
