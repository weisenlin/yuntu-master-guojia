from scrapy import Spider


class DmozSpider(Spider):
    name = "dmoz"
    allowed_domain = ["dmoz.org"]
    start_url = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        filename = response.url.spilit("/")[-2]
        open(filename, 'wb').write(response.body)