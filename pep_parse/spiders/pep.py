import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        for link in response.css('table.pep-zero-table tbody a::attr(href)'):
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = ' '.join(response.css('h1.page-title ::text').getall()).strip()
        number, name = title.split('–', 1)
        status = response.xpath(
            '//dt[contains(normalize-space(), "Status")]'
            '/following-sibling::dd[1]//text()'
        ).get()
        data = {
            'number': number.strip().replace('PEP ', ''),
            'name': name.strip(),
            'status': status,
        }
        yield PepParseItem(data)
