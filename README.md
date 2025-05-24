# 🛡️ Phishing Detection Tool — Internship Task 1

Hi, I’m Deepthi 👋 — and this project was built as part of my internship at Brainwave Matrix Solutions. The task was to develop a Python tool that helps detect phishing links by scanning and analyzing URLs for suspicious patterns.

---
### 🔍 What This Tool Can Do

This Python-based tool checks if a given URL is suspicious or not. It looks for multiple red flags commonly used in phishing attempts.

### ✅ Key Features:
- Detects **URL shorteners** like `bit.ly`, `tinyurl.com`, etc.
- Flags links that use an **IP address** instead of a proper domain
- Warns about URLs with **too many digits**
- Checks for the presence of **"@" symbol** (often used to trick users)
- Verifies if the URL is using **HTTPS**
- Uses **fuzzy matching** to detect fake versions of real brand domains (like `go0gle.com`)
- Allows scanning of **multiple URLs at once**

---

### 🧠 How It Works

The tool breaks down and inspects each URL, using a mix of pattern detection and fuzzy string matching to identify risky elements. If any red flags are found, it highlights them clearly for the user.

---

### 🔧 What You’ll Need

- **Python** 3.8 or higher installed on your system
- Python libraries:
  - `fuzzywuzzy`
  - Standard libraries: `re`, `urllib.parse`

To install the required libraries, run:

```bash
   pip install fuzzywuzzy 
```
---

### 🚀 How to Use

1. Download or Clone the Project

2. Run the Tool
Run the script using:

```bash
 python Phishing_scanner.py
```

4. Enter your URLs (comma-separated), and the tool will analyze each one and give you a result

5. Example Inputs
   
   ![](https://github.com/deepthiii33/Brainwave_Matrix_Intern/blob/main/Sample.png)

📌 **Notes**  
--------

> This script is built for educational purposes as part of an internship.  
> While it does a good job catching many common phishing signs, it may not always be accurate. Always stay cautious and double-check links — no automated tool is perfect.

   
   























