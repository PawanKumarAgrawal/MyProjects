import asyncio
import os
import aiofiles
import logging
import urllib.parse
from crawl4ai import AsyncWebCrawler

# Folder to store all markdown files
OUTPUT_FOLDER = "extracted_pages"

# Ensure the folder exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="crawler_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Rate limiting: Maximum requests per second
MAX_REQUESTS_PER_SECOND = 2
REQUEST_DELAY = 1 / MAX_REQUESTS_PER_SECOND

# Custom User-Agent header
CUSTOM_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

async def fetch_and_save_page(url, index):
    """Fetch page content and save to a markdown file."""
    try:
        async with AsyncWebCrawler(headers=CUSTOM_HEADERS) as crawler:
            result = await crawler.arun(url=url, screenshot=False)
            
            if not result:
                logging.error(f"Failed to fetch: {url}")
                print(f"Failed to fetch: {url}")
                return

            # # Ensure correct method is used to access links
            # links_data = result.links  # Use the correct attribute or method
            
            text = result.links.get('text', 'No text')
            print(text)
            content = result.markdown
            filename = os.path.join(OUTPUT_FOLDER, f"page_{index}.md")

            async with aiofiles.open(filename, "w", encoding="utf-8") as f:
                await f.write(f"# Extracted Content from {url}\n\n{text}\n\n{content}")

            # print(result)
            print(f"Saved: {filename}")

        await asyncio.sleep(REQUEST_DELAY)  # Rate limiting inside function
    except Exception as e:
        logging.error(f"Error fetching {url}: {e}", exc_info=True)
        print(f"Error fetching {url}: {e}")





async def main():
    start_url = "https://us.pg.com/annualreport2024/"

    try:
        async with AsyncWebCrawler(headers=CUSTOM_HEADERS) as crawler:
            result = await crawler.arun(url=start_url, screenshot=True)

        if not result or not hasattr(result, "links"):
            logging.error("Failed to fetch the start URL or no links found.")
            print("Failed to fetch the start URL or no links found.")
            return
        
        links = result.links.get("internal", [])
        
        if not links:
            logging.warning("No internal links found.")
            print("No internal links found.")
            return

        tasks = []
        for index, link in enumerate(links):
            href = link.get("href", "").strip()
            
            if not href:
                continue

            full_url = urllib.parse.urljoin(start_url, href)  # Safer URL handling
            tasks.append(fetch_and_save_page(full_url, index))

        await asyncio.gather(*tasks)  # Run all requests asynchronously

    except Exception as e:
        logging.error(f"Error in main function: {e}", exc_info=True)
        print(f"Error in main function: {e}")

if __name__ == "__main__":
    asyncio.run(main())
