import sqlite3

conn = sqlite3.connect("quiz.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    option1 TEXT,
    option2 TEXT,
    option3 TEXT,
    option4 TEXT,
    answer TEXT,
    difficulty TEXT
)
""")

# Insert sample data
advanced_questions = [

# ---------------- DE ----------------
("What is the output of SR Flip-Flop when S=1, R=0?", "Set","Reset","Invalid","Toggle","Set","easy"),
("Invalid condition of SR Flip-Flop?", "S=1,R=1","S=0,R=0","S=1,R=0","S=0,R=1","S=1,R=1","easy"),
("JK Flip-Flop solves which problem?", "Race condition","Invalid state","Overflow","Deadlock","Invalid state","medium"),
("Characteristic equation of JK FF?", "Q=JQ'+K'Q","Q=JQ+KQ'","Q=J+K","None","Q=JQ'+K'Q","hard"),
("D Flip-Flop eliminates?", "Race condition","Invalid state","Overflow","Deadlock","Invalid state","medium"),
("T Flip-Flop toggles when?", "T=0","T=1","T=2","Always","T=1","easy"),
("Propagation delay refers to?", "Time to change output","Clock delay","Memory delay","None","Time to change output","medium"),
("Combinational circuit depends on?", "Input only","Output only","Memory","Clock","Input only","easy"),
("Sequential circuit depends on?", "Input","Past output","Clock","All","All","medium"),
("Encoder converts?", "Binary to decimal","Decimal to binary","Analog to digital","None","Decimal to binary","easy"),

# ---------------- DMGT ----------------
("A relation that is reflexive, symmetric and transitive?", "Function","Equivalence","Partial","Total","Equivalence","easy"),
("Number of subsets of set with n elements?", "n","2^n","n^2","n!","2^n","easy"),
("Pigeonhole principle ensures?", "Uniqueness","At least one repetition","No repetition","None","At least one repetition","medium"),
("If a|b and b|c then?", "a|c","c|a","b|a","None","a|c","medium"),
("Graph with no cycles?", "Tree","Complete","Null","Directed","Tree","easy"),
("Euler path exists if?", "All vertices even","2 odd vertices","All odd","None","2 odd vertices","medium"),
("Hamiltonian path visits?", "All edges","All vertices","None","Repeated","All vertices","easy"),
("Bipartite graph contains?", "Odd cycle","Even cycle","No cycle","None","Even cycle","hard"),
("Adjacency matrix represents?", "Edges","Vertices","Both","None","Edges","medium"),
("Planar graph can be drawn?", "Without crossing","With crossing","Circular","None","Without crossing","easy"),

# ---------------- OS ----------------
("Process is?", "Program in execution","Program","Thread","File","Program in execution","easy"),
("PCB stores?", "Process info","Memory","CPU","None","Process info","medium"),
("FCFS scheduling is?", "Non-preemptive","Preemptive","Hybrid","None","Non-preemptive","easy"),
("Shortest Job First minimizes?", "Waiting time","Turnaround","CPU","None","Waiting time","medium"),
("Deadlock occurs when?", "Circular wait","No wait","Fast CPU","None","Circular wait","easy"),
("Semaphore used for?", "Synchronization","Memory","CPU","None","Synchronization","easy"),
("Paging removes?", "Fragmentation","Deadlock","CPU","None","Fragmentation","medium"),
("Virtual memory uses?", "Disk","RAM","CPU","None","Disk","easy"),
("Thrashing occurs when?", "High paging","Low memory","CPU idle","None","High paging","medium"),
("Round Robin uses?", "Time quantum","Priority","FCFS","None","Time quantum","easy"),

# ---------------- JAVA ----------------
("Java is?", "Compiled","Interpreted","Both","None","Both","easy"),
("JVM stands for?", "Java Virtual Machine","Java Variable Machine","Just VM","None","Java Virtual Machine","easy"),
("Method overloading is?", "Compile-time polymorphism","Runtime","None","Both","Compile-time polymorphism","medium"),
("Method overriding is?", "Runtime polymorphism","Compile-time","None","Both","Runtime polymorphism","medium"),
("final keyword means?", "Constant","Variable","Loop","None","Constant","easy"),
("Inheritance uses?", "extends","implements","import","None","extends","easy"),
("Interface contains?", "Abstract methods","Concrete","Both","None","Abstract methods","medium"),
("Exception handling uses?", "try-catch","if-else","loop","None","try-catch","easy"),
("Array index starts from?", "0","1","-1","None","0","easy"),
("String is?", "Immutable","Mutable","Both","None","Immutable","medium"),

# ---------------- DSA ----------------
("Stack follows?", "LIFO","FIFO","Random","None","LIFO","easy"),
("Queue follows?", "FIFO","LIFO","Random","None","FIFO","easy"),
("Binary search complexity?", "O(log n)","O(n)","O(n^2)","O(1)","O(log n)","easy"),
("Linear search complexity?", "O(n)","O(log n)","O(n^2)","O(1)","O(n)","easy"),
("Tree root has?", "No parent","Children","Edges","None","No parent","easy"),
("Graph is?", "Set of nodes","Edges","Both","None","Both","easy"),
("DFS uses?", "Stack","Queue","Heap","None","Stack","medium"),
("BFS uses?", "Queue","Stack","Heap","None","Queue","medium"),
("Linked list stores?", "Nodes","Array","Stack","None","Nodes","easy"),
("Heap is?", "Complete binary tree","Binary tree","Graph","None","Complete binary tree","medium")
]

cursor.executemany("""
INSERT INTO questions (question, option1, option2, option3, option4, answer, difficulty)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", advanced_questions)

conn.commit()
conn.close()

print("Database created successfully!")