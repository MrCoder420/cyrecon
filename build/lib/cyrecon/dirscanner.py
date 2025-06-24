import requests
from tqdm import tqdm
import os

# AI classification of risky paths
SUSPICIOUS_PATHS = {
    "admin": "Admin login panel",
    "phpinfo": "PHP system info exposure",
    "backup": "Potential backup leak",
    "config": "Exposes config files",
    "dev": "Dev panel or internal files",
    "test": "Testing env (leaks info)",
    "staging": "Staging version exposed",
    "old": "Old backup files",
    "debug": "Debug tools exposed",
    "upload": "Upload endpoint",
    "private": "Private or restricted",
    "files": "Raw file access",
    "data": "Data leak risk",
    "login": "User login",
    "dashboard": "Control dashboard"
}

def scan_directories(base_url, wordlist_path="wordlists/directories.txt"):
    """Scan for common directories and flag suspicious ones using AI logic"""
    if not base_url.startswith("http"):
        base_url = "http://" + base_url

    if not os.path.exists(wordlist_path):
        print(f"[!] Wordlist not found: {wordlist_path}")
        return []

    with open(wordlist_path, 'r') as f:
        paths = [line.strip() for line in f if line.strip()]

    headers = {"User-Agent": "CyRecon-DirScanner/1.0"}
    results = []

    print(f"\n[+] Scanning Directories on {base_url}...\n")

    for path in tqdm(paths, desc="📂 Scanning Dirs", ncols=70):
        url = f"{base_url.rstrip('/')}/{path}"
        try:
            r = requests.get(url, headers=headers, timeout=4)
            if r.status_code in [200, 301, 302]:
                label = "⚠️ Suspicious" if path.lower() in SUSPICIOUS_PATHS else "✓ Normal"
                reason = SUSPICIOUS_PATHS.get(path.lower(), "")
                print(f"[+] {url} [{r.status_code}] - AI: {label} {reason}")
                results.append({
                    "url": url,
                    "status": r.status_code,
                    "ai_label": label,
                    "reason": reason
                })
        except:
            continue

    if not results:
        print("[!] No valid directories found.\n")
    else:
        print(f"\n✅ Found {len(results)} directories.\n")

    return results
