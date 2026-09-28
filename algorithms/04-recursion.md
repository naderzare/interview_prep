# 04 · Recursion

**Recognize:** A problem contains smaller copies of itself; trees and divide-and-conquer are natural fits. Name the smaller input, base case, and return value.

```text
depth(node)
  ├─ 1 + depth(left)
  └─ 1 + depth(right)
answer = 1 + max(child depths)
```

**Why:** Assume each smaller call returns the promised result. Combine those results for the current input. The base case stops the descent.

```python
def depth(node):
    if node is None: return 0
    return 1 + max(depth(node.left), depth(node.right))
```

## Choose the call shape

| Shape | Example | Use it because… |
| --- | --- | --- |
| One smaller call | `factorial(n) = n * factorial(n-1)` | The answer depends on one shorter chain; the base case ends it. |
| Branching calls | `depth(node)` calls both children | Independent child answers must be combined (here, `1 + max`). |
| Divide and conquer | `power(x,n)` halves `n` | Reusing the half result gives O(log n) calls instead of O(n). |
| Recursion + memo | `ways(n)` reuses `ways(n-1)` and `ways(n-2)` | Cache repeated states so each distinct state is solved once. |
| Traversal with shared state | Visit every node and update a path/result | The goal is to explore, not necessarily to return a value from every call. |

**Another trace — halve the problem:** `power(2,5)` asks for `power(2,2)`, which asks for `power(2,1)`, then `power(2,0)=1`. On the way back: `2`, `4`, then `4² × 2 = 32`. Compute each half **once**; calling it twice loses the O(log n) benefit.

**Watch:** Every path must move toward a base case. Define what an empty input returns. Trace the call stack on a tiny example; Python recursion depth can be a practical limit. If calls revisit the same state, consider memoization.

**Anchors:** [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) · [Pow(x, n)](https://leetcode.com/problems/powx-n/) · [Merge Two Binary Trees](https://leetcode.com/problems/merge-two-binary-trees/).
