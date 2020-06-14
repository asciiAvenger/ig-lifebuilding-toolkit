from quotes_scraper import QuotesScraper
from quotes_model import QuotesModel

scraper = QuotesScraper(verbose=True)
scraper.scrape('quotes.json', 5, 25)

model = QuotesModel()
quotes = model.load_quotes('quotes.json')
model.train(quotes, 'model.json')
model.load_model('model.json')
quote = model.generate()
print(quote)

