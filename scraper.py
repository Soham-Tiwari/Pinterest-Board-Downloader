import time
import requests
import os
import re
from playwright.sync_api import sync_playwright

def download_pinterest_board(board_url, output_folder="pinterest_downloads"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) 
        context = browser.new_context()
        page = context.new_page()
        page.goto(board_url)
        
        print("\n*** ACTION REQUIRED ***")
        print("Log in to Pinterest. Once you see the board, click here and press ENTER.")
        input("Press ENTER to start...\n")

        image_urls = set()
        
        print("Starting scroll (I will ignore errors now)...")
        
        while True:
            try:
                # 1. Scroll
                page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                time.sleep(3) # Wait for images to load
                
                # 2. Grab images
                images = page.locator("img").all()
                for img in images:
                    src = img.get_attribute("src")
                    if src and "i.pinimg.com" in src:
                        if any(ext in src for ext in [".mp4", ".gif", "video"]):
                            continue
                        high_res_url = re.sub(r'/\d+x/', '/originals/', src)
                        image_urls.add(high_res_url)
                
                # 3. Check if height changed
                current_height = page.evaluate("document.body.scrollHeight")
                # If we've scrolled a few times and the height hasn't changed, we are done
                # (Simple check: break if we have 500+ images or just let user stop it)
                print(f"Found {len(image_urls)} unique images so far...")
                
            except Exception:
                # THIS IS THE FIX: Instead of crashing, we just wait and try the loop again.
                print("Page refreshed, retrying...")
                time.sleep(2)
                continue

        # (To stop the script, just close the browser window when you are satisfied)

# --- RUN ---
TARGET_BOARD = " https://uk.pinterest.com/etoilez/fits/ " 
download_pinterest_board(TARGET_BOARD)