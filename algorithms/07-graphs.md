# 07 · Graphs

**Recognize:** arbitrary connections · reachability · connected groups · cycles · prerequisites. Model nodes and edges before choosing DFS/BFS.

```text
A — B — D
|   |
C — E       visited prevents A→B→E→C→A forever
```

**Why:** From a start node, DFS/BFS follows every reachable edge. Marking a node when discovered keeps each node from being expanded repeatedly: O(V + E) with an adjacency list.

```python
seen = {start}
stack = [start]                 # use deque for BFS
while stack:
    node = stack.pop()
    for neighbor in graph[node]:
        if neighbor not in seen:
            seen.add(neighbor)
            stack.append(neighbor)
```

## Choose the tool

| Goal | Tool | Why? |
| --- | --- | --- |
| Reachability/components | DFS or BFS + visited | Expand each reachable node once; restart for unvisited components. |
| Shortest path in **unweighted** graph | BFS queue | First discovery uses the fewest edges. |
| Prerequisite order / directed cycle | Topological sort (indegrees) | Remove zero-indegree nodes; leftover nodes imply a cycle. |
| Repeated connectivity as edges arrive | Disjoint set union | Join groups and query whether nodes share a group. |

**Another trace — BFS distance:** In the picture, start at `A`: level 0 `[A]`, level 1 `[B,C]`, level 2 includes `[D,E]`. So `D` is two edges away via `A→B→D`. DFS can reach `D`, but its first route is not guaranteed shortest.

**Watch:** Disconnected components need an outer loop over all nodes. Directed edges differ from undirected ones. For cycle detection in directed graphs, a single visited set is insufficient; track the active path or use indegrees.

**Anchors:** [Number of Islands](https://leetcode.com/problems/number-of-islands/) · [Clone Graph](https://leetcode.com/problems/clone-graph/) · [Course Schedule](https://leetcode.com/problems/course-schedule/).
