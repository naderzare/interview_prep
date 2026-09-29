"""Binary-tree practice. Build small trees by hand to check your answers."""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Example tree used by several questions:
#       4
#      / \
#     2   7
#    / \
#   1   3
def sample_tree():
    """Return a fresh copy, since some questions mutate their input."""
    return TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))


# Question 1: Count nodes.
# Return 0 for an empty tree. Example: sample_tree() -> 5
def count_nodes(root):
    raise NotImplementedError


# Question 2: Maximum depth.
# Count nodes on the longest root-to-leaf path. Example: sample_tree() -> 3
def max_depth(root):
    raise NotImplementedError


# Question 3: Preorder values.
# Return values in node-left-right order. Example: sample_tree() -> [4, 2, 1, 3, 7]
def preorder_values(root):
    raise NotImplementedError


# Question 4: Level-order values.
# Return one list per depth. Example: sample_tree() -> [[4], [2, 7], [1, 3]]
def level_order(root):
    raise NotImplementedError


# Question 5: Same tree.
# Return whether two trees have identical shapes and values.
# Example: (sample_tree(), sample_tree()) -> True;
#          (sample_tree(), TreeNode(4)) -> False
def same_tree(a, b):
    raise NotImplementedError


# Question 6: Invert a tree.
# Swap left and right children at every node, mutate the tree, and return root.
# Example: sample_tree()'s preorder becomes [4, 7, 2, 3, 1].
def invert_tree(root):
    raise NotImplementedError


# Question 7: Root-to-leaf path sum.
# Return True if some root-to-leaf path adds to target.
# Example: (sample_tree(), 7) -> True via 4->2->1;
#          (sample_tree(), 6) -> False
def has_path_sum(root, target):
    raise NotImplementedError


# Question 8: Validate a binary search tree.
# Every node in a left subtree must be smaller than its ancestor, and every
# node in a right subtree larger. Duplicates are invalid.
# Example: sample_tree() -> True
def is_valid_bst(root):
    raise NotImplementedError


# Question 9: Lowest common ancestor in a binary tree.
# p and q are references to two distinct nodes guaranteed to be in root.
# Return their lowest common ancestor node. In sample_tree(), LCA(1, 3) is node 2.
def lowest_common_ancestor(root, p, q):
    raise NotImplementedError


# Question 10: Tree diameter.
# Return the largest number of edges on any path between two nodes; the path
# need not pass through the root. Example: sample_tree() -> 3 (1->2->4->7).
def diameter(root):
    raise NotImplementedError


def check_question_1():
    assert count_nodes(sample_tree()) == 5
    assert count_nodes(None) == 0


def check_question_2():
    assert max_depth(sample_tree()) == 3
    assert max_depth(None) == 0
    assert max_depth(TreeNode(1)) == 1


def check_question_3():
    assert preorder_values(sample_tree()) == [4, 2, 1, 3, 7]
    assert preorder_values(None) == []


def check_question_4():
    assert level_order(sample_tree()) == [[4], [2, 7], [1, 3]]
    assert level_order(None) == []


def check_question_5():
    assert same_tree(sample_tree(), sample_tree()) is True
    assert same_tree(sample_tree(), TreeNode(4)) is False
    assert same_tree(None, None) is True


def check_question_6():
    root = sample_tree()
    assert invert_tree(root) is root
    assert root.left.val == 7 and root.right.val == 2
    assert root.right.left.val == 3 and root.right.right.val == 1


def check_question_7():
    assert has_path_sum(sample_tree(), 7) is True
    assert has_path_sum(sample_tree(), 6) is False
    assert has_path_sum(None, 0) is False


def check_question_8():
    assert is_valid_bst(sample_tree()) is True
    deep_violation = TreeNode(5, TreeNode(1), TreeNode(8, TreeNode(4), TreeNode(9)))
    assert is_valid_bst(deep_violation) is False
    assert is_valid_bst(TreeNode(2, TreeNode(2))) is False


def check_question_9():
    root = sample_tree()
    assert lowest_common_ancestor(root, root.left.left, root.left.right) is root.left
    assert lowest_common_ancestor(root, root.left.left, root.right) is root
    assert lowest_common_ancestor(root, root.left, root.left.left) is root.left


def check_question_10():
    assert diameter(sample_tree()) == 3
    assert diameter(None) == 0
    assert diameter(TreeNode(1)) == 0


if __name__ == "__main__":
    import sys
    question = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    if question not in range(1, 11):
        raise SystemExit("Choose a question from 1 to 10")
    globals()[f"check_question_{question}"]()
    print(f"Question {question}: examples passed")
