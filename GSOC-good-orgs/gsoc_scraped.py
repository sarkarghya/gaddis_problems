import time
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install()) #to just make it work anywhere

#chromedriver_path= r"C:\Users\Admin\chrome_driver\chromedriver.exe"
#driver = webdriver.Chrome(executable_path=chromedriver_path) #webdriver.Chrome(executable_path=r'C:/path/to/chromedriver.exe')
url = "https://summerofcode.withgoogle.com/organizations/?sp-page=6"
driver.get(url)
time.sleep(15) #if you want to wait 15 seconds for the page to load
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')
orgs = soup.find_all('md-card', class_ = 'organization-card _md md-soc-theme flex') #find returns list, attrs returns dict
url_ids = [data.attrs['data-id'] for data in orgs]