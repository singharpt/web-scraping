# from playwright.sync_api import sync_playwright
# from playwright_stealth import stealth_sync
# import urllib.parse
# import urllib.robotparser as rb
# import requests
# from requests.adapters import HTTPAdapter
# from urllib3.util import Retry
# import requests


# class scrapeIt:
#     def __init__(self) -> None:
#         pass

#     def create_session(self, url):
#         h = requests.head(url)
#         header = h.headers
#         content_type = header.get('Content-Type', '').lower()
#         page_content = 'HTML' if 'html' in content_type else 'PDF' if 'pdf' in content_type else content_type
#         return page_content

#     def get_page_HTML(self) -> str:
#         with sync_playwright() as pw:

#             # create browser instance
#             browser = pw.chromium.launch()

#             # create context so that we can define page properties like viewport dimensions
#             context = browser.new_context(
#                 viewport={"width": 1920, "height": 1080})

#             # create page aka browser tab which we'll be using to do everything
#             page = context.new_page()
#             stealth_sync(page)

#             # go to the target page
#             page.goto(url, wait_until='domcontentloaded')

#             # take a screen shot
#             page.screenshot(path="screenshots.png")

#             # close the browser
#             browser.close()

#             # return the page
#             return page.content()

#     # Function extracts permission from the robots.txt file of the website

#     def get_robots_consent(self, userAgent, url) -> bool:
#         robots_txt_url = urllib.parse.urljoin(url, '/robots.txt')
#         rp = rb.RobotFileParser()
#         rp.set_url(robots_txt_url)
#         rp.read()
#         return rp.can_fetch(userAgent, url)

#     def get_HTML_content(self):
#         pass

#     def show_page_content(self):
#         pass


# userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
# url = "https://constitutioncenter.org/media/files/constitution.pdf"
# page = scrapeIt()
# page_content = page.create_session(url)
# print(f"Page Content is : {page_content}")
# print(f"Robots Response is : {page.get_robots_consent(userAgent, url)}")
# if page.get_robots_consent(userAgent, url):
#     pass
#     # print(page.get_page_HTML())
