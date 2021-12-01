from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
driver = Chrome(executable_path='C:/Users/donov/Hacktiv_Assignment/web-scraping-python/chromedriver_win32/chromedriver.exe')
driver.get('https://www.tokopedia.com/p/handphone-tablet/handphone')
driver.execute_script("window.scrollTo(0, 1460)")

try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME,  "css-13l3l78"))
    )
    
finally:
    print(" Sukses? ")

# print(len(driver.find_elements(By.XPATH, "//div[@class = 'css-bk6tzz e1nlzfl3']")),'<=========')

data = driver.page_source
driver.quit()
soup = BeautifulSoup(data, "html.parser")

itemLists = soup.findAll("div", class_ = "css-bk6tzz")

output = []

for i, item in enumerate(itemLists):
    rating_counter = 0
    nama_produk = item.find("span", class_ = "css-1bjwylw").text
    gambar_produk = item.find("img")['src']
    harga_produk = item.find("span", class_ = "css-o5uqvq").text
    nama_toko = item.findAll("span", class_ = "css-1kr22w3")[1].text
    rating_produk = item.findAll("img", class_ = "css-177n1u3")
    for i, rating in enumerate(rating_produk):
        rating_counter += 1
    output.append([nama_produk,gambar_produk,harga_produk,nama_toko,rating_counter])

with open('bricksTest.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    heading = ['Nama Produk','Gambar Produk','Harga Produk','Nama Toko','Rating Produk']
    csv_writer.writerow(heading)
    for data in output:
        csv_writer.writerow(data)
