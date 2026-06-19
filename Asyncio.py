import aiohttp
import asyncio
import time

async def get_weather(city):
    url = f"https://wttr.in/{city}?format=1"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            return f"{city}: {text}"

async def main():
    start = time.time()
    results = await asyncio.gather(
        get_weather("Moscow"),
        get_weather("Vladivostok"),
        get_weather("Novorossiysk"),
        get_weather("Kalifornia"),
        get_weather("Artem")
    )
    for r in results:
        print(r)
    print(f"\nВремя: {time.time() - start:.2f} сек")

asyncio.run(main())


import requests
import time

def get_weather_sync(city):
    url = f"https://wttr.in/{city}?format=1"
    response = requests.get(url)
    return f"{city}: {response.text}"

start = time.time()

print(get_weather_sync("Moscow"))
print(get_weather_sync("Vladivostok"))
print(get_weather_sync("Novorossiysk"))
print(get_weather_sync("Kalifornia"))
print(get_weather_sync("Artem"))


print(f"\nВремя синхронное: {time.time() - start:.2f} сек")