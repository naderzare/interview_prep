# 09 · Dynamic programming

**Recognize:** overlapping smaller states + a rule that combines them; ask "what must I know to decide the next answer?" Useful for counts, best values, and existence.

```text
climb 4 stairs, steps 1 or 2
ways(4) = ways(3) + ways(2)
          3        + 2       = 5
```

**Why:** Define `dp[state]` precisely. A recurrence covers every allowed last choice without double-counting; compute each state once. Base cases ground the recurrence.

```python
def climb(n):
    if n <= 1: return 1
    prev2, prev1 = 1, 1       # ways(0), ways(1)
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev1 + prev2
    return prev1
```

## Choose the state shape

| State | Example | Use it because… |
| --- | --- | --- |
| One index `dp[i]` | House Robber: best through house `i` | Each answer depends on nearby earlier answers. |
| Index + capacity/amount | Coin Change or knapsack | The remaining budget changes which choices are possible. |
| Two positions `dp[i][j]` | Longest Common Subsequence | The answer depends on progress through **both** inputs. |
| Top-down memo | Sparse or awkward state graph | Recurse naturally and cache only states reached. |

**Another trace — best value:** House Robber on `[2,7,9,3,1]`: best prefix values are `2,7,11,11,12`. At each house, `best[i] = max(best[i-1], value[i] + best[i-2])`: skip it or take it and skip its neighbor. The final answer is `12` (houses worth `2+9+1`).

**Watch:** Write state meaning before code. Check base cases and impossible states. Choose computation order so dependencies already exist. Greedy choices are not automatically safe; explain why a local choice would stay optimal before using one.

**Anchors:** [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) · [House Robber](https://leetcode.com/problems/house-robber/) · [Coin Change](https://leetcode.com/problems/coin-change/) · [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/).
