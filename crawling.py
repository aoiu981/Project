import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver as wd
from selenium.webdriver.common.by import By

options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = wd.Chrome(executable_path='C:\chromedriver', options=options)
driver.maximize_window()

URL = 'https://www.melon.com/genre/song_list.htm?gnrCode=GN0100'
driver.get(URL)

# driver.find_element(By.XPATH, '//*[@id="frm"]/div/table/tbody/tr[1]/td[4]/div/a').click()
# driver.implicitly_wait(2)

html = driver.page_source
soup = bs(html, 'lxml')

song_bs = soup.select('#downloadfrm > div > div > div.entry > div.info > div.artist > a')
# song_bs = soup.select('#downloadfrm > div > div > div.entry > div.info > div.song_name')

print(song_bs)