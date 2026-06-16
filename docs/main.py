import json
def load_users():
    with open("users.json", "r") as file:
        return json.load(file)
def audit_users(users):
    findings = []
    for user in users:
        username = user["username"]
        role = user["role"]
        if role == "Administrator":
            findings.append(f"[HIGH RISK] {username} has Administrator access")
        elif role == "PowerUser":
            findings.append(f"[MEDIUM RISK] {username} has PowerUser access")
        else:
            findings.append(f"[LOW RISK] {username} has {role} access")
    return findings
def create_report(findings):
    with open("findings.txt", "w") as report:
        report.write("AWS IAM Security Audit Report\n")
        report.write("=" * 35 + "\n\n")
        for finding in findings:
            report.write(finding + "\n")
    print("Audit complete.")
    print("Report saved to findings.txt")
users = load_users()
results = audit_users(users)
create_report(results)
