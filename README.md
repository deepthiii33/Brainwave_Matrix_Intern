# 👩‍💻 Brainwave_Matrix_Intern

## 🛡️ Phishing Detection Tool — Internship Task 1

Hi! I'm Deepthi 👋 — and this tool was built as part of my internship at **Brainwave Matrix Solutions**. The task was to build a **Phishing Link Scanner** using Python that can analyze URLs for signs of phishing and help detect unsafe links.

---
### 🔍 What This Tool Can Do

This Python-based tool checks if a given URL is suspicious or not. It looks for multiple red flags commonly used in phishing attempts.

### ✅ Features:
- Detects **URL shorteners** like `bit.ly`, `tinyurl.com`, etc.
- Flags links that use an **IP address** instead of a proper domain
- Warns about URLs with **too many digits**
- Checks for the presence of **"@" symbol** (often used to trick users)
- Verifies if the URL is using **HTTPS**
- Uses **fuzzy matching** to detect fake versions of real brand domains (like `go0gle.com`)
- Allows scanning of **multiple URLs at once**

---

### 🧠 How It Works

The tool parses the structure of each URL and applies logic-based filters. It combines pattern matching and fuzzy string comparison to flag potentially harmful links.

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
🚀 Getting Started
1. Download or Clone the Project
Option 1: Click the green Code button on this page and download the ZIP file. Then extract it on your system.

Option 2: Use Git :
- ```git clone https://github.com/deepthiii33/Brainwave_Matrix_Intern.git```
- ```cd Brainwave_Matrix_Intern```

2. Run the Tool
Run the script using: ``` python Phishing_scanner.py ```

3. Enter your URLs (comma-separated), and the tool will analyze each one and give you a result

4. Example Inputs
   
   ![](https://github.com/deepthiii33/Brainwave_Matrix_Intern/blob/main/Sample.png)

📌 **Notes**  
--------

> This script is built for educational purposes as part of an internship.  
> While it detects many phishing tactics, no tool is 100% accurate — always stay cautious online.

   
   























