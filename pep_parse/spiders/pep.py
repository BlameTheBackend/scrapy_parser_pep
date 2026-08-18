import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import PEP_NAME, PEP_ALLOWED_DOMAINS, PEP_START_URLS


class PepSpider(scrapy.Spider):
    name = PEP_NAME
    allowed_domains = PEP_ALLOWED_DOMAINS
    start_urls = PEP_START_URLS

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
