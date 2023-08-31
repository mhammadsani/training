import time
import scrapy
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from .constants import BASE_URL, BUTTON_ID, COURSE_LINK, WIDTH, HEIGHT
from .credentials import EMAIL, USER, PASSWORD


class CodedamnSpider(scrapy.Spider):
    name = 'codedamn'
    
    def start_requests(self):
        yield scrapy.Request(
            'https://codedamn.com/login',
            callback=self.scrap_codedamn
        )
        
    def scrap_codedamn(self, response):
        driver = self.open_chrome(response.url)
        self.login(driver)
        self.solve_captcha()
        self.open_course(driver)
        self.expand_buttons(driver)
        video_links = self.get_video_links(driver, driver.page_source, response)
        self.wait()
        for video_title, link in video_links.items():
            yield {
                video_title: link
            }
        driver.close()
    
    def solve_captcha(self):
        time.sleep(120)
    
    def wait(self):
        time.sleep(300)
    
    def open_course(self, driver):
        driver.get(COURSE_LINK)
        time.sleep(2)
        
    def open_chrome(self, url):
        driver = webdriver.Chrome()
        driver.set_window_size(WIDTH, HEIGHT)
        driver.get(url)
        time.sleep(2)
        return driver
           
    def login(self, driver):
        email_input = driver.find_element(By.ID, 'email')
        password_input = driver.find_element(By.ID, 'password')
        login_button = driver.find_element(
            By.CSS_SELECTOR, BUTTON_ID
            )
        email_input.send_keys(USER[EMAIL])
        password_input.send_keys(USER[PASSWORD])
        login_button.click()
    
    def expand_buttons(self, driver):
        for number in range(8, 19, 2):
            try:
                button = driver.find_element(By.ID, f'headlessui-disclosure-button-:r{number}:')
                button.click()
            except NoSuchElementException:
                continue
            
        for asci in range(97, 123, 2):
            try:
                button = driver.find_element(By.ID, f'headlessui-disclosure-button-:r{chr(asci)}:')
                button.click()
                button = driver.find_element(By.ID, f'headlessui-disclosure-button-:r1{chr(asci)}:')
                button.click()
            except NoSuchElementException:
                continue
    
    def get_video_links(self, driver, initial_page_source, response):
        course_page_html = HtmlResponse(url=response.url, body=initial_page_source, encoding='utf-8')
        links = course_page_html.css('div.flex.justify-between.gap-4.py-2.text-sm div a::attr(href)').extract()
        return self.process_links(driver, links, response)
   
    def process_links(self, driver, links, response):       
        video_links = {} 
        for link_number in range(len(links)):
            page_link = BASE_URL + links[link_number]
            driver.get(page_link)
            time.sleep(10)
            initial_page_source = driver.page_source
            response = HtmlResponse(url=response.url, body=initial_page_source, encoding='utf-8')
            video_link = response.css('video#main-video-element source::attr(src)').get()
            titles = response.css('span.flex.items-center.space-x-2 span::text').extract()
            title = titles[link_number].replace('\xa0\xa0', '')
            video_links[title] = video_link
            self.download_video(driver, video_link)
        return video_links
        
    def download_video(self, driver, video_link):
        try:
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get(video_link)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        except Exception as e:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
