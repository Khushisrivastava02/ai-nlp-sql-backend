def convert_question_to_sql(question):
    q = question.lower()

    if "how many" in q and "python" in q:
        return """
        SELECT COUNT(*)
        FROM enrollments e
        JOIN courses c ON e.course_id = c.id
        WHERE c.name = 'Python'
        """

    elif "list students" in q:
        return "SELECT * FROM students"

    elif "list courses" in q:
        return "SELECT * FROM courses"

    else:
        return "SELECT * FROM students LIMIT 5"