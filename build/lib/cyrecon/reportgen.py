import json
from datetime import datetime
from fpdf import FPDF
import os

def save_json_report(results, output_dir="reports"):
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "results.json")
    with open(path, "w") as f:
        json.dump(results, f, indent=4)
    print(f"[+] JSON report saved to {path}")

def save_pdf_report(results, vulns, output_dir="reports"):
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "report.pdf")
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.set_text_color(30, 30, 30)
    pdf.cell(0, 10, "CyRecon Scan Report", ln=True, align="C")

    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Date: {datetime.now()}", ln=True)

    # Subdomains
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "\nSubdomains:", ln=True)
    pdf.set_font("Arial", size=10)
    for s in results.get("subdomains", []):
        pdf.multi_cell(0, 7, f"{s['url']} [{s['status']}] - AI: {s['ai_label']}")

    # Ports
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "\nOpen Ports:", ln=True)
    pdf.set_font("Arial", size=10)
    for p in results.get("ports", []):
        pdf.cell(0, 7, f"{p['port']} ({p['service']}) - AI: {p['ai_label']}", ln=True)

    # Directories
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "\nDiscovered Directories:", ln=True)
    pdf.set_font("Arial", size=10)
    for d in results.get("dirs", []):
        pdf.multi_cell(0, 7, f"{d['url']} [{d['status']}] - AI: {d['ai_label']} {d['reason']}")

    # Vulnerabilities
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "\nAI Vulnerability Matches:", ln=True)
    pdf.set_font("Arial", size=10)
    for v in vulns:
        pdf.multi_cell(0, 7, f"{v['target']} - {v['risk']} [{v['ai_label']}]")

    pdf.output(path)
    print(f"[+] PDF report saved to {path}")
