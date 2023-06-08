import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver as wd
from selenium.webdriver.common.by import By

options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = wd.Chrome(executable_path='C:\chromedriver', options=options)
driver.maximize_window()

URL = 'https://www.melon.com/genre/song_list.htm?gnrCode=GN0100'
driver.get(URL)

# 노래 정보 dataframe
df = pd.DataFrame({'song_name':[], 'artist_name':[], 'release_date':[], 'song_genre':[]})

# 위에서 50개
for i in range(50):
    driver.find_element(By.XPATH, '//*[@id="frm"]/div/table/tbody/tr[{0}]/td[4]/div/a'.format(i+1)).click()
    driver.implicitly_wait(2)

    song_name = driver.find_element(By.CLASS_NAME, 'song_name').text
    artist_name = driver.find_element(By.XPATH, '//*[@id="downloadfrm"]/div/div/div[2]/div[1]/div[2]/a/span[1]').text
    release_date = driver.find_element(By.XPATH, '//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[2]').text
    song_genre = driver.find_element(By.XPATH, '//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[3]').text

    df.loc[i] = [song_name, artist_name, release_date, song_genre]

    driver.back()


print(df)