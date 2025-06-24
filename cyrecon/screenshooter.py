import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

def take_screenshots(subdomains, output_dir="screenshots"):
    os.makedirs(output_dir, exist_ok=True)

    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1366,768")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--log-level=3")  # Suppress warnings

    # 👇 Set path to chromedriver.exe (same directory as this script)
    chromedriver_path = os.path.join(os.path.dirname(__file__), "chromedriver.exe")

    try:
        driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)
    except WebDriverException as e:
        print(f"[!] ChromeDriver error: {e}")
        print("    → Make sure chromedriver.exe is present in the same folder.")
        return

    print(f"\n📸 Starting screenshot capture for {len(subdomains)} subdomains...\n")

    for entry in subdomains:
        url = entry.get("url")
        if not url:
            continue
        try:
            print(f"[+] Capturing: {url}")
            driver.get(url)
            time.sleep(2)  # Allow time for full page load

            # Safe filename for saving
            fname = url.replace("http://", "").replace("https://", "").replace("/", "_")
            screenshot_path = os.path.join(output_dir, f"{fname}.png")

            driver.save_screenshot(screenshot_path)
            print(f"    → Screenshot saved: {screenshot_path}")

        except Exception as e:
            print(f"[!] Failed to capture {url} — {e}")

    driver.quit()
    print(f"\n✅ Done capturing {len(subdomains)} screenshots.")
