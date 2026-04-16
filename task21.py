def count_names(names: list[str]) -> dict[str, int]:
    name_count = {}
    for name in names:
        if name in name_count:
            name_count[name] += 1
        else:
            name_count[name] = 1
    return name_count

names = ["Ali", "Vali", "Ali", "Sami", "Vali", "Ali"]

result = count_names(names)
print(result)
