# 00 · Hashmap

**Recognize:** "Have I seen this?" · frequency counts · key → value · complement lookup. Trade memory for near-constant-time average lookup.

```text
target 9, nums [2, 7, 11]
see 2 → need 7; store {2: 0}
see 7 → need 2; found index 0
```

**Why:** The map summarizes the useful part of the prefix. For Two Sum, before index `i`, it contains earlier values only; checking `target - x` first prevents reusing the same element.

```python
seen = {}                       # value -> index (or count)
for i, x in enumerate(nums):
    if target - x in seen:
        return [seen[target - x], i]
    seen[x] = i
```

## Choose the variation

| Need | Map stores | Why this version? |
| --- | --- | --- |
| Find a partner | value → earlier index | One complement lookup replaces a scan of all earlier values. |
| Count or group | key → count/list | Equal keys share one bucket; use a sorted word or letter-count tuple for anagrams. |
| Count subarrays with sum `k` | prefix sum → frequency | A previous prefix `p - k` makes the current subarray sum `k`, even with negative values. |

**Another trace — prefix counts:** For `[1, 2, 1]`, `k=3`, start `{0: 1}`. Prefixes `1, 3, 4` look for `-2, 0, 1`; the last two searches each find one earlier prefix → **2 subarrays**: `[1,2]`, `[2,1]`. Query before adding the current prefix so an empty subarray is not counted.

**Watch:** Pick the right key (value, prefix sum, canonical string). Check before insert when indices must differ. Duplicates and missing keys matter. Hash lookup is average O(1), not a sorting guarantee.

**Anchors:** [Two Sum](https://leetcode.com/problems/two-sum/) · [Group Anagrams](https://leetcode.com/problems/group-anagrams/) · [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) (prefix counts).
