def group_by_age(people: list[dict[str, int | str]]) -> dict[int, list[str]]:
    age_groups = {}
    for person in people:
        age = person["age"]
        name = person["name"]
        if age not in age_groups:
            age_groups[age] = []
        age_groups[age].append(name)
    return age_groups

        
people = [
    {"name": "Ali", "age": 25},
    {"name": "Vali", "age": 30},
    {"name": "Soli", "age": 25},
    {"name": "Karim", "age": 30}
]
result = group_by_age(people)
print(result)