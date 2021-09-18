import time
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

#chromedriver_path= r"C:\Users\Admin\chrome_driver\chromedriver.exe"
#driver = webdriver.Chrome(executable_path=chromedriver_path) #webdriver.Chrome(executable_path=r'C:/path/to/chromedriver.exe')
url = "https://summerofcode.withgoogle.com/organizations/?sp-page=6"
driver.get(url)
time.sleep(15) #if you want to wait 15 seconds for the page to load
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')
orgs = soup.find_all('div', class_ = 'organization-card__name font-black-54')
print(orgs)
