import json
import os
def load_users():
    project_folder = os.path.dirname(os.path.abspath(__file__))
    users_file = os.path.join(project_folder, "users.json")
    with open(users_file, "r") as file:
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
    project_folder = os.path.dirname(os.path.abspath(__file__))
    report_file = os.path.join(project_folder, "findings.txt")
    with open(report_file, "w") as report:
        report.write("AWS IAM Security Audit Report\n")
        report.write("=" * 35 + "\n\n")
        for finding in findings:
            report.write(finding + "\n")
    print("\nAudit Complete")
    print(f"Total Findings: {len(findings)}")
    print("Report saved to findings.txt")
users = load_users()
results = audit_users(users)
create_report(results)
