import requests
import time
import os
from concurrent.futures import ThreadPoolExecutor

urls = [
    "https://www.python.org/",
    "https://www.wikipedia.org/",
    "https://www.github.com/",
    "https://www.stackoverflow.com/",
    "https://www.openai.com/"
]

os.makedirs("hasil_html", exist_ok=True)

def crawl(url):
    try:
        response = requests.get(url, timeout=10)
        filename = url.replace("https://", "").replace("http://", "").replace("/", "_") + ".html"
        with open(f"hasil_html/{filename}", "w", encoding="utf-8") as f:
            f.write(response.text)
        return {"url": url, "status": "berhasil"}
    except Exception as e:
        return {"url": url, "status": f"gagal ({e})"}

def crawl_single():
    start = time.time()
    results = [crawl(url) for url in urls]
    end = time.time()
    return results, round(end - start, 2)

def crawl_multi():
    start = time.time()
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(crawl, urls))
    end = time.time()
    return results, round(end - start, 2)
