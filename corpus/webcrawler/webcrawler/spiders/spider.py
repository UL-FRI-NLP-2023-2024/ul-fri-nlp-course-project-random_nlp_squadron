import scrapy
from datetime import datetime


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['med.over.net']
    start_urls = ['https://med.over.net/']

    def parse(self, response):

        posts = response.css('.forum-post__content ::text').getall()

        # Getting the current timestamp
        current_time = datetime.now().isoformat()
        
        # Processing extracted content
        for post in posts:
            # Here you can further process each post if needed
            # For example, you can yield a dictionary containing the post content
            yield {
                'content': post.strip(),
                'timestamp': current_time,  # ISO 8601 format timestamp
                'url': response.url  # URL of the page where the post was found
            }

        # Extracting links and yielding new requests
        links = response.css('a::attr(href)').getall()  # This assumes all links are contained in 'a' tags and are of interest
        for link in links:
            full_url = response.urljoin(link)  # Ensures the link is a complete URL
            print(full_url)
            if any(domain in full_url for domain in self.allowed_domains):
                yield scrapy.Request(full_url, callback=self.parse)


    # class selector med.over.net: forum-post__content
    # class selector slo-tech: content
