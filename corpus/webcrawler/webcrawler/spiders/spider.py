import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['med.over.net']
    start_urls = ['http://med.over.net/']

    def parse(self, response):
        posts = response.css('.forum-post__content ::text').getall()
        print(len(posts))
        
        # Processing extracted content
        for post in posts:
            # Here you can further process each post if needed
            # For example, you can yield a dictionary containing the post content
            yield {
                'content': post.strip()
            }


    # class selector med.over.net: forum-post__content
    # class selector slo-tech: content
