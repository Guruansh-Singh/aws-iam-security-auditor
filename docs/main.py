import json
print("\nAWS IAM Security Auditor")
print("-" * 30)
with open("users.json", "r") as file:
    users = json.load(file)
for user in users:
    username = user["username"]
    role = user["role"]
    if role == "Administrator":
        print(f"[HIGH RISK] {username} has Administrator access")
    else:
        print(f"[OK] {username} -> {role}")
