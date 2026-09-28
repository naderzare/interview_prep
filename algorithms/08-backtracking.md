# 08 · Backtracking

**Recognize:** enumerate all valid combinations, permutations, or paths; each step makes a choice and later undoes it.

```text
subsets of [a,b]
[] ─skip a→ [] ─skip b→ []
 │           └take b→ [b]
 └take a→ [a] ─skip b→ [a]
             └take b→ [a,b]
```

**Why:** Each decision branch covers one set of possibilities. A path records current choices; undo restores exactly the state the sibling branch expects.

```python
def dfs(start):
    answer.append(path.copy())
    for i in range(start, len(nums)):
        path.append(nums[i])
        dfs(i + 1)
        path.pop()
dfs(0)
```

## Choose the decision tree

| Output | Next choice | Why this shape? |
| --- | --- | --- |
| Subsets/combinations | Continue from `i + 1` | Order is irrelevant; never revisit earlier choices. |
| Permutations | Choose any unused item | Order matters, so each position has fresh candidates. |
| Combinations with reuse | Recurse from `i` | The same item may be chosen again. |
| Constrained paths | Try legal next steps; undo after | Prune a branch as soon as it cannot reach a valid answer. |

**Another trace — reuse changes the tree:** With candidates `[1,2]` and target `4`, keeping the next start at `i` permits `[1,1,1,1]`, `[1,1,2]`, `[2,2]`. Using `i + 1` would forbid repeats and miss all three. Stop when the remaining target is `0`; with positive candidates, prune when it goes below `0`.

**Watch:** Copy the path when saving it. Choose the correct next index (`i + 1` means no reuse). Skip duplicate branches when unique outputs are required. Prune only when a branch cannot produce a valid answer.

**Anchors:** [Subsets](https://leetcode.com/problems/subsets/) · [Permutations](https://leetcode.com/problems/permutations/) · [Combination Sum](https://leetcode.com/problems/combination-sum/).
