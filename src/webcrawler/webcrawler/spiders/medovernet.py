import scrapy
from datetime import datetime
from urllib.parse import urlparse

class MedovernetSpider(scrapy.Spider):
    name = 'medovernet'
    allowed_domains = ['med.over.net']
    start_urls = ['http://med.over.net/']
    minimal_chars_allowed = 10
    
    custom_settings = {
        'FEED_URI': '../../../data/output_medovernet.xml'
    }

    def parse(self, response):
        
        posts = response.css('.forum-post__content ::text').getall()
    
        # Extracting the domain from the URL
        domain = urlparse(response.url).netloc        

        # Getting the current timestamp        
        current_time = datetime.now().isoformat()
        
        # Processing extracted content
        for post in posts:
            post = post.strip()
            if post and len(post) >= self.minimal_chars_allowed:
                yield {
                    'content': post,
                    'timestamp': current_time,  # ISO 8601 format timestamp
                    'url': response.url,  # URL of the page where the post was found
                    'domain': domain  # Domain of the page
                }

        # Extracting links and yielding new requests
        links = response.css('a::attr(href)').getall()
        for link in links:
            full_url = response.urljoin(link)
            if any(domain in full_url for domain in self.allowed_domains):
                yield scrapy.Request(full_url, callback=self.parse)


