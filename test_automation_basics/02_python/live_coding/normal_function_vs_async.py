import time
import requests
import asyncio
import aiohttp

URL = "https://jsonplaceholder.typicode.com/todos/{}"
REQUESTS_COUNT = 100


def run_sync():
    print("--- 1. Starting Sync (One at a time) ---")
    start = time.time()

    for i in range(1, REQUESTS_COUNT + 1):
        current_url = URL.format(i)
        response = requests.get(current_url)
        print(f"Finished request {i}", response.text)

    end = time.time()
    return end - start


async def fetch_one(session, i):
    current_url = URL.format(i)
    async with session.get(current_url) as response:
        await (
            response.text()
        )  # wait for the result, but other tasks can run in the background
        print(f"Finished request {i}")


async def run_async():
    print("\n--- 2. Starting Async (All at once) ---")
    start = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(1, REQUESTS_COUNT + 1):
            task = fetch_one(session, i)
            tasks.append(task)
        await asyncio.gather(*tasks)

    end = time.time()
    return end - start


time_sync = run_sync()

time_async = asyncio.run(run_async())

print("\n==============================")
print(f"Sync took:  {time_sync:.2f} seconds")
print(f"Async took: {time_async:.2f} seconds")
print("==============================")
