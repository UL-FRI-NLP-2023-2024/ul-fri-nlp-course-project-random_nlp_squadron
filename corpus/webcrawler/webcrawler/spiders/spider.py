import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['med.over.net']
    start_urls = ['http://med.over.net/']

    def parse(self, response):
        print(response.status)
        print("Here")
        posts = response.css('.forum-post__content ::text').getall()
        print(len(posts))
        print(self)
        
        # Processing extracted content
        for post in posts:
            # Here you can further process each post if needed
            # For example, you can yield a dictionary containing the post content
            yield {
                'content': post.strip()
            }

        # Extracting links and yielding new requests
        links = response.css('a::attr(href)').getall()  # This assumes all links are contained in 'a' tags and are of interest
        for link in links:
            full_url = response.urljoin(link)  # Ensures the link is a complete URL
            if "med.over.net" in full_url:  # Optional: additional check to stay within the domain
                yield scrapy.Request(full_url, callback=self.parse)


    # class selector med.over.net: forum-post__content
    # class selector slo-tech: content
