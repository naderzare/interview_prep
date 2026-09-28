# 01 · Two pointers

**Recognize:** sorted input · pair target · palindrome from both ends · in-place filtering. Decide what moving one pointer safely rules out.

```text
sorted [1, 3, 5, 8], target 9
        L        R    1+8=9 ✓
```

**Why:** In a sorted array, if `a[L] + a[R]` is too small, pairing `a[L]` with anything left of `R` is also too small. Discard `L`; the symmetric rule discards `R` when too large.

```python
left, right = 0, len(a) - 1
while left < right:
    total = a[left] + a[right]
    if total == target: return [left, right]
    if total < target: left += 1
    else: right -= 1
```

## Choose the variation

| Pointers | Use when | Why it works |
| --- | --- | --- |
| Opposite ends | Sorted pair sum, palindrome, container area | An ordering rule or limiting side tells you which end cannot improve the answer. |
| Read + write, same direction | Remove duplicates or filter in place | Read examines every item; write marks the compacted valid prefix. |
| Slow + fast | Linked-list cycle or middle | Different speeds expose a cycle or let slow reach the midpoint. |

**Another trace — compact duplicates:** In sorted `[1,1,2,2,3]`, keep `write=1`. Read `1` (skip), `2` (write at index 1), `2` (skip), `3` (write at index 2) → valid prefix `[1,2,3]`, length `3`. The prefix before `write` is always deduplicated.

**Watch:** The sorted-pair proof needs sorted data. Define whether pointers may meet. With duplicates, decide whether you want one pair, unique pairs, or all indices. An in-place write pointer has a different invariant.

**Anchors:** [Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) · [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) · [Container With Most Water](https://leetcode.com/problems/container-with-most-water/).
