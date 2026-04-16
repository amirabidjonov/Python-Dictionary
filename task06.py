dict = {
    "name": "Alice",
    "age": 30, 
    "city": "New York"
    },
{
        "name": "Bob",
        "age": 25,
        "city": "Los Angeles"
        }
a = input("Enter the keys: ")
b = (input("Enter the dict: "))
if b == "dict1":
    if a in dict[0]:
        print(dict[0][a])
    else:
        print("Key not found in dict1.")


elif b == "dict2":
    if a in dict[1]:
        print(dict[1][a])
    else:
        print("Key not found in dict2.")

else:    
    print("Key not found in any dictionary.")