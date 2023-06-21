from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync
import urllib.parse
import urllib.robotparser as rb
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import requests


class scrapeIt:
    def __init__(self, targetURL) -> None:
        pass

    # The function uses the request library to get the response headers, and checks for content type
    def create_session(self, userAgent, url):
        headers = {'User-Agent': userAgent}
        session = requests.Session()
        session.verify = False
        adapter = HTTPAdapter(max_retries=Retry(
            total=2, connect=2, read=1, backoff_factor=0.5))
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        head = session.head(url, timeout=3.05 * 2,
                            headers=headers, allow_redirects=True)
        content_type = head.headers.get('Content-Type', '').lower()
        page_content = 'HTML' if 'html' in content_type else 'PDF' if 'pdf' in content_type else content_type
        return session, page_content

    # The function uses the playwright library that uses a headless browser and gets the HTML conent of the website
    def get_page_HTML(self) -> str:

        with sync_playwright() as pw:
            # create browser instance
            browser = pw.chromium.launch()

            # create context so that we can define page properties like viewport dimensions
            context = browser.new_context(
                viewport={"width": 1920, "height": 1080})

            # create page aka browser tab which we'll be using to do everything
            page = context.new_page()
            stealth_sync(page)

            # go to the target page
            page.goto(url, wait_until='domcontentloaded')

            # take a screen shot
            page.screenshot(path="screenshots.png")

            # close the browser
            browser.close()

            # return the page
            return page.content()

    # Function that extracts if permission to scrap is included in robots.txt file of the website
    def is_scraping_allowed(self, userAgent, session, url) -> bool:

        # robots.txt file could be getched using URL -> 'url_of_website' + '/robots.txt'
        robots_txt_url = urllib.parse.urljoin(url, '/robots.txt')
        rp = rb.RobotFileParser()

        # get the reponse by a get request from the target website
        response = session.get(
            robots_txt_url, timeout=3, allow_redirects=False)

        # parse the reponse
        content = response.content.decode(
            "utf-8").splitlines()
        rp.parse(content)

        # the can_fetch function of RobotFileParser returns true if the userAgent can scrap website data else false
        scraping_allowed = rp.can_fetch(userAgent, url)

        # return the boolen value
        return scraping_allowed

    def get_HTML_content(self):
        pass

    def show_page_content(self):
        pass


userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
url = "https://constitutioncenter.org/media/files/constitution.pdf"
page = scrapeIt(url)
session, page_content = page.create_session(userAgent, url)
print(f"Page Content is : {page_content}")
print(
    f"Is Scraping Allowed : {page.is_scraping_allowed(userAgent, session, url)}")
if page.is_scraping_allowed(userAgent, session, url):
    pass
    print(page.get_page_HTML())
