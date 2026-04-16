def group_indices(numbers: list[int]) -> dict[int, list[int]]:
    indices = {}
    for index, number in enumerate(numbers):
        if number not in indices:
            indices[number] = []
        indices[number].append(index)
    return indices
numbers = [1, 2, 3, 2, 1, 4]
result = group_indices(numbers)
print(result)