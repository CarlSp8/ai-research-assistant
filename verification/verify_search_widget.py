from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        # Use absolute path
        file_path = os.path.abspath("verification/index.html")
        page.goto(f"file://{file_path}")
        # Wait for React to render
        page.wait_for_selector("div.text-base")
        page.screenshot(path="verification/search_widget_loading.png")
        print(f"Screenshot saved to {os.path.abspath('verification/search_widget_loading.png')}")
        browser.close()

if __name__ == "__main__":
    run()
