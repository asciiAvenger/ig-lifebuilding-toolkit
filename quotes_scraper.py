import requests
from bs4 import BeautifulSoup
import re
import json

class QuotesScraper:

    url = 'https://www.goodreads.com/quotes/tag/inspirational?page={}'
    verbose = False

    def __init__(self, verbose=False):
        self.verbose = verbose

    def scrape(self, output, start_page=1, end_page=50, clean=True):
        quotes = []
        pattern = re.compile(r'\".+\"')

        for page_num in range(start_page, end_page+1):
            if self.verbose:
                print('Fetching page {}'.format(page_num))
            page = requests.get(self.url.format(page_num))

            html = str(page.content).replace('&ldquo;', '"').replace('&rdquo;', '"')

            soup = BeautifulSoup(html, 'html.parser')

            quote_divs = soup.findAll('div', {'class': 'quoteText'})

            for div in quote_divs:
                match = pattern.findall(div.text)[0]
                match = match.replace('"', '').replace('\\', '')
                quotes.append(match)

        # clean quotes
        for i, quote in enumerate(quotes):
            quotes[i] = quote.replace('xe2x80x99', '\'')
            if 'xd' in quote or '2x' in quote:
                del quotes[i]

        with open(output, 'w') as f:
            if self.verbose:
                print('Writing {}'.format(output))
            json.dump(quotes, f)
