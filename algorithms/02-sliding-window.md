# 02 · Sliding window

**Recognize:** contiguous substring/subarray · longest/shortest valid range · add right, remove left. Ask whether validity can be restored by shrinking.

```text
"abca" unique-character window
 [abc]a → duplicate a → move left past old a → [bca]
```

**Why:** Maintain a fact about `[left, right]` (counts, sum, distinct count). Each boundary moves forward at most `n` times, so many windows take O(n) despite the nested loop.

```python
left = 0
for right, x in enumerate(items):
    add(x)
    while invalid():
        remove(items[left])
        left += 1
    update_answer(left, right)
```

## Choose the variation

| Window | Use when | Move left when… |
| --- | --- | --- |
| Fixed length | Every candidate has length `k` | Length exceeds `k`; remove one as each new item enters. |
| Variable, longest valid | Maximize a range satisfying a rule | It becomes invalid; then record the valid length. |
| Variable, shortest valid | Minimize a range meeting a threshold | It is valid: record it, then shrink to seek a shorter one. |

**Another trace — shortest sum:** For positive `[2,3,1,2,4,3]`, target `7`, the first valid window is `[2,3,1,2]` (length 4). Shrink and continue; later `[4,3]` is valid (length 2), the answer. Positive values make the sum fall as left moves; with negatives, that rule is unreliable.

**Watch:** Update the answer only when the window has the needed validity. Distinguish "shrink while invalid" (longest valid) from "record while valid, then shrink" (shortest valid). A sum-based shrinking rule may fail with negative numbers.

**Anchors:** [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) · [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) · [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/).
