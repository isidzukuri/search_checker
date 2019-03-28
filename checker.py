import mechanicalsoup
from termcolor import colored

class Checker:

  def __init__(self, params = {}):
    self.params = params

  def call(self):
    print(colored('parsing page...', 'green'))
    browser = self.get_browser()
    content = browser.get_current_page()
    self.parse_results(content)
    self.print_links()

    if len(self.links) > 0:
      print(colored('Everything works', 'green'))
    else:
      print(colored('Results list empty', 'red'))


  def print_links(self):
    for link in self.links:
      print(link.text, '->', link.attrs['href'])


  def parse_results(self, content):
    self.links = []

    for book in content.select('.book_item'):
      self.links += book.select('a:nth-of-type(1)')


  def get_browser(self):
    self.browser = mechanicalsoup.StatefulBrowser()
    self.browser.open("https://findbook.in.ua/search?word=%D1%87%D0%BE%D1%80%D0%BD%D0%B8%D0%B9")

    return self.browser


