# AWS IAM Security Auditor

A Python-based cloud security project that simulates an AWS Identity and Access Management (IAM) security audit. The tool analyzes IAM user data, identifies potential security risks, and generates an automated security report highlighting privileged accounts, password policy violations, and Multi-Factor Authentication (MFA) compliance.

---

## Features

* Role-based IAM risk classification
* Detection of Administrator and PowerUser accounts
* Password age auditing
* MFA compliance checking
* Automated security report generation
* Summary of high, medium, and low-risk users

---

## Technologies Used

* Python 3
* JSON
* Git
* GitHub

---

## Project Structure

```text
aws-iam-security-auditor
│
├── main.py
├── users.json
├── findings.txt
├── README.md
└── docs/
    └── requirements.txt
```

---

## How It Works

1. Loads IAM user information from a JSON file.
2. Reviews each user's assigned role.
3. Checks password age against a defined threshold.
4. Verifies whether MFA is enabled.
5. Assigns risk levels based on findings.
6. Generates a security audit report.

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/Guruansh-Singh/aws-iam-security-auditor.git
```

Move into the project folder:

```bash
cd aws-iam-security-auditor
```

Run the program:

```bash
python main.py
```

The generated report will be saved as:

```text
findings.txt
```

---

## Sample Output
<img width="2190" height="876" alt="image" src="https://github.com/user-attachments/assets/39c12ef0-bf01-4bd5-94bf-d04485da81ac" />


## Future Improvements

* Integration with AWS IAM APIs using Boto3
* CSV and HTML report generation
* Interactive dashboard for audit results
* Email alert notifications
* Support for multiple AWS accounts

---

## Author

**Guruansh Singh**

Bachelor of Computer Applications (BCA)

Interested in Cloud Security, Cybersecurity, and Secure Computing Systems.
