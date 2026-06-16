import json
import os
def load_users():
    project_folder = os.path.dirname(os.path.abspath(__file__))
    users_file = os.path.join(project_folder, "users.json")
    with open(users_file, "r") as file:
        return json.load(file)
def audit_users(users):
    findings = []
    high_risk = 0
    medium_risk = 0
    low_risk = 0
    for user in users:
        username = user["username"]
        role = user["role"]
        if role == "Administrator":
            findings.append(f"[HIGH RISK] {username} has Administrator access")
            high_risk += 1
        elif role == "PowerUser":
            findings.append(f"[MEDIUM RISK] {username} has PowerUser access")
            medium_risk += 1
        else:
            findings.append(f"[LOW RISK] {username} has {role} access")
            low_risk += 1
    summary = {
        "high": high_risk,
        "medium": medium_risk,
        "low": low_risk,
        "total": len(users)
    }
    return findings, summary
def create_report(findings, summary):
    project_folder = os.path.dirname(os.path.abspath(__file__))
    report_file = os.path.join(project_folder, "findings.txt")

    with open(report_file, "w") as report:
        report.write("AWS IAM Security Audit Report\n")
        report.write("=" * 35 + "\n\n")
        report.write(f"Total Users: {summary['total']}\n")
        report.write(f"High Risk Users: {summary['high']}\n")
        report.write(f"Medium Risk Users: {summary['medium']}\n")
        report.write(f"Low Risk Users: {summary['low']}\n\n")
        report.write("Findings:\n")
        report.write("-" * 20 + "\n")
        for finding in findings:
            report.write(finding + "\n")

    print("\nAudit Complete")
    print(f"Total Users: {summary['total']}")
    print(f"High Risk Users: {summary['high']}")
    print(f"Medium Risk Users: {summary['medium']}")
    print(f"Low Risk Users: {summary['low']}")
    print("Report saved to findings.txt")

users = load_users()
findings, summary = audit_users(users)
create_report(findings, summary)