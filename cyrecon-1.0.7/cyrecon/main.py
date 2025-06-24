from cyrecon import subdomains
from cyrecon import portscanner
from cyrecon import dirscanner
from cyrecon import vulnmatcher
from cyrecon import reportgen
from cyrecon import screenshooter

import os

all_results = {}
last_vulns = []

def banner():
    print(r"""
   ____       ____                     
  / ___| ___ |___ \ ___  ___  ___ ___ 
 | |    / _ \  __) / _ \/ __|/ __/ _ \
 | |___| (_) |/ __/  __/\__ \ (_| (_) |
  \____|\___/|_____\___||___/\___\___/

     CyRecon - Automated Recon Toolkit
     Author: Nikhil Bhor
    """)

def main_menu():
    global all_results, last_vulns

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        banner()
        print("Choose a module:\n")
        print("1. 🌐 Subdomain Scanner with AI Detection")
        print("2. 📡 AI Port Scanner")
        print("3. 📂 AI Directory Brute-Forcer")
        print("4. 🧠 AI Vulnerability Matcher")
        print("5. 📝 Export Full Report (JSON + PDF)")
        print("6. 📸 Capture Subdomain Screenshots")
        print("7. ❌ Exit")

        choice = input("\nEnter your choice (1-7): ").strip()

        if choice == "1":
            domain = input("\nEnter target domain (e.g., example.com): ").strip()
            results = subdomains.scan_subdomains(domain)
            all_results["subdomains"] = results
            if results:
                print("\n✅ Scan Complete. Found Subdomains:")
                for res in results:
                    print(f" - {res['url']} [{res['status']}] ({res['ip']}) - AI: {res['ai_label']}")
            else:
                print("\n[!] No live subdomains found.")
            input("\nPress Enter to return to menu...")

        elif choice == "2":
            ip = input("\nEnter target IP (e.g., 192.168.1.1): ").strip()
            results = portscanner.scan_ports(ip)
            all_results["ports"] = results
            if not results:
                print("\n[!] No open ports found.")
            input("\nPress Enter to return to menu...")

        elif choice == "3":
            target = input("\nEnter target domain or IP (e.g., example.com): ").strip()
            results = dirscanner.scan_directories(target)
            all_results["dirs"] = results
            if results:
                print("\n✅ Discovered Directories:")
                for res in results:
                    print(f" - {res['url']} [{res['status']}] - AI: {res['ai_label']} {res['reason']}")
            else:
                print("\n[!] No valid directories found.")
            input("\nPress Enter to return to menu...")

        elif choice == "4":
            print("\n[+] Running all scans for vulnerability analysis...\n")
            domain = input("Enter domain (e.g., example.com): ").strip()
            ip = input("Enter IP (e.g., 192.168.1.1): ").strip()

            sub_res = subdomains.scan_subdomains(domain)
            port_res = portscanner.scan_ports(ip)
            dir_res = dirscanner.scan_directories(domain)

            aggregated = {
                "subdomains": sub_res,
                "ports": port_res,
                "dirs": dir_res
            }

            all_results = aggregated
            suggestions = vulnmatcher.match_vulnerabilities(aggregated)
            last_vulns = suggestions

            if suggestions:
                print("\n🧠 AI Vulnerability Warnings:\n")
                for s in suggestions:
                    print(f"Target: {s['target']}\nRisk:   {s['risk']}\nLabel:  {s['ai_label']}\n")
            else:
                print("\n✅ No obvious vulnerabilities detected.")
            input("\nPress Enter to return to menu...")

        elif choice == "5":
            if not all_results:
                print("[!] Please run a scan first (Options 1–4).")
            else:
                reportgen.save_json_report(all_results)
                reportgen.save_pdf_report(all_results, last_vulns)
            input("\nPress Enter to return to menu...")

        elif choice == "6":
            if not all_results.get("subdomains"):
                print("[!] No subdomain scan results found. Run Option 1 first.")
            else:
                screenshooter.take_screenshots(all_results["subdomains"])
            input("\nPress Enter to return to menu...")

        elif choice == "7":
            print("\nGoodbye!\n")
            break

        else:
            input("\nInvalid option. Press Enter to retry...")

if __name__ == "__main__":
    main_menu()
