def merge_dicts(a: dict, b: dict) -> dict:
    merged = a.copy()
    merged.update(b)
    return merged

dict1 = {"apple": 10, "banana": 5}
dict2 = {"banana": 20, "orange": 8}

result = merge_dicts(dict1, dict2)
print(result)