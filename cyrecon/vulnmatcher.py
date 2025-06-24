# cyrecon/vulnmatcher.py

def match_vulnerabilities(scan_results):
    suggestions = []

    # === 1. PORT-BASED CHECKS ===
    for item in scan_results.get("ports", []):
        port = item["port"]
        service = item["service"].lower()

        if port == 21 or "ftp" in service:
            suggestions.append({
                "target": f"Port {port} (FTP)",
                "risk": "Anonymous FTP login — CVE-2021-44142",
                "ai_label": "⚠️ Vulnerable"
            })

        elif port == 22 or "ssh" in service:
            suggestions.append({
                "target": f"Port {port} (SSH)",
                "risk": "Check for weak credentials or outdated OpenSSH",
                "ai_label": "🟡 Warning"
            })

        elif port == 23 or "telnet" in service:
            suggestions.append({
                "target": f"Port {port} (Telnet)",
                "risk": "Telnet is insecure. Possible sniffing / remote access risk",
                "ai_label": "🔴 Dangerous"
            })

        elif port == 25 or "smtp" in service:
            suggestions.append({
                "target": f"Port {port} (SMTP)",
                "risk": "SMTP relay attacks or spoofing possible — CVE-2023-0669",
                "ai_label": "⚠️ Check relay config"
            })

        elif port == 80 or port == 8080:
            suggestions.append({
                "target": f"Port {port} (HTTP)",
                "risk": "Check for outdated CMS, XSS, or directory listing",
                "ai_label": "🟡 Needs Manual Review"
            })

        elif port == 443:
            suggestions.append({
                "target": f"Port {port} (HTTPS)",
                "risk": "If weak SSL, could be vulnerable to SSL attacks (BEAST, POODLE)",
                "ai_label": "🟡 Medium"
            })

        elif port == 3306 or "mysql" in service:
            suggestions.append({
                "target": f"Port {port} (MySQL)",
                "risk": "CVE-2012-2122 – Bypass auth via handshake bug",
                "ai_label": "🔴 Critical"
            })

        elif port == 3389:
            suggestions.append({
                "target": f"Port {port} (RDP)",
                "risk": "BlueKeep RDP vuln — CVE-2019-0708",
                "ai_label": "🔴 Critical"
            })

        elif port == 4444:
            suggestions.append({
                "target": f"Port {port}",
                "risk": "Metasploit reverse shell. May be actively exploited.",
                "ai_label": "🔴 Exploitable"
            })

        elif port == 5900:
            suggestions.append({
                "target": f"Port {port} (VNC)",
                "risk": "Exposed VNC sessions can be hijacked — CVE-2019-15681",
                "ai_label": "⚠️ High Risk"
            })

    # === 2. DIRECTORY/URL-BASED CHECKS ===
    for item in scan_results.get("dirs", []):
        path = item["url"].lower()

        if "phpinfo" in path:
            suggestions.append({
                "target": path,
                "risk": "Exposes PHP config and environment — CVE-2019-11043",
                "ai_label": "🔴 Dangerous"
            })

        elif any(x in path for x in [".sql", ".zip", ".tar", "backup", "dbdump"]):
            suggestions.append({
                "target": path,
                "risk": "Possible database or source code dump exposed",
                "ai_label": "🔴 Critical"
            })

        elif "/.git" in path:
            suggestions.append({
                "target": path,
                "risk": "Git repository may be downloaded — CVE-2018-17456",
                "ai_label": "🔴 Dangerous"
            })

        elif "/admin" in path or "/wp-admin" in path:
            suggestions.append({
                "target": path,
                "risk": "Admin panel detected — Brute-force or default creds risk",
                "ai_label": "🟠 Sensitive"
            })

    # === 3. SUBDOMAIN CHECKS ===
    for item in scan_results.get("subdomains", []):
        sub = item["url"].lower()

        if "phpmyadmin" in sub:
            suggestions.append({
                "target": sub,
                "risk": "phpMyAdmin exposed — CVE-2018-12613, RCE via GET",
                "ai_label": "🔴 Critical"
            })

        elif "test" in sub or "dev" in sub or "staging" in sub:
            suggestions.append({
                "target": sub,
                "risk": "Non-production subdomain exposed. May have weak security.",
                "ai_label": "⚠️ High Risk"
            })

        elif "webmail" in sub:
            suggestions.append({
                "target": sub,
                "risk": "Webmail often vulnerable to brute-force or XSS",
                "ai_label": "🟠 Watch"
            })

        elif "git" in sub:
            suggestions.append({
                "target": sub,
                "risk": "May contain .git leaks or developer tools",
                "ai_label": "⚠️ Sensitive"
            })

    return suggestions
