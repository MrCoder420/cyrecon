import socket
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

# Known services
COMMON_PORTS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
    80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS",
    3306: "MySQL", 3389: "RDP", 8080: "HTTP-Alt"
}

# Suspicious ports based on hacking/malware tools
SUSPICIOUS_PORTS = {
    23: "Telnet (Unencrypted, legacy access)",
    4444: "Metasploit Reverse Shell",
    1337: "Leet Shell / Custom Backdoor",
    6667: "IRC (Botnet control)",
    31337: "Elite Backdoor / NetBus",
    12345: "NetBus Trojan",
    8081: "Hidden HTTP proxy / panel",
    5985: "Windows Remote Mgmt",
    2323: "Telnet Alt (often abused)",
    9001: "Tor / Hidden Shell",
}

def scan_port(ip, port, timeout=1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((ip, port))
            if result == 0:
                service = COMMON_PORTS.get(port, "Unknown")
                label = "⚠️ Suspicious" if port in SUSPICIOUS_PORTS else "✓ Normal"
                reason = SUSPICIOUS_PORTS.get(port, "")
                return {
                    "port": port,
                    "service": service,
                    "ai_label": label,
                    "reason": reason
                }
    except:
        pass
    return None

def scan_ports(ip, ports=None, threads=100):
    if ports is None:
        ports = list(range(1, 1025))  # top 1024

    print(f"\n[+] Starting AI Port Scan on {ip}...\n")
    results = []

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(scan_port, ip, port) for port in ports]

        for future in tqdm(futures, desc="Scanning Ports", ncols=70):
            result = future.result()
            if result:
                print(f"[+] Port {result['port']} ({result['service']}) - AI: {result['ai_label']} {result['reason']}")
                results.append(result)

    return results
