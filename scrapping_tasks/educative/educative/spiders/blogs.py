import scrapy
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from playwright._impl._api_types import TimeoutError
from .constants import (
    URL, TOTAL_PAGES, BLOG_ID, SCROLL_HEIGHT, BLOGS_CLASS
    )
from ..items import EducativeItem


class EducativeBlogScraper(scrapy.Spider):
    name = 'educative_blog_scraper'
    
    def start_requests(self):
        yield scrapy.Request(
            URL,
            meta={
                'playwright': True,
                'playwright_include_page': True,
                'proxy': '116.58.62.58'
            },
            errback=self.close_page
        )

    async def parse(self, response):
        page = response.meta['playwright_page']
        for page_number in range(TOTAL_PAGES):
            try:
                blog_number = page_number * 8
                await page.wait_for_selector(f'{BLOG_ID}{blog_number}')
                await page.evaluate(SCROLL_HEIGHT)
            except TimeoutError:
                break
        html_content = await page.content()
        await page.close()
        return self.extract_blogs(html_content)
    
    def extract_blogs(self, html_content):
        response = Selector(text=html_content)
        blogs = response.css(BLOGS_CLASS)
        for blog in blogs:
            loader = ItemLoader(item=EducativeItem())
            loader.add_value('blog_title', blog.css("a div.h-64 div.mt-4 p.m-0::text").get())
            loader.add_value('blog_link', blog.css("a::attr(href)").get())
            loader.add_value('blog_summary', blog.css("div#reader-blog-summary::text").get())
            loader.add_value('blog_image_link', blog.css('img::attr(src)').get())
            loader.add_value('blog_publish_date', blog.css("div#read-blogInfo-publishDate"))
            loader.add_value('author_name', blog.css("div.body-small::text").get())
            yield loader.load_item()
                  
    async def close_page(self, error):
        page = error.request.meta['playwright_page']
        print("Following Error Occured ", error)
        await page.close()
