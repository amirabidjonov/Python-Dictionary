users = [
  {"id": 1, "active": True},
  {"id": 2, "active": True},
]
result = users[0]["active"] = False
result = users[1]["active"] = False
print(users)