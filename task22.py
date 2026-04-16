def group_students(students: list[dict[str, str]]) -> dict[str, list[str]]:
    grouped = {}
    for student in students:
        group = student["group"]
        name = student["name"]
        if group not in grouped:
            grouped[group] = []
        grouped[group].append(name)
    return grouped

students = [
    {"name": "Ali", "group": "A"},
    {"name": "Soli", "group": "A"},
    {"name": "Karim", "group": "B"},
    {"name": "Vali", "group": "B"} 
    ]
result = group_students(students)
print(result)