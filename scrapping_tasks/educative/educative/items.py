from scrapy import Item, Field
from itemloaders.processors import MapCompose, TakeFirst


def extract_publish_date(selector):
    selector = selector.css('div#read-blogInfo-publishDate::text')
    date_parts = [temp.get().strip() 
                  for temp in selector 
                  if not(any([temp.get().strip() == '', temp.get().strip()=='·']))] 
    if len(date_parts) == 1:
        date_parts = date_parts[0].split(" ")
        date_parts = [temp for temp in date_parts if not(any([temp.strip() == '', temp.strip()=='·']))]
    return '-'.join(pd for pd in date_parts)

# def extract_publish_date(selector):
#     date_parts = [
#         temp.strip() for temp in selector.css('div#read-blogInfo-publishDate::text')
#         if temp.strip() not in ['', '·']
#     ]
#     if len(date_parts) == 1:
#         date_parts = [temp for temp in date_parts[0].split(" ") if temp.strip() != '']
#     return '-'.join(date_parts)


def complete_link(href):
    BASE_URL = 'https://www.educative.io'
    return BASE_URL + href


class EducativeItem(Item):
    blog_title = Field(
        output_processor=TakeFirst()
    )
    blog_link = Field(
        input_processor=MapCompose(complete_link),
        output_processor=TakeFirst()
    )
    blog_summary = Field(
        output_processor=TakeFirst()
    )
    blog_image_link = Field(
        input_processor=MapCompose(complete_link),
        output_processor=TakeFirst()
    )
    blog_publish_date = Field(
        input_processor=MapCompose(extract_publish_date),
        output_processor=TakeFirst()
    )
    author_name = Field(
        output_processor=TakeFirst()
    )
