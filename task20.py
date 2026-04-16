permissions = {"read": True, "write": False, "delete": True}
for key in permissions:
    if permissions[key] == True:
        print(key)