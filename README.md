# Brainwave_Matrix_Intern

# 🛡️ Phishing Detection Tool (Internship Task 1)

This is a Python-based phishing detection tool built for **Task 1 of the Brainwave Matrix Solutions Internship**. The tool can detect potentially malicious URLs and suspicious email addresses using logic-based filters and WHOIS lookups.

---

## 🔍 Features

### 🔗 URL Phishing Detection
- Detects use of IP addresses instead of domain names
- Flags shortened URLs (like bit.ly, t.co)
- Warns about lack of HTTPS
- Identifies common phishing tricks (e.g., g00gle.com)
- Uses WHOIS to check domain registration status

### 📧 Email Phishing Detection
- Detects suspicious keywords in emails (e.g., login, verify)
- Flags emails using public domains pretending to be official
- Looks for misspellings and numeric overload

---

## 📦 Requirements

Install dependencies:

```bash
pip install fuzzywuzzy python-whois
