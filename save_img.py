import requests
from bs4 import BeautifulSoup
import urllib


# get a webpage html
def download(url):
	
	page = None
	
	try:
	
		response = requests.get(url)
	
		page = response.text
	
	except requests.exceptions.RequestException as e:
	
		print('Download error:', e.reason)
	
	return page


wikipedia_url = 'https://en.wikipedia.org'

url = wikipedia_url + '/wiki/Brazil'

html = download(url)

soup = BeautifulSoup(html, 'html.parser')

# find the <a> tags with class image to get the links to the page to see the image big 
images = soup.find_all('a', {'class':'image'})

for img in images:
	
	# link of the bigger image
	link = wikipedia_url + img.get('href')
	
	print(link)	
	
	# get the html of the page of the bigger image
	img_data_html = download(link)
	
	img_data = BeautifulSoup(img_data_html, 'html.parser')
	
	# get the div that contains the link to the original image
	img_download_div = img_data.find('div', {'class':'fullMedia'})
	
	#link of the original image
	img_a = img_download_div.find('a')
	
	img_href = img_a.get('href')
	
	print("https:"+img_href)
	
	# download the image
	urllib.urlretrieve("https:"+img_href, urllib.quote_plus(img_href[-100:]))

