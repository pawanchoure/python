import requests
import concurrent.futures
import time

def get_wiki_page_existence(wiki_page_url, timeout=10):
    response = requests.get(url=wiki_page_url, timeout=timeout)

    page_status = "unknown"
    if response.status_code == 200:
        page_status = "exists"
    elif response.status_code == 404:
        page_status = "does not exist"

    time.sleep(5)
    return wiki_page_url + " - " + page_status


wiki_page_urls = [
    "https://en.wikipedia.org/wiki/Ocean",
    "https://en.wikipedia.org/wiki/Island",
    "https://en.wikipedia.org/wiki/this_page_does_not_exist",
    "https://en.wikipedia.org/wiki/Shark",
    "https://en.wikipedia.org/wiki/Ocean",
    "https://en.wikipedia.org/wiki/Island",
    "https://en.wikipedia.org/wiki/this_page_does_not_exist",
    "https://en.wikipedia.org/wiki/Shark",
]
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    futures = []
    for url in wiki_page_urls:
        futures.append(
            executor.submit(
                get_wiki_page_existence, wiki_page_url=url, timeout=10
            )
        )
    for future in concurrent.futures.as_completed(futures):
        try:
            print(future.result())
        except requests.ConnectTimeout:
            print("ConnectTimeout.")
