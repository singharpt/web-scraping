from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync


class scrapeIt:
    def __init__(self) -> None:
        pass

    def get_page_HTML(self, target_URL):
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
            page.goto(target_URL, wait_until='domcontentloaded')

            # take a screen shot
            page.screenshot(path="screenshots.png")

            # return the page
            return page.content()

    def get_HTML_content(self):
        pass

    def show_page_content(self):
        pass


page = scrapeIt()
page = page.get_page_HTML(
    'https://scrapfly.io/blog/web-scraping-with-playwright-and-python/')
print(page)
