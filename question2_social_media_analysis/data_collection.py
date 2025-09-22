import requests
from bs4 import BeautifulSoup
import time
import random
import csv
import json
import re


BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"
HEADERS = {"User-Agent": "Mozilla/5.0"}
MAX_RETRIES = 3
DELAY_RANGE = (1, 3)  # Random delay between requests (1–3 sec)

def fetch_page(url):
    """Fetch a web page with retry logic."""
    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url} (attempt {attempt+1}): {e}")
            time.sleep(2)  # wait before retry
    return None

def parse_books(html):
    """Extract book data from a single page, including category from detail page."""
    soup = BeautifulSoup(html, "html.parser")
    books = []

    for book in soup.select(".product_pod"):
        title = book.h3.a["title"]
        price = book.select_one(".price_color").text.strip("£")
        rating = book.p["class"][1]  # rating is stored in CSS class
        relative_link = book.h3.a["href"]
        book_link = "http://books.toscrape.com/catalogue/" + relative_link

        # Default values
        category = "Unknown"
        stock = 0  

        # Fetch detail page (needed for category + stock)
        book_html = fetch_page(book_link)
        if book_html:
            detail_soup = BeautifulSoup(book_html, "html.parser")

            # Extract category
            breadcrumb = detail_soup.select("ul.breadcrumb li a")
            if len(breadcrumb) >= 3:
                category = breadcrumb[2].text.strip()

            # Extract stock number
            stock_text = detail_soup.select_one(".instock.availability").get_text(strip=True)
            stock_match = re.search(r'\d+', stock_text)
            if stock_match:
                stock = int(stock_match.group())

        books.append({
            "title": title,
            "price": price,
            "stock": stock,
            "rating": rating,
            "link": book_link,
            "category": category
        })

        # Polite delay between each book detail request
        time.sleep(random.uniform(*DELAY_RANGE))

    return books

def scrape_books(max_pages=5):
    """Scrape books from multiple pages with delays."""
    all_books = []
    for page_num in range(1, max_pages + 1):
        url = BASE_URL.format(page_num)
        print(f"Scraping {url} ...")
        html = fetch_page(url)
        if not html:
            continue
        books = parse_books(html)
        if not books:
            break  # Stop if no books found (end of pagination)
        all_books.extend(books)
        time.sleep(random.uniform(*DELAY_RANGE))  # polite delay
    return all_books

def save_to_csv(data, filename="books.csv"):
    """Save scraped data to CSV file."""
    keys = data[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    scraped_data = scrape_books(max_pages=50)  # site has 50 pages
    print(f"Scraped {len(scraped_data)} books in total.")

    if scraped_data:
        save_to_csv(scraped_data)  # Save results
        print("Data saved to books.csv")

print(scraped_data[:5])
