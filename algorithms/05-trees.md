# 05 · Trees

**Recognize:** parent/child structure · subtree answers · level-by-level work · ordered BST search. First decide DFS or BFS and what each visit returns.

```text
      4
     / \
    2   7       DFS: finish child subtrees
   / \          BFS: [4] → [2,7] → [1,3]
  1   3
```

**Why:** A tree has one path from root to each node, so DFS can combine child results without a visited set. BFS's queue processes nodes by increasing depth.

```python
def dfs(node):
    if not node: return 0
    left, right = dfs(node.left), dfs(node.right)
    return 1 + max(left, right)  # replace combine step per problem
```

## Choose the traversal

| Traversal | Visit order | Use when |
| --- | --- | --- |
| DFS preorder | node → left → right | Pass state from parent to child; serialize or copy a tree. |
| DFS postorder | left → right → node | Compute subtree sizes, depths, or other child results first. |
| DFS inorder | left → node → right | Read a BST in sorted order. |
| BFS | one level, then the next | Need level groups or the shallowest matching node. |

**Another trace — inorder:** In the tree above, `left → node → right` visits `1,2,3,4,7`. That order is sorted because it is a **BST**; an arbitrary binary tree has no such promise. To validate a BST, carry allowed `(low, high)` bounds down to every descendant.

**Watch:** Null children and single-node trees. For BST validation, compare against inherited lower/upper bounds; checking only immediate children misses deeper violations. Skewed trees use O(n) DFS stack space.

**Anchors:** [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) · [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) · [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/).
