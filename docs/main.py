import json
def load_users():
    with open("users.json", "r") as file:
        return json.load(file)
def audit_users(users):
    print("\nAWS IAM Security Auditor")
    print("-" * 30)
    for user in users:
        username = user["username"]
        role = user["role"]
        if role == "Administrator":
            print(f"[HIGH RISK] {username} has Administrator access")
        else:
            print(f"[OK] {username} -> {role}")

users = load_users()
audit_users(users)
