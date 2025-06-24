# 🔐 CyRecon – Automated Reconnaissance Toolkit

[![PyPI version](https://badge.fury.io/py/cyrecon.svg)](https://pypi.org/project/cyrecon/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**CyRecon** is an open-source, AI-assisted reconnaissance toolkit for ethical hackers and cybersecurity enthusiasts. Designed in Python, CyRecon helps automate information gathering by combining subdomain enumeration, port scanning, directory brute-forcing, vulnerability matching, and more — all in one tool.

---

## 🚀 Features

* 🌐 Subdomain Scanner with AI-based Risk Detection
* 🛁 Port Scanner with Service Guessing and Risk Categorization
* 📂 Directory Brute-Forcer with Sensitive Path Detection
* 🧠 CVE Matcher: Automatically suggests vulnerabilities from scan results
* 🖼️ Screenshot Capture for Discovered Subdomains (via Headless Chrome)
* 📝 Export Reports in JSON and PDF formats

---

## 📦 Installation

Install directly from PyPI:

```bash
pip install cyrecon
```

Or install locally:

```bash
git clone https://github.com/mrcoder420/cyrecon.git
cd cyrecon
pip install -r requirements.txt
```

---

## 🧑‍💻 Usage

```bash
python -m cyrecon
```

You’ll be presented with a menu:

```
1. 🌐 Subdomain Scanner
2. 🛁 Port Scanner
3. 📂 Directory Scanner
4. 🧠 Vulnerability Matcher
5. 📝 Export Report
6. 🖼️ Subdomain Screenshots
7. ❌ Exit
```

Each module takes basic input (domain/IP) and returns a result list with AI labels.

---

## ✨ Example

```bash
Enter domain: example.com

[+] https://admin.example.com [200] - AI: 🔴 Malicious
[+] Port 3306 (MySQL) - AI: ⚠️ Vulnerable
[+] /phpinfo - AI: 🔴 Dangerous (PHP info leak)
```

---

## 📄 Report Output

* JSON: `cyrecon_report.json`
* PDF:  `cyrecon_report.pdf`

Example:

```json
{
  "subdomains": [...],
  "ports": [...],
  "dirs": [...],
  "vulnerabilities": [...]
}
```

---

## 🛠️ Dependencies

* `requests`
* `tqdm`
* `colorama`
* `selenium`
* `reportlab`

> 📌 Requires **ChromeDriver** for screenshot functionality — place it in your project root or system PATH.

---

## 🧠 AI Labels

CyRecon uses rule-based heuristics for AI labeling:

* 🔴 Critical / Malicious
* 🟡 Warning / Check Config
* 🟢 Normal / Safe

---

## 📀 Project Structure

```
cyrecon/
├── subdomains.py
├── portscanner.py
├── dirscanner.py
├── vulnmatcher.py
├── screenshooter.py
├── reportgen.py
└── __main__.py
```

---

## 👨‍💼 Author

**Nikhil Sunil Bhor**
💼 Passionate Python Developer & Security Enthusiast
📧 [bhavishya@gmail.com](mailto:bhavishya@gmail.com)
🌐 [LinkedIn](https://linkedin.com/in/yourusername) | [GitHub](https://github.com/yourusername)

---

## 📃 License

MIT License © 2025 Nikhil Bhor
See [`LICENSE`](LICENSE) for full details.

---

## ❤️ Contribute

Pull requests are welcome! For major changes, open an issue first to discuss.

---

## 📊 PyPI

[https://pypi.org/project/cyrecon/](https://pypi.org/project/cyrecon/)

---

> **Tip:** Use this content in your `setup.py` or `pyproject.toml` description too!
