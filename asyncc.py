import asyncio
import urllib.request

async def fetch(url):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, urllib.request.urlopen, url)

async def main():
    urls = [
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/3",
        "https://httpbin.org/delay/1"
    ]
    tasks = [fetch(url) for url in urls]
    for task in asyncio.as_completed(tasks):
        response = await task
        content = response.read().decode('utf-8')
        print(f"Fetched: {content}")

if __name__ == "__main__":
    asyncio.run(main())
    
