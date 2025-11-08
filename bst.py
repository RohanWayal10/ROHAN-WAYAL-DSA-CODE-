print("ROHAN WAYAL")

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        else:
            pass
        return root

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self._minValueNode(root.right)
            root.key = temp.key
            root.right = self._delete(root.right, temp.key)
        return root

    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        else:
            return self._search(root.right, key)

    def inorder(self):
        res = []
        self._inorder(self.root, res)
        return res

    def _inorder(self, root, res):
        if root:
            self._inorder(root.left, res)
            res.append(root.key)
            self._inorder(root.right, res)

    def preorder(self):
        res = []
        self._preorder(self.root, res)
        return res

    def _preorder(self, root, res):
        if root:
            res.append(root.key)
            self._preorder(root.left, res)
            self._preorder(root.right, res)

    def postorder(self):
        res = []
        self._postorder(self.root, res)
        return res

    def _postorder(self, root, res):
        if root:
            self._postorder(root.left, res)
            self._postorder(root.right, res)
            res.append(root.key)

    def depth(self):
        return self._depth(self.root)

    def _depth(self, root):
        if root is None:
            return 0
        left_depth = self._depth(root.left)
        right_depth = self._depth(root.right)
        return max(left_depth, right_depth) + 1

    def mirror(self):
        self._mirror(self.root)

    def _mirror(self, root):
        if root:
            root.left, root.right = root.right, root.left
            self._mirror(root.left)
            self._mirror(root.right)

    def copy(self):
        new_tree = BST()
        new_tree.root = self._copy(self.root)
        return new_tree

    def _copy(self, root):
        if root is None:
            return None
        new_node = Node(root.key)
        new_node.left = self._copy(root.left)
        new_node.right = self._copy(root.right)
        return new_node

    def display_parents_with_children(self):
        result = []
        self._display_parents_with_children(self.root, result)
        return result

    def _display_parents_with_children(self, root, result):
        if root:
            children = []
            if root.left:
                children.append(root.left.key)
            if root.right:
                children.append(root.right.key)
            if children:
                result.append((root.key, children))
            self._display_parents_with_children(root.left, result)
            self._display_parents_with_children(root.right, result)

    def leaf_nodes(self):
        leaves = []
        self._leaf_nodes(self.root, leaves)
        return leaves

    def _leaf_nodes(self, root, leaves):
        if root:
            if root.left is None and root.right is None:
                leaves.append(root.key)
            self._leaf_nodes(root.left, leaves)
            self._leaf_nodes(root.right, leaves)

    def level_order(self):
        res = []
        if self.root is None:
            return res
        queue = [self.root]
        while queue:
            level_size = len(queue)
            level_nodes = []
            for _ in range(level_size):
                node = queue.pop(0)
                level_nodes.append(node.key)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level_nodes)
        return res


bst = BST()

for val in [50, 30, 20, 40, 70, 60, 80, 70]:  # 70 duplicate ignored
    bst.insert(val)

print("Inorder Traversal:", bst.inorder())
print("Preorder Traversal:", bst.preorder())
print("Postorder Traversal:", bst.postorder())

key = 40
found = bst.search(key)
print(f"Search {key}:", "Found" if found else "Not Found")

print("Depth of tree:", bst.depth())

print("Parents with children:", bst.display_parents_with_children())

print("Leaf nodes:", bst.leaf_nodes())

print("Level order traversal:", bst.level_order())

bst_copy = bst.copy()
print("Copy - Inorder Traversal:", bst_copy.inorder())

bst.mirror()
print("Mirror - Inorder Traversal:", bst.inorder())

bst.delete(30)
print("After deleting 30, Inorder Traversal:", bst.inorder())
