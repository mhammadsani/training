# import time
# import scrapy
# from scrapy.http import HtmlResponse
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.by import By
# from .constants import BUTTON_ID, COURSE_LINK
# from .credentials import EMAIL, PASSWORD, USER


# class CodedamnSpider(scrapy.Spider):
#     name = 'codedamn'
    
#     def start_requests(self):
#         yield scrapy.Request(
#             'https://codedamn.com/login',
#             callback=self.login
#         )
           
#     def login(self, response):
#         driver = webdriver.Chrome()
#         driver.set_window_size(1200, 800)
#         driver.get(response.url)
#         time.sleep(2)
        
#         email_input = driver.find_element(By.ID, 'email')
#         password_input = driver.find_element(By.ID, 'password')
#         login_button = driver.find_element(
#             By.CSS_SELECTOR, BUTTON_ID
#             )
#         email_input.send_keys(USER[EMAIL])
#         password_input.send_keys(USER[PASSWORD])
#         login_button.click()
#         time.sleep(120)
#         driver.get(COURSE_LINK)
#         time.sleep(2)
        
#         for number in range(8, 19, 2):
#             try:
#                 expand_button = driver.find_element(By.ID, f'headlessui-disclosure-button-:r{number}:')
#                 expand_button.click()
#             except Exception as e:
#                 print('=' * 100)
#                 print("Expand Button 1 :",e)
#                 print('=' * 100)
#                 continue

#         for number in range(97, 123, 2):
#             try:
#                 expand_button = driver.find_element(By.ID, f'headlessui-disclosure-button-:r{chr(number)}:')
#                 expand_button.click()
#                 expand_button = driver.find_element(By.ID, f'headlessui-disclosure-button-:r1{chr(number)}:')
#                 expand_button.click()
#             except Exception as e:
#                 print('=' * 100)
#                 print("Expand Button :",e)
#                 print('=' * 100)
#                 continue
    
#         initial_page_source = driver.page_source
#         response = HtmlResponse(url=response.url, body=initial_page_source, encoding='utf-8')
#         links = response.css('div.flex.justify-between.gap-4.py-2.text-sm div a::attr(href)').extract()
        
#         for link in range(len(links)):
#             video_link = 'https://codedamn.com' + links[link]
#             driver.get(video_link)
#             time.sleep(10)
#             initial_page_source = driver.page_source
#             response = HtmlResponse(url=response.url, body=initial_page_source, encoding='utf-8')
#             source_link = response.css('video#main-video-element source::attr(src)').get()
#             titles = response.css('span.flex.items-center.space-x-2 span::text').extract()
#             title = titles[link].replace('\xa0\xa0', '')
#             try:
#                 driver.execute_script("window.open('');")
#                 driver.switch_to.window(driver.window_handles[1])
#                 driver.get(source_link)
#                 driver.close()
#                 driver.switch_to.window(driver.window_handles[0])
#             except Exception as e:
#                 print('=' * 100)
#                 print("Execute script :", e)
#                 print('=' * 100)
#                 driver.close()
#                 driver.switch_to.window(driver.window_handles[0])
#                 yield {
#                     title: source_link if source_link is not None else f'{title}'
#                 }
                
#             yield {
#                 title: source_link if source_link is not None else f'{title}'
#             }
  
#     def closed(self, reason):
#         self.driver.quit()
