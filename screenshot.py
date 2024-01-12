import asyncio
import os
from playwright.async_api import async_playwright

async def main():
    # Define the folder path where screenshots will be saved
    folder_path = "screenshots"

    # Check if the folder exists, if not, create it
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Initialize Playwright
    async with async_playwright() as p:
        # Launch the Chromium browser in non-headless mode (visible)
        browser = await p.chromium.launch(headless=False)

        # Create a new page in the browser
        page = await browser.new_page()

        # Navigate to the specified URL
        await page.goto("put your URL here")

        # Wait for the presence of a specific selector on the page
        await page.wait_for_selector("td.BodyTextBlack")

        # Find all elements on the page with the specified selector
        elements = await page.query_selector_all("td.BodyTextBlack")

        # Iterate through the found elements and take screenshots
        for i, element in enumerate(elements):
            # Save the screenshot of each element to a file
            await element.screenshot(path=f"{folder_path}/element_{i}.png")

        # Close the browser when done
        await browser.close()

# Run the asynchronous event loop with the main function
asyncio.run(main())
