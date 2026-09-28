# 06 · Heap

**Recognize:** repeatedly take the smallest/largest live item · keep top `k` while streaming · merge sorted streams. A heap exposes one extreme, not a fully sorted collection.

```text
top 3 of [5, 1, 9, 2, 8]
kept values, shown sorted: [5] → [1,5] → [1,5,9]
              2 replaces 1 → [2,5,9]
              8 replaces 2 → [5,8,9]
```

**Why:** In a size-`k` min-heap, the root is the weakest kept candidate. Any new value larger than it belongs among the top `k`; replacing the root costs O(log k).

```python
import heapq
heap = []
for x in nums:
    if len(heap) < k: heapq.heappush(heap, x)
    elif x > heap[0]: heapq.heapreplace(heap, x)
return heap[0]                 # kth largest, if k is valid
```

## Choose the variation

| Need | Heap setup | Why? |
| --- | --- | --- |
| Kth largest / top `k` | Min-heap of size `k` | Root is the smallest kept item, so it is easy to replace. |
| Repeated largest priority | Max-heap (negate numeric keys in Python) | Each pop gives the current largest without sorting again. |
| Merge `k` sorted streams | Heap of each stream's next item | Pop global minimum, then push only its successor: O(N log k). |

**Another trace — merge streams:** `[1,4]` and `[2,3]`: heap starts with `1,2`; pop `1`, push `4`; pop `2`, push `3`; pop `3`, then `4` → `[1,2,3,4]`. Heap size never exceeds the number of streams.

**Watch:** Python `heapq` is a min-heap; negate values for max behavior. Check `k` and empty input. If you need every element sorted once, sorting may be simpler. For top frequencies, heap entries need the frequency as priority.

**Anchors:** [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) · [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) · [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/).
