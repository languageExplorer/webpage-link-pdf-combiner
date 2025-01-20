import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time


def get_internal_links(url):
    options = uc.ChromeOptions()
    # Run in headless mode
    options.headless = True
    driver = uc.Chrome(options=options)

    try:
        driver.get(url)
        # Allow JavaScript to load
        time.sleep(5)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        base_domain = urlparse(url).netloc

        internal_links = set()
        for link in soup.find_all('a', href=True):
            full_link = urljoin(url, link['href'])
            if urlparse(full_link).netloc == base_domain:
                internal_links.add(full_link)

        return sorted(list(internal_links))

    finally:
        driver.quit()
