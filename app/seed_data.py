import sqlite3

conn = sqlite3.connect("edtech.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    grade TEXT,
    created_at TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses(
    id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS enrollments(
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_id INTEGER,
    enrolled_at TEXT
)
""")

# Insert students
students = [
(1,"Rahul","A","2024-01-01"),
(2,"Aman","B","2024-02-01"),
(3,"Priya","A","2024-03-01"),
(4,"Riya","C","2024-04-01"),
(5,"Ankit","B","2024-05-01"),
(6,"Simran","A","2024-06-01"),
(7,"Karan","B","2024-07-01"),
(8,"Neha","A","2024-08-01"),
(9,"Arjun","C","2024-09-01"),
(10,"Pooja","B","2024-10-01")
]

# Insert courses
courses = [
(1,"Python","Programming"),
(2,"Machine Learning","AI"),
(3,"Data Science","AI"),
(4,"Web Development","Programming"),
(5,"SQL","Database")
]

# Insert enrollments
enrollments = [
(1,1,1,"2024-01-10"),
(2,2,1,"2024-01-15"),
(3,3,2,"2024-02-10"),
(4,4,3,"2024-02-20"),
(5,5,1,"2024-03-01"),
(6,6,4,"2024-03-05"),
(7,7,5,"2024-03-10"),
(8,8,1,"2024-04-01"),
(9,9,2,"2024-04-10"),
(10,10,3,"2024-04-20"),
(11,1,4,"2024-05-01"),
(12,2,5,"2024-05-10"),
(13,3,1,"2024-06-01"),
(14,4,2,"2024-06-10"),
(15,5,3,"2024-06-20"),
(16,6,1,"2024-07-01"),
(17,7,2,"2024-07-10"),
(18,8,3,"2024-07-20"),
(19,9,1,"2024-08-01"),
(20,10,5,"2024-08-10")
]

cursor.executemany("INSERT INTO students VALUES(?,?,?,?)", students)
cursor.executemany("INSERT INTO courses VALUES(?,?,?)", courses)
cursor.executemany("INSERT INTO enrollments VALUES(?,?,?,?)", enrollments)

conn.commit()
conn.close()

print("Database created and data inserted successfully!")