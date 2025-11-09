# ROHAN-WAYAL-DSA-CODE-


________________________________________
🧩 PART A (C++)
________________________________________
1️⃣ Searching and Sorting – Student Database
Q1: What is the difference between Linear Search and Binary Search?

A1: Linear Search checks every element one by one (O(n)), while Binary Search divides the list in half repeatedly (O(log n)) but works only on sorted data.

Q2: Why do we use realloc() in the program?

A2: realloc() dynamically expands or shrinks the allocated memory without losing existing data.

Q3: What is the difference between Bubble Sort and Selection Sort?

A3: Bubble Sort repeatedly swaps adjacent elements, while Selection Sort selects the smallest/largest element and places it in correct position. Both have O(n²) complexity.

Q4: Why must we sort before using Binary Search?

A4: Because Binary Search relies on comparing midpoints — if the array isn’t sorted, its logic fails.

Q5: What are the time complexities of the algorithms used?

A5: Linear Search – O(n), Binary Search – O(log n), Bubble Sort/Selection Sort – O(n²).
________________________________________

2️⃣ Stack using Linked List (Infix → Postfix & Prefix)
Q1: Why do we use Stack in expression conversion?

A1: Stack helps manage operators and parentheses according to precedence and associativity rules.

Q2: What is the main advantage of using Linked List for Stack?

A2: It removes size limitations of arrays and allows dynamic memory usage.

Q3: What is operator precedence?

A3: It defines the order in which operations are performed, e.g., * and / have higher precedence than + and -.

Q4: Convert (A + B) * C to Postfix.

A4: Postfix form = AB+C*.

Q5: What is the time complexity of push() and pop()?

A5: Both push() and pop() have O(1) time complexity.
________________________________________
3️⃣ Circular Queue using Array
Q1: Why is a circular queue better than a linear queue?

A1: It reuses deleted space efficiently without shifting elements.


Q2: How to check if the queue is full or empty?
A2:

•	Full → (rear + 1) % size == front
•	Empty → front == -1.

Q3: What is the function of front and rear pointers?

A3: front points to the first element; rear points to the last element in the queue.

Q4: What happens if dequeue is performed on an empty queue?

A4: It causes an “Underflow” condition.

Q5: What is the time complexity of enqueue/dequeue operations?

A5: Both are O(1).

________________________________________
🧩 PART B (Python)
________________________________________
4️⃣ Binary Search Tree (BST)

Q1: What is the property of BST?

A1: Left child < Root < Right child.

Q2: Difference between inorder, preorder, and postorder traversals?

A2:
•	Inorder → Left, Root, Right
•	Preorder → Root, Left, Right
•	Postorder → Left, Right, Root

Q3: How to handle duplicate entries?

A3: Either reject them or place duplicates on the right subtree.

Q4: What is tree depth?

A4: The number of edges from the root to the deepest leaf.

Q5: What are the time complexities of insert, search, delete?

A5: Average – O(log n), Worst – O(n) (for skewed tree).
________________________________________

5️⃣ Graph – Minimum Spanning Tree (Kruskal’s & Prim’s)

Q1: What is a Minimum Spanning Tree?

A1: A tree connecting all vertices with minimum total edge weight and no cycles.

Q2: Difference between Kruskal’s and Prim’s algorithm?

A2:
•	Kruskal’s → Edge-based, uses sorting.
•	Prim’s → Vertex-based, grows one vertex at a time.
Q3: What data structure is used in Kruskal’s?

A3: Disjoint Set (Union-Find) to detect cycles.

Q4: What are their time complexities?

A4: O(E log E) for Kruskal’s, O(V²) for basic Prim’s, O(E log V) for optimized Prim’s.

Q5: Where are MSTs used?

A5: In network design, road maps, and communication systems.
________________________________________
6️⃣ Heap Sort
Q1: What is a heap?

A1: A binary tree satisfying heap property:

•	Max-Heap → parent ≥ children
•	Min-Heap → parent ≤ children.

Q2: How is a heap built from an array?

A2: By repeatedly calling heapify() from the last non-leaf node upwards.

Q3: What is Heap Sort’s complexity?


A3: O(n log n) for all cases.

Q4: Why is Heap Sort in-place?

A4: Because it sorts the array without extra memory.

Q5: Is Heap Sort stable?

A5: No, equal elements may change relative order.

________________________________________
7️⃣ Merge Sort
Q1: What is the idea behind Divide and Conquer?

A1: Divide problem → Solve subproblems → Combine solutions.

Q2: How does Merge Sort work?

A2: Recursively splits array into halves, sorts them, and merges sorted halves.

Q3: What are its time and space complexities?

A3: Time – O(n log n), Space – O(n).

Q4: Why is Merge Sort stable?

A4: Because it preserves the order of equal elements during merging.

Q5: Why is Merge Sort better for linked lists?

A5: Merging linked lists doesn’t need extra space or index manipulation.

________________________________________
8️⃣ Fractional Knapsack (Greedy Algorithm)
Q1: Why is it called Greedy?

A1: Because at every step, it makes the locally optimal choice (highest profit/weight ratio).

Q2: What is the role of profit/weight ratio?

A2: It determines which parcel gives maximum profit per kg.

Q3: Difference between Fractional and 0/1 Knapsack?

A3: In Fractional, items can be divided; in 0/1, they cannot.

Q4: What is the time complexity?

A4: O(n log n) (due to sorting).

Q5: Is Greedy approach always optimal?

A5: Only for Fractional Knapsack — not for 0/1 Knapsack.

________________________________________
9️⃣ Naïve String Matching
Q1: How does the Naïve algorithm work?

A1: It compares pattern with every substring of text sequentially.

Q2: What is its time complexity?

A2: O((n−m+1) × m), worst case O(n×m).

Q3: Why is it called Naïve?

A3: Because it doesn’t skip any unnecessary comparisons.

Q4: What are its advantages?

A4: Easy to implement and works fine for small text.

Q5: How can it be improved?

A5: Using efficient algorithms like KMP or Rabin-Karp.

________________________________________
🔟 AI Search Algorithm (Maze Navigation)
Q1: What is the difference between uninformed and informed search?
A1:
•	Uninformed (BFS, DFS) → No heuristic knowledge.
•	Informed (A*, Best-first) → Uses heuristics to guide search.
Q2: What is a heuristic?
A2: A function estimating the cost from current node to goal.
Q3: How does A* ensure the shortest path?
A3: By combining actual cost (g) and heuristic cost (h): f(n) = g(n) + h(n).
Q4: Difference between BFS and DFS?
A4:
•	BFS → Level-order, finds shortest path.
•	DFS → Goes deep first, uses less memory but may get stuck.
Q5: Real-life applications of AI Search?
A5: GPS navigation, robotics, game pathfinding, and puzzle solving.
________________________________________
✅ Total: 10 programs × 5 questions = 50 Viva Questions with Answers
________________________________________

