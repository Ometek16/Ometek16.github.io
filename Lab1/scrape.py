from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json


# Initialize the webdriver (ensure the appropriate driver is installed)
driver = webdriver.Chrome()

# Navigate to the target website
driver.get("https://leetcode.com/u/Ometek/")

# Wait for JavaScript to render the dynamic content
x = input()

# Get the fully rendered page source
html_content = driver.page_source

# (Optional) Use BeautifulSoup to parse the HTML
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')


# open a json object
data = []

# print all class="mt-6" text line by line and image source
for div in soup.find_all('div', class_='mt-6'):
	div2 = list(div.children)[0]
	div3 = list(div2.children)[1]
 
	locdata = []
	for div4 in div3.find_all('div'):
		locdata.append(div4.text)

	for img in div.find_all('img'):
		locdata.append(img['src'])
  
	if locdata[2][0] == '/':
		locdata[2] = "https://leetcode.com" + locdata[2]
  
	dct = {
		"Badge Name": locdata[0],
		"Date": locdata[1],
		"img": locdata[2]
	}
 
	data.append(dct)
 
# save the json object to a file
with open('data.json', 'w') as f:
	json.dump(data, f, indent=4)

driver.quit()