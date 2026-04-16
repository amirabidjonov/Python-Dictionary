person = {"name": "Ali", "age": 25, "city": "Tashkent"}
key = input("Enter the key: ")
if key in person:
    person.pop(key)
else:
    print(f"Key '{key}' not found in the dictionary.")
