import asyncio
from pyppeteer import launch
import os

async def print_page_to_pdf(url, output_pdf_path):
    print(f"Loading {url} using headless Chrome...")

    # Launch headless Chromium with SSL errors ignored
    browser = await launch(headless=True, args=['--no-sandbox', '--ignore-certificate-errors'])
    page = await browser.newPage()

    # Ignore HTTPS certificate errors
    await page.setJavaScriptEnabled(True)

    # Try visiting the page
    try:
        # Wait until the page is fully loaded
        await page.goto(url, {'waitUntil': 'networkidle2'})
    except Exception as e:
        print(f"⚠️ Warning: Page load issue: {e}")

    print("Scrolling down to load dynamic content...")
    # Adjust number of scrolls if needed
    for _ in range(10):
        await page.evaluate("window.scrollBy(0, document.body.scrollHeight)")
        # Allow time for new content to load
        await asyncio.sleep(1)

    print("Waiting for final elements to load...")
    # Give extra time for images or scripts
    await asyncio.sleep(2)

    # Scroll slowly upwards
    print("Scrolling slowly upwards to ensure all content is loaded...")
    # Adjust number of scrolls if needed
    for _ in range(10):
        # Scroll up by 10% of the page height
        await page.evaluate("window.scrollBy(0, -document.body.scrollHeight / 10)")
        # Allow time for content to settle
        await asyncio.sleep(1)

    print("Saving page as PDF...")
    await page.pdf({'path': output_pdf_path, 'format': 'A4'})

    await browser.close()

    # Check if the PDF was created
    if os.path.exists(output_pdf_path):
        print(f"✅ PDF saved successfully: {output_pdf_path}")
    else:
        print("⚠️ PDF file was not created.")
