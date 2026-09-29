"""Graph practice. Inputs use adjacency dictionaries or edge lists as stated."""


# Question 1: Build an undirected adjacency list.
# Nodes are 0..n-1. Return a dict with every node as a key and neighbor lists
# in edge-input order. Example: (3, [(0, 1), (1, 2)])
# -> {0: [1], 1: [0, 2], 2: [1]}
def build_undirected(n, edges):
    raise NotImplementedError


# Question 2: Reachable node count.
# graph is an adjacency dict. Count distinct nodes reachable from start,
# including start. Example: ({0: [1], 1: [0, 2], 2: [1], 3: []}, 0) -> 3
def reachable_count(graph, start):
    raise NotImplementedError


# Question 3: Does a directed path exist?
# graph's neighbor lists represent outgoing edges. Return whether target
# is reachable from start. Example: ({"a": ["b"], "b": [], "c": []}, "a", "c") -> False
def has_directed_path(graph, start, target):
    raise NotImplementedError


# Question 4: Count connected components.
# Undirected graph with nodes 0..n-1; isolated nodes count too.
# Example: (5, [(0, 1), (2, 3)]) -> 3
def count_components(n, edges):
    raise NotImplementedError


# Question 5: Number of islands.
# grid contains "1" for land and "0" for water; horizontal/vertical land
# cells connect. Do not mutate grid. Example: ["110", "010", "001"] -> 2
def island_count(grid):
    raise NotImplementedError


# Question 6: Shortest unweighted path length.
# Return the minimum number of edges from start to target, or -1 if absent.
# graph is an adjacency dict. Example: ({0: [1, 2], 1: [3], 2: [3], 3: []}, 0, 3) -> 2
def shortest_unweighted_path(graph, start, target):
    raise NotImplementedError


# Question 7: Detect an undirected cycle.
# Nodes are 0..n-1. Return True if any component contains a cycle.
# Example: (3, [(0, 1), (1, 2), (2, 0)]) -> True
def has_undirected_cycle(n, edges):
    raise NotImplementedError


# Question 8: Course schedule.
# prerequisites contains (course, prerequisite) pairs. Return whether all
# courses 0..n-1 can be completed. Example: (2, [(1, 0), (0, 1)]) -> False
def can_finish_courses(n, prerequisites):
    raise NotImplementedError


# Question 9: Return a valid course order.
# Use the same prerequisite format; return one order containing all courses,
# or [] if impossible. Example: (3, [(1, 0), (2, 1)]) -> [0, 1, 2]
def course_order(n, prerequisites):
    raise NotImplementedError


# Question 10: Shortest weighted distances.
# Directed edges are (u, v, weight) with nonnegative weight; nodes 0..n-1.
# Return a list of shortest distances from start, with float('inf') when
# unreachable. Example: (3, [(0,1,4), (0,2,10), (1,2,3)], 0) -> [0,4,7]
def shortest_weighted_distances(n, edges, start):
    raise NotImplementedError


def check_question_1():
    assert build_undirected(3, [(0, 1), (1, 2)]) == {0: [1], 1: [0, 2], 2: [1]}
    assert build_undirected(2, []) == {0: [], 1: []}


def check_question_2():
    assert reachable_count({0: [1], 1: [0, 2], 2: [1], 3: []}, 0) == 3
    assert reachable_count({0: []}, 0) == 1


def check_question_3():
    graph = {"a": ["b"], "b": [], "c": []}
    assert has_directed_path(graph, "a", "c") is False
    assert has_directed_path(graph, "a", "b") is True
    assert has_directed_path(graph, "a", "a") is True


def check_question_4():
    assert count_components(5, [(0, 1), (2, 3)]) == 3
    assert count_components(0, []) == 0
    assert count_components(3, [(0, 1), (1, 2)]) == 1


def check_question_5():
    assert island_count(["110", "010", "001"]) == 2
    assert island_count(["000"]) == 0
    assert island_count(["1"]) == 1


def check_question_6():
    graph = {0: [1, 2], 1: [3], 2: [3], 3: [], 4: []}
    assert shortest_unweighted_path(graph, 0, 3) == 2
    assert shortest_unweighted_path(graph, 0, 4) == -1
    assert shortest_unweighted_path(graph, 0, 0) == 0


def check_question_7():
    assert has_undirected_cycle(3, [(0, 1), (1, 2), (2, 0)]) is True
    assert has_undirected_cycle(3, [(0, 1), (1, 2)]) is False
    assert has_undirected_cycle(0, []) is False


def check_question_8():
    assert can_finish_courses(2, [(1, 0), (0, 1)]) is False
    assert can_finish_courses(3, [(1, 0), (2, 1)]) is True
    assert can_finish_courses(0, []) is True


def check_question_9():
    assert course_order(3, [(1, 0), (2, 1)]) == [0, 1, 2]
    assert course_order(2, [(1, 0), (0, 1)]) == []
    assert sorted(course_order(3, [])) == [0, 1, 2]


def check_question_10():
    assert shortest_weighted_distances(3, [(0, 1, 4), (0, 2, 10), (1, 2, 3)], 0) == [0, 4, 7]
    assert shortest_weighted_distances(2, [], 0) == [0, float("inf")]
    assert shortest_weighted_distances(3, [], 2) == [float("inf"), float("inf"), 0]


if __name__ == "__main__":
    import sys
    question = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    if question not in range(1, 11):
        raise SystemExit("Choose a question from 1 to 10")
    globals()[f"check_question_{question}"]()
    print(f"Question {question}: examples passed")
