import pandas as pd
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
temp_df = pd.DataFrame({'song_name':[], 'artist_name':[], 'release_date':[], 'song_genre':[]})

# 위에서 50개
for page in range(1, 11):
    driver.refresh()
    list_btn = driver.find_elements(By.CSS_SELECTOR, 'a.btn.button_icons.type03.song_info')

    for i in range(len(list_btn)):
        list_btn[i].click()
        driver.implicitly_wait(5)

        song_name = driver.find_element(By.XPATH, '//*[@id="downloadfrm"]/div/div/div[2]/div[1]/div[1]').text
        artist_name = driver.find_element(By.XPATH, '//*[@id="downloadfrm"]/div/div/div[2]/div[1]/div[2]/a/span[1]').text
        release_date = driver.find_element(By.XPATH, '//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[2]').text
        song_genre = driver.find_element(By.XPATH, '//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[3]').text
        
        temp_df.loc[i] = [song_name, artist_name, release_date, song_genre]

        driver.back()
        driver.implicitly_wait(5)
    
    df = pd.concat([df, temp_df], ignore_index=True)

    if not page == 10:
        driver.find_element(By.XPATH, f'//*[@id="pageObjNavgation"]/div/span/a[{page}]').click()
        driver.implicitly_wait(5)
    


print(df)
