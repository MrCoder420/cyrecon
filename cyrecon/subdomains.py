import requests
import socket
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from cyrecon.ai_classifier import predict_phishing  # ✅ CORRECT
# Importing the AI classifier for phishing detection


import os
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def load_wordlist(filepath):
    """Load subdomain wordlist file"""
    if not os.path.exists(filepath):
        print(f"[!] Wordlist not found: {filepath}")
        return []
    with open(filepath, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def check_subdomain(subdomain, domain):
    """Check if a subdomain is live, fetch IP, label with AI"""
    full_domain = f"{subdomain}.{domain}"
    urls = [
        f"http://{full_domain}",
        f"https://{full_domain}"
    ]
    headers = {'User-Agent': 'CyRecon-Scanner/1.0'}

    for url in urls:
        try:
            ip = socket.gethostbyname(full_domain)
            r = requests.get(url, headers=headers, timeout=4, verify=False, allow_redirects=True)
            if r.status_code < 400:
                label = predict_phishing(url)
                return {
                    "url": url,
                    "status": r.status_code,
                    "ip": ip,
                    "ai_label": label
                }
        except Exception as e:
            continue
    return None

def scan_subdomains(domain, wordlist_path="wordlists/subdomains.txt", threads=20):
    """Main entry point for scanning subdomains with multithreading"""
    wordlist = load_wordlist(wordlist_path)
    if not wordlist:
        print("[!] Wordlist is empty or missing.")
        return []

    print(f"\n[+] Starting Subdomain Scan on: {domain}\n")
    found = []

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(check_subdomain, sub, domain) for sub in wordlist]

        for future in tqdm(futures, desc="🔍 Scanning", ncols=70):
            result = future.result()
            if result:
                print(f"[+] {result['url']} [{result['status']}] ({result['ip']}) - 🧠 AI: {result['ai_label']}")
                found.append(result)

    if not found:
        print("[!] No live subdomains found.\n")
    else:
        print(f"\n✅ Found {len(found)} live subdomains.\n")

    return found
