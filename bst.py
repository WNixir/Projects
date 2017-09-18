class BTNode(object):
    """A node in a binary tree."""

    def __init__(self, value, left=None, right=None):
        """(BTNode, int, BTNode, BTNode) -> NoneType
        Initialize this node to store value and have children left and right,
        as well as depth 0.
        """
        self.value = value
        self.left = left
        self.right = right
        self.d = 0

    def __str__(self):
        return self._str_helper("")

    def _str_helper(self, indentation=""):
        """(BTNode, str) -> str
        Return a "sideways" representation of the subtree rooted at this node,
        with right subtrees above parents above left subtrees and each node on
        its own line, preceded by as many TAB characters as the node's depth.
        """
        ret = ""

        if(self.right is not None):
            ret += self.right._str_helper(indentation + "\t") + "\n"
        ret += indentation + str(self.value) + "\n"
        if(self.left is not None):
            ret += self.left._str_helper(indentation + "\t") + "\n"
        return ret

    def set_depth(self, depth):
        '''(BTNode, int) -> NoneType
        '''
        # set the depth for itself
        self.d = depth
        # set the depth for all nodes in left subtree
        if self.left is not None:
            self.left.set_depth(depth+1)
        # set the depth for all nodes in right subtree
        if self.right is not None:
            self.right.set_depth(depth+1)

    def leaves_and_internals(self):
        '''(BTNode) -> Tuple of Sets
        '''
        leaves = set()
        internals = set()

        # node is a leaf if no left or right child
        if (self.left is None) and (self.right is None):
            leaves.add(self.value)
        else:
            # recurse for left tree
            if self.left is not None:
                leaves, internals = self.left.leaves_and_internals()
            # recurse for right sub tree
            if self.right is not None:
                templeaves, tempinternals = self.right.leaves_and_internals()
                # combine the 2 sets
                leaves = leaves.union(templeaves)
                internals = internals.union(tempinternals)
            internals.add(self.value)
        return leaves, internals

    def sum_to_deepest(self):
        '''(BTNode) -> int
        '''
        total = self.sum_to_deepest_helper()
        return total[1]

    def sum_to_deepest_helper(self, depth=0, total=0):
        '''(BTNode) -> int

        Sum from root to leaf of the longest path
        '''
        # base case: no left and right children
        if self.left is None and self.right is None:
            total += self.value
            result = depth, total
        else:
            depth += 1
            total += self.value

            # recurse on the left subtree
            if self.left is not None:
                result = self.left.sum_to_deepest_helper(depth, total)
            # store the result in a temp variable
            lresult = result

            # then recurse on the right subtree
            if self.right is not None:
                result = self.right.sum_to_deepest_helper(depth, total)
            # store the result in temp variable
            rresult = result

            # compare the return the bigger value
            if lresult > rresult:
                result = lresult
            else:
                result = rresult
        return result
