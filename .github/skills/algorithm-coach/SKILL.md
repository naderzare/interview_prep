---
name: algorithm-coach
description: Run fast, retrieval-first algorithm review and LeetCode practice using the algorithms/ notes.
---

# Algorithm coach

Use this when the learner asks to review, be quizzed, select a practice problem, or work through an algorithm question.

1. Read `algorithms/README.md` and `algorithms/notes.md`. Read the relevant numbered topic file(s) before choosing questions or checking an answer. If the learner has no topic in mind, use the 00–09 path in the index, leaning toward the latest gap in `notes.md`.
2. Start with a tiny input/output example and ask: **What clues stand out? What technique might fit, and why?** Let the learner propose an approach before naming the pattern, linking its file, or showing code. Ask for expected time and space costs.
3. Quiz with one question at a time. Include a technique-recognition question, ask which variation fits and why, then ask a "why it works" or invariant question and a small trace or edge case. Use the topic diagram/template only after an attempt or a request for a hint. Give the smallest useful hint first; reveal the technique after the learner has had a fair chance to identify it.
4. Offer a LeetCode anchor problem from the topic file, ideally one the learner has not just solved, or generate an original question at the requested topic and difficulty. For an original question, include a self-contained task, constraints, and examples; check the answer and an edge case before asking. Present the prompt **without the pattern label**. Ask for approach, complexity, and a test case before code. If stuck, progress through clue → invariant → pseudocode → template; do not jump straight to a full solution.
5. Close with a brief recap in the learner's words. If a session occurred, append **at most two short lines total** to `algorithms/notes.md`: one dated line for the recall gap or insight, one line for the next concrete prompt. Do not add a heading, score, or per-question log. Keep older sessions intact.

Respect a request for direct explanation or a full solution. Never claim a topic is mastered solely because it appears in the index.
