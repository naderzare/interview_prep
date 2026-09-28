# 03 · Binary search

**Recognize:** sorted values or a monotone predicate: `false false true true`. Seek a boundary, not just an exact value.

```text
capacity:  1  2  3  4  5  6
feasible:  N  N  N  Y  Y  Y
                     ↑ first yes
```

**Why:** The predicate cannot turn false again after it becomes true. Testing `mid` safely discards half the candidates while preserving the first true answer.

```python
lo, hi = 0, len(a)            # search first index with a[i] >= target
while lo < hi:                # answer stays in [lo, hi]
    mid = (lo + hi) // 2
    if a[mid] >= target: hi = mid
    else: lo = mid + 1
return lo                     # can equal len(a)
```

## Choose the variation

| Search for | Predicate / decision | Why this version? |
| --- | --- | --- |
| Exact value | Compare `a[mid]` with target | Return on equality; otherwise discard the impossible sorted half. |
| First/last occurrence | First `>= target` / first `> target` | Boundary searches handle duplicates; last equal is one before first `>`. |
| Smallest feasible answer | Can the task be done with candidate `mid`? | If feasible stays feasible for larger candidates, find the first `True`. |

**Another trace — duplicates:** In `[1,3,3,7]`, first `>= 3`: test index `2` (`3`, keep left half), then `1` (`3`, keep left half), then `0` (`1`, discard). `lo=1` is the first `3`. This also returns insertion position when the target is absent.

**Watch:** State the interval and whether the answer is guaranteed. Use `hi = mid` for a possible answer, `lo = mid + 1` for a rejected one. For "minimum feasible" problems, prove monotonicity and pick valid bounds.

**Anchors:** [Binary Search](https://leetcode.com/problems/binary-search/) · [Search Insert Position](https://leetcode.com/problems/search-insert-position/) · [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/).
