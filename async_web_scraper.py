import asyncio
import aiohttp
import sqlite3

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def scrape_website(url):
    html = await fetch_data(url)
    
    # Connect to SQLite database
    conn = sqlite3.connect('scraped_data.db')
    cursor = conn.cursor()

    # Insert scraped data into the database
    cursor.execute('INSERT INTO scraped_data (url, content) VALUES (?, ?)', (url, html))

    # Commit changes and close connection
    conn.commit()
    conn.close()

    print(f"Scraped and saved data from {url}")

async def main():
    # List of URLs to scrape
    urls = [
        'https://google.com',
        'https://youtube.com',
        'https://instagram.com',
        # Add more URLs as needed
    ]

    # Create tasks for scraping each website concurrently
    tasks = [scrape_website(url) for url in urls]

    # Gather results from all tasks
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
