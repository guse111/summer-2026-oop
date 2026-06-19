import aiohttp
import asyncio
import json
import time
from datetime import datetime

async def check_site(url):
    try:
        start = time.time()
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://{url}", timeout=5) as response:
                elapsed = time.time() - start
                return {
                    "url": url,
                    "status": response.status,
                    "time": round(elapsed, 2),
                    "available": True
                }
    except Exception as e:
        return {
            "url": url,
            "status": None,
            "time": None,
            "available": False
        }

async def main():
    start = time.time()
    sites = ["google.com", "github.com", "youtube.com", "chat.qwen.ai", "wttr.in", "mail.yandex.ru", "yandex.ru", "mail.google.com", "vk.com", "telegram.org", "boosty.to", "www.dns-shop.ru", "rutracker.ru"]
    results = await asyncio.gather(*(check_site(url) for url in sites))
    with open("results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    available = sum(1 for r in results if r["available"])
    print(f"\nДоступно: {available}/{len(sites)}")
    print(f"Время выполнения: {time.time() - start:.2f} сек")



asyncio.run(main())